from django.contrib import admin
from django.urls import path
from users.views import index, RegistroUsuario, UserList, UserDelete, UserAprove
from django.contrib.auth.views import LoginView,LogoutView,logout_then_login
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(),name="registrar"),
    path('logout',logout_then_login,name="logout"),
    path('listado_usuario',UserList.as_view(),name="lista_users"),
    path('eliminar_usuario/<pk>/',UserDelete.as_view(),name="eliminar_user"),
    path('aprobar_usuario/<pk>/',UserAprove.as_view(),name="aprobar_user")
]

