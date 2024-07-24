import csv
from m7_python.models import Comuna

def import_comuna():
    with open('regiones-chile.csv', 'r', encoding='utf8') as file:
        data = csv.reader(file, 
                            delimiter=';'
                            )
        data = list(data)

    data.pop(0)

    for d in data:
        Comuna.objects.create(
            nombre_comuna = d[3],
            region = d[0]
        )