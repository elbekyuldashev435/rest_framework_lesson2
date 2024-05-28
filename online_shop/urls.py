from django.urls import path
from .views import get_users, get_user, create_user, delete_user, update_user


urlpatterns = [
    path('get-users/', get_users, name='get-users'),
    path('get-user/<int:pk>/', get_user, name='get-user'),
    path('create-user/', create_user, name='create-user'),
    path('delete-user/<int:pk>/', delete_user, name='delete-user'),
    path('update-user/<int:pk>/', update_user, name='update-user')
]