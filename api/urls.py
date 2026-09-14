from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/nouveau/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/modifier/', views.user_update, name='user_update'),
    path('users/<int:pk>/supprimer/', views.user_delete, name='user_delete'),
]