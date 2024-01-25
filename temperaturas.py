import random
from time import sleep
from datetime import datetime

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

def reporte(temperaturas):
    print(f'\nLa temperatura promedio es: {promedio(temperaturas)}')
    print(f'La temperatura máxima es: {maximo(temperaturas)}')
    print(f'La temperatura mínima es: {minimo(temperaturas)}')

#----------Inicio del programa-----------------#
cantidad_lecturas=int(input('Introduzca la cantidad de lecturas a realizar: '))
temperaturas=lecturas(cantidad_lecturas)
print(f'\nLas lecturas realizadas son: {temperaturas}')
reporte(temperaturas)