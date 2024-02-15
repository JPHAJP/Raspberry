import random
from time import sleep
from datetime import datetime, timedelta
from archivos import manejador as mg

def sensor_temp():
    return round(random.uniform(8,25),2)

def lecturas(cantidad):
    temperaturas=[]
    for i in range(cantidad):
        temperaturas.append(sensor_temp())
    return temperaturas

def promedio(temperaturas):
    return round(sum(temperaturas)/len(temperaturas),2)

def maximo(temperaturas):
    return max(temperaturas)

def minimo(temperaturas):
    return min(temperaturas)

# def guardar(temperaturas): 
#     fecha=datetime.fromtimestamp(random.randint(1704900000, 1707000000))
#     with open('temperaturas.txt','w') as archivo:
#         #agregar 60 segundos a la fecha
#         for i in range(len(temperaturas)):
#             fecha=fecha+timedelta(minutes=1)
#             archivo.write(f'{fecha}, - {temperaturas[i]}\n')

def guardar(temperaturas,nombre):
    fecha=datetime.now()
    archivo=mg(nombre)
    archivo.escritura_remplazo('')
    for i in range(len(temperaturas)):
        fecha=fecha+timedelta(minutes=1)
        archivo.escritura(f'{fecha}, - {temperaturas[i]}')

def reporte(temperaturas):
    print(f'\nLa temperatura promedio es: {promedio(temperaturas)}')
    print(f'La temperatura máxima es: {maximo(temperaturas)}')
    print(f'La temperatura mínima es: {minimo(temperaturas)}')

#----------Inicio del programa-----------------#
cantidad_lecturas=int(input('Introduzca la cantidad de lecturas a realizar: '))
temperaturas=lecturas(cantidad_lecturas)
print(f'\nLas lecturas realizadas son: {temperaturas}')
reporte(temperaturas)

print('\nGuardando lecturas en archivo...')
guardar(temperaturas,'temperaturas.txt')
print('Lecturas guardadas en archivo')
eleccion=input('Desea ver el archivo de lecturas? (s/n): ')
if eleccion=='s':
    archivo=mg('temperaturas.txt')
    print(archivo.lectura())
else:
    print('Fin del programa')
    sleep(2)
    exit()