import csv
from django.core.management.base import BaseCommand
from m7_python.models import Inmueble, Usuario, Comuna

class Command(BaseCommand):
    help = 'Carga inmuebles desde un archivo CSV'

    def handle(self, *args, **kwargs):
        with open('inmuebles.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                propietario = Usuario.objects.get(rut=row['propietario_id'])
                arrendatario = Usuario.objects.get(rut=row['arrendatario_id']) if row['arrendatario_id'] else None
                comuna = Comuna.objects.get(id=row['comuna_id'])
                
                Inmueble.objects.update_or_create(
                    nombre=row['nombre'],
                    defaults={
                        'propietario': propietario,
                        'descripcion': row['descripcion'],
                        'm2_construidos': row['m2_construidos'],
                        'm2_totales': row['m2_totales'],
                        'cantidad_estacionamientos': row['cantidad_estacionamientos'],
                        'cantidad_habitaciones': row['cantidad_habitaciones'],
                        'cantidad_banos': row['cantidad_banos'],
                        'direccion': row['direccion'],
                        'comuna': comuna,
                        'tipo_inmueble': row['tipo_inmueble'],
                        'precio_arriendo': row['precio_arriendo'],
                        'disponible': row['disponible'].lower() == 'true',
                        'solicitudes': row['solicitudes'],
                        'arrendatario': arrendatario,
                    }
                )
        self.stdout.write(self.style.SUCCESS('Inmuebles cargados con éxito'))

### se ejecuta con: python manage.py cargar_inmuebles
