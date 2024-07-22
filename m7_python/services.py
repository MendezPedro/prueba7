from m7_python.models import Inmueble, Usuario, Comuna


def get_all_inmuebles():
    inm = Inmueble.objects.all()
    return inm

def create_comuna(request):
    comuna = Comuna.objects.create(
        nombre_comuna=request.POST['nombre_comuna'],
        region=request.POST['region'],
    )
    return ('httpresponse')

def actualizar_inmueble(id_inmueble, new_description):
    Inmueble.objects.filter(pk=id_inmueble).update(descripcion=new_description)
    return 'actualizacion'

def delete_inmueble(id_inmueble):
    Inmueble.objects.get(id = id_inmueble).delete()
    return 'eliminado'