"""
Funciones de utilidades
"""


cleaned_data = lambda x:{k:v for k,v in x.items() if k != 'csrfmiddlewaretoken'}



def funcion(x):
    temp_dict = {}
    for k,v in x.items():
        if k !='csrfmiddlewaretoken':
            temp_dict[k] = v

    return temp_dict


