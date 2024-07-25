from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_user', views.crear_user, name='crear_user'),
    path('perfil', views.actualizar_usuario, name='perfil'),

    path('accounts/', include('django.contrib.auth.urls')),
]
