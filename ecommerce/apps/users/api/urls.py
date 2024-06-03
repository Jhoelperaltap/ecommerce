from django.urls import path

from apps.users.api.api import UserAPIView, UserDetailView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name= 'users_view'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail_view'),
]
