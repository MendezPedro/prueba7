import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from m7_python.models import Usuario

class Command(BaseCommand):
    help = 'Carga usuarios desde un archivo CSV'

    def handle(self, *args, **kwargs):
        with open('usuarios.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user, created = User.objects.get_or_create(username=row['correo_electronico'])
                if created:
                    user.set_password('defaultpassword')  # Set a default password
                    user.save()

                Usuario.objects.update_or_create(
                    rut=row['rut'],
                    defaults={
                        'user': user,
                        'nombre': row['nombre'],
                        'apellido': row['apellido'],
                        'direccion': row['direccion'],
                        'telefono_personal': row['telefono_personal'],
                        'correo_electronico': row['correo_electronico'],
                        'tipo_usuario': row['tipo_usuario'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Usuarios cargados con éxito'))


##se ejecuta con " python manage.py cargar_usuarios "