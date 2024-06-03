from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

# Vista para listar y crear usuarios
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para operaciones CRUD en un usuario específico
class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk=None):
        user = self.get_object(pk)
        if user:
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        user = self.get_object(pk)
        if user:
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        user = self.get_object(pk)
        if user:
            user.delete()
            return Response({'message': 'User deleted successfully!'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
