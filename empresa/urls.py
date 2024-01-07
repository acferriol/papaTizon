from django.contrib import admin
from django.urls import path
from empresa.views import EmpresaCreate,EmpresaList,EmpresaDelete,EmpresaUpdate


urlpatterns = [
    path('lista_empresas',EmpresaList.as_view(),name="lista_empresa"),
    path('crear_empresa',EmpresaCreate.as_view(),name="crear_empresa"),
    path('eliminar_empresa/<pk>/',EmpresaDelete.as_view(),name="eliminar_empresa"),
    path('editar_empresa/<pk>/',EmpresaUpdate.as_view(),name="editar_empresa")
]
