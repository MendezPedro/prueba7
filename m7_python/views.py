from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Usuario, Comuna, Inmueble
from .utilities import cleaned_data
# Create your views here.

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request):
    return redirect('crear_user')


# . Un nuevo usuario se debe poder:
# a. Lograr registrarse en la aplicación.
def crear_user(request):
    if request.method == 'POST':
        user = User.objects.create(
            username = request.POST['username'],
            password = 'clave inventada'
        )
        user.set_password(request.POST['password'])
        user.save()
        # data = cleaned_data(request.POST)
        # User.objects.create(**data)
        Usuario.objects.create(
            user = user,
            rut = request.POST['rut']
        )
        return redirect('perfil')
    else:
        return render(request,'crear_user.html')


# b. Actualizar sus datos.
# c. Poder identificarse como arrendatario o como arrendador
@login_required
def actualizar_usuario(request):
    user = request.user
    if request.method == 'POST':
        usuario = Usuario.objects.filter(user=user)
        data = cleaned_data(request.POST)
        usuario.update(**data)
        return redirect('perfil')
    else:
        usuario = Usuario.objects.get(user=user)
        return render(request, 'perfil.html',{'usuario':usuario})


# Un usuario tipo arrendatario debe poder:
# a. Listar las propiedades de diversas propiedades de una comuna específica.
@login_required
def inmueble_comuna2(request):
    user = request.user
    print(user)
    usuario = Usuario.objects.get(correo_electronico=user)
    print(usuario)
    if usuario.tipo_usuario == 'arrendatario':
        if request.method == 'POST':
            comuna = request.POST['comuna']
            comuna = Comuna.objects.get(comuna = comuna)
            inmuebles_comuna = Inmueble.objects.filter(comuna=comuna, disponible=True)#.filter(disponible=True)
            return render(request, 'inmueble_comuna.html',{'inmuebles_comuna':inmuebles_comuna})
        else:
            comunas = Comuna.objects.all()
            return render(request, 'listar_propiedades.html',{'comunas':comunas})
    else:
        comunas = Comuna.objects.all()
        return render(request, 'inmueble_comuna.html',{'comunas':comunas})
    
#################### hito #############################
# b. Poder generar una solicitud de arriendo a la propiedad.
@login_required
def solicitud_arriendo(request,id):
    inmueble = Inmueble.objects.filter(id=id)
    inmueble.update(
        solicitudes={
            f'solicitud_{request.user.username}':request.user.id
        },
        disponible=False
    )
    return redirect('inmueble_comuna')

    
# 3. Un usuario tipo arrendador debe poder:
# a. Publicar sus propiedades en una comuna determinada con sus
# características.
@login_required
def crear_inmueble(request):
    if request.method =='GET':
        inmuebles = Inmueble.objects.all()
        propietarios = Usuario.objects.all()
        comunas = Comuna.objects.all()
        print(propietarios)
        return render(request, 'crear_inmueble.html',{'inmuebles':inmuebles, 'propietarios':propietarios, 'comunas':comunas})
    else:
        print(request.POST)
        user = request.user
        print(user)
        comuna = Comuna.objects.get(id = request.POST['comuna'])
        data = cleaned_data(request.POST) | {'propietario': Usuario.objects.get(user=user), 'comuna': comuna}
        print(data)
        Inmueble.objects.create(**data)
        return redirect('crear_inmueble')


# b. Listar propiedades en el dashboard.
@login_required
def listar_inmueble(request,id):
    # user = request.user
    # usuario = Usuario.objects.get(correo_electronico=user)
    inmuebles = Inmueble.objects.filter(id=id)
    return render(request,'listar_inmueble.html',{'inmuebles':inmuebles})

@login_required
def listar(request):
    user = request.user
    usuario = Usuario.objects.get(correo_electronico=user)

    inmuebles = Inmueble.objects.filter(propietario=usuario)
    return render(request,'listar.html',{'inmuebles':inmuebles})


# c. Eliminar y editar sus propiedades.
@login_required
def eliminar_inmueble(request,id):
    Inmueble.objects.get(id=id).delete()
    return redirect('crear_inmueble')


@login_required
def editar_inmueble(request,id):
    if request.method == 'GET':
        inmueble = Inmueble.objects.get(id=id)
        return render(request,'editar_inmueble.html',{'inmueble':inmueble})
    else:
        inmueble = get_object_or_404(Inmueble, id=id)
        comuna = Comuna.objects.all()  
        # comuna = Comuna.objects.get(comuna = request.POST['comuna'])
        data = cleaned_data(request.POST)
        print(data)
        Inmueble.objects.filter(id=id).update(**data)
        return redirect('crear_inmueble')

# def editar_inmueble(request,id):
#     inmueble = get_object_or_404(Inmueble, id=id)
#     comuna = Comuna.objects.all()  
#     # comuna = Comuna.objects.get(comuna = request.POST['comuna'])
#     data = cleaned_data(request.POST) | {'comuna':comuna}
#     Inmueble.objects.filter(id=id).update(**data)
#     return redirect('listar_inmuebles')

###########################  hito  ##########################################
# d. Aceptar arrendatarios.
@login_required
def aceptar_arrendatarios(request):
    arrendatario = Usuario.objects.get(id=request.POST['arrendador_id'])
    inmueble = Inmueble.objects.filter(id=request.POST['inmueble_id'])
    inmueble.update(
        solicitud_arriendo='',
        arrendatario=arrendatario,
        disponible=False
    )
    return redirect('listar_inmuebles')


def inmueble_comuna(request):
    if request.method == 'POST':
        inmueble_comuna = Inmueble.objects.all()
        regiones = set()
        for region in inmueble_comuna:
            regiones.add(region.id)
        regiones = Comuna.objects.filter(id__in=regiones).order_by('nombre_comuna')


        region = request.POST['region']
        region = Comuna.objects.get(id = region)
        inmuebles = Inmueble.objects.filter(comuna=region).order_by('precio_arriendo')
        return render(request, 'inmueble_comuna.html', {'regiones':regiones, 'inmuebles':inmuebles})

    else:
        inmueble_comuna = Inmueble.objects.all()
        regiones = set()
        for region in inmueble_comuna:
            regiones.add(region.id)
        print(regiones)
        regiones = Comuna.objects.filter(id__in=regiones).order_by('nombre_comuna')
        return render(request, 'inmueble_comuna.html', {'regiones':regiones})
    

def fetch_data(request,id):
    region = Comuna.objects.get(comunaid=id)
    album = region.comuna_set.all()
    return JsonResponse(list(album.values('title', 'albumid')), safe = False)