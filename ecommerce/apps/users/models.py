from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Gestor personalizado de usuarios
class UserManager(BaseUserManager):
    # Método auxiliar para crear usuarios
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe estar establecido')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Crear un usuario estándar
    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    # Crear un superusuario
    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

# Modelo personalizado de usuario
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)  # Campo de nombre de usuario único
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)  # Campo de correo electrónico único
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)  # Campo de nombre
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)  # Campo de apellidos
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)  # Imagen de perfil
    is_active = models.BooleanField(default=True)  # Estado de actividad del usuario
    is_staff = models.BooleanField(default=False)  # Indicador de si el usuario es miembro del personal
    historical = HistoricalRecords()  # Registro histórico de cambios
    
    objects = UserManager()  # Asignación del gestor de usuarios personalizado

    class Meta:
        verbose_name = 'Usuario'  # Nombre del modelo en singular
        verbose_name_plural = 'Usuarios'  # Nombre del modelo en plural

    USERNAME_FIELD = 'username'  # Campo utilizado para el login
    REQUIRED_FIELDS = ['email', 'name', 'last_name']  # Campos requeridos además del username

    def __str__(self):
        return f'{self.name} {self.last_name}'  # Representación en cadena del usuario
