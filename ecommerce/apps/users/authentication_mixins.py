from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class JWTAuthenticationMixin:
    user = None
    user_token_expired = False

    def get_user(self, request):
        jwt_authenticator = JWTAuthentication()
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            try:
                validated_token = jwt_authenticator.get_validated_token(auth_header.split()[1])
                self.user = jwt_authenticator.get_user(validated_token)
                return self.user
            except InvalidToken as e:
                self.user_token_expired = 'Token is invalid or expired' in str(e)
                return str(e)
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is not None:
            if isinstance(user, str):
                response = Response({'error': user, 'expired': self.user_token_expired},
                                    status=status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response

            if not self.user_token_expired:
                return super().dispatch(request, *args, **kwargs)

        response = Response({'error': 'No credentials provided', 'expired': self.user_token_expired},
                            status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response
