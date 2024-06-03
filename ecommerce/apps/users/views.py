from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from apps.users.authentication_mixins import JWTAuthenticationMixin
from apps.users.api.serializers import UserTokenSerializer

class UserToken(JWTAuthenticationMixin, APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user = UserTokenSerializer().Meta.model.objects.get(username=username)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        except UserTokenSerializer().Meta.model.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Credenciales enviadas incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

class Login(JWTAuthenticationMixin,TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                user_serializer = UserTokenSerializer(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Exitoso.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(JWTAuthenticationMixin, APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if request.user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                return Response({'message': 'Sesión cerrada exitosamente.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Token de actualización no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

