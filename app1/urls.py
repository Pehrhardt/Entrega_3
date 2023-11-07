
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path("clientes/", clientes, name="clientes"),
    path ("fondos_inversion/", fondos_inversion, name="fondos"),
    path ("bonos/",bono, name='bonos'),
    path ("acciones/", accion , name='acciones'),
    path('buscar_fondos/', buscar_fondos, name='buscar_fondos'),

]

