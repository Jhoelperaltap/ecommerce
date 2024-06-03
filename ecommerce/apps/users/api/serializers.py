from rest_framework import serializers
from apps.users.models import User

# Serializer para representar el token de usuario
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')  # Campos a incluir en la representación

# Serializer para crear y actualizar usuarios, incluyendo todos los campos
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Incluir todos los campos del modelo de usuario
        extra_kwargs = {'password': {'write_only': True}}  # Hacer que el campo de la contraseña solo sea de escritura

    # Método para crear un nuevo usuario
    def create(self, validated_data):
        user = User(**validated_data)  # Crear una instancia de usuario con los datos validados
        user.set_password(validated_data['password'])  # Establecer la contraseña
        user.save()  # Guardar el usuario en la base de datos
        return user

    # Método para actualizar un usuario existente
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Extraer la contraseña de los datos validados si está presente
        updated_user = super().update(instance, validated_data)  # Actualizar los campos del usuario
        if password:
            updated_user.set_password(password)  # Actualizar la contraseña si fue proporcionada
            updated_user.save()  # Guardar los cambios
        return updated_user

    # Método para personalizar la representación de los datos del usuario
    def to_representation(self, instance):
        representation = super().to_representation(instance)  # Obtener la representación predeterminada
        representation.pop('password', None)  # Eliminar la contraseña de la representación
        return representation

# Serializer para listar usuarios con campos específicos
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Campos a incluir en la lista de usuarios

    # Método para personalizar la representación de la lista de usuarios
    def to_representation(self, instance):
        return {
            'id': instance['id'],  # ID del usuario
            'username': instance['username'],  # Nombre de usuario
            'email': instance['email'],  # Correo electrónico del usuario
        }
