from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente,fondos,bonos,acciones


def home(request):
    return render(request, "app1/index.html")

def clientes(request):
    if request.method == 'POST':
        nuevo_cliente = Cliente(nombre_cliente=request.POST['nombre_cliente'], apellido=request.POST['Apellido_cliente'], email=request.POST['email_cliente'])
        nuevo_cliente.save()
        return render(request, "app1/index.html") 
    
    return render(request, "app1/clientes.html")


def fondos_inversion(request):
    if request.method == 'POST':
        nuevo_fondo = fondos(nombre_fondo=request.POST['nombre_fondo'], cant_activos=request.POST['can_act'])
        nuevo_fondo.save()
        return render(request, "app1/index.html") 

    return render(request, "app1/fondos_inversion.html")

def bono(request):
    if request.method == 'POST':
        nuevo_bono = bonos(nombre_bonos=request.POST['nombre_bono'], ticket=request.POST['ticketn'],valor_nominal=request.POST['vn'], valor_mercado=request.POST['vm'],tir=request.POST['TIR'] )
        nuevo_bono.save()
        return render(request, "app1/index.html") 
     
    return render(request, "app1/bonos.html")

def accion(request):
    if request.method == 'POST':
        nuevo_accion = acciones(nombre_acciones=request.POST['nombre_accion'], ticket=request.POST['ticketa'],precio=request.POST['precio'] )
        nuevo_accion.save()
        return render(request, "app1/index.html") 
    return render(request, "app1/acciones.html")




def buscar_fondos(request):
    mensaje = ""

    if request.method == 'POST':
        nombre_fondo = request.POST.get('nombre_fondo')
        resultado = fondos.objects.filter(nombre_fondo=nombre_fondo).first()

        if resultado:
            mensaje = f'El fondo "{nombre_fondo}" se encuentra en nuestra BD con {resultado.cant_activos} activos en cartera.'
        else:
            mensaje = f'No se encontró ningún fondo con el nombre "{nombre_fondo}".'

    return render(request, 'app1/index.html', {'mensaje': mensaje})




