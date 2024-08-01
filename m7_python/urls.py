from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('perfil', views.actualizar_usuario, name='perfil'),

    path('crear_user', views.crear_user, name='crear_user'),
    path('crear_inmueble', views.crear_inmueble, name='crear_inmueble'),
    path('editar_inmueble', views.editar_inmueble, name='editar_inmueble'),

    # path('listar_inmueble/<id>', views.listar_inmueble, name='listar_inmueble'),
    path('editar_inmueble/<id>/', views.listar_inmueble, name='editar_inmueble'),
    # path('editar_inmueble/<id>/', views.editar_inmueble, name='editar_inmueble'),


    path('listar', views.listar, name='listar'),
    path('inmueble_comuna', views.inmueble_comuna, name='inmueble_comuna'),
    
    path('fetch_data/<id>', views.fetch_data, name='fetch_data'),
    path('eliminar_inmueble', views.eliminar_inmueble, name='eliminar_inmueble'),


    path('eliminar_inmueble/<id>/', views.eliminar_inmueble, name='eliminar_inmueble'),
]

