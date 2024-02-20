import random
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt
from archivos import manejador as mg

def sensor_temp():
    return round(random.uniform(8,25),2)
    #aprox en puebla 16°C

def sensor_humedad():
    return round(random.uniform(40,80),2)
    #aprox en puebla 60%

def sensor_presion():
    return round(random.uniform(99,103),2)
    #aprox en puebla 101 kPa

def graficar(cantidad,datos):
    plt.figure(figsize=(18, 10))
    plt.plot([i for i in range(cantidad)],datos[0])
    plt.plot([i for i in range(cantidad)],datos[1])
    plt.plot([i for i in range(cantidad)],datos[2])
    plt.legend(['Temperatura','Humedad','Presion(kPa)'])
    plt.title('Grafica de temperatura')
    plt.xlabel('Tiempo')
    plt.ylabel('Datos')
    plt.grid()
    plt.show()

def lecturas():
    #escribir datos generados
    temperaturas=sensor_temp()
    humendades=sensor_humedad()
    presiones=sensor_presion()
    return temperaturas, humendades, presiones



def guardar(espacio,datos,nombre):
    fecha=datetime.now()
    archivo=mg(nombre)
    archivo.escritura(f'{fecha}, {datos[espacio][0]}, {datos[espacio][1]}, {datos[espacio][2]}')

def estadisticos(datos):
    return round(sum(datos)/len(datos),2), max(datos), min(datos)

def reporte(datos, tipo):
    estad=estadisticos(datos)
    print(f'\nLa {tipo} promedio es: {estad[0]}')
    print(f'La {tipo} máxima es: {estad[1]}')
    print(f'La {tipo} mínima es: {estad[2]}')

#----------Inicio del programa-----------------#
#generar lecturas
cantidad_lecturas=10
nombre='temperaturas.txt'

#limpiar archivo
archivo=mg(nombre)
archivo.escritura_remplazo('Tiempo, Temperatura, Humedad, Presion\n')
temp=[]
hum=[]
pres=[]
datos=[]

for i in range(cantidad_lecturas):
    datos.append(lecturas())
    print(f'\nLectura {i+1} de {cantidad_lecturas}')
    guardar(i,datos,nombre)
    for j in range(i+1):
        #temp.append(datos[j][0])
        temp.append(datos[j][0])
        hum.append(datos[j][1])
        pres.append(datos[j][2])
    reporte(temp,'temperatura')
    reporte(hum,'humedad')
    reporte(pres,'presion')
    sleep(.5)
datos=[temp,hum,pres]

#verificar archivo
print(f'\nLas lecturas realizadas son: {datos}')

#graficar temperaturas, presiones y humedades
graficar(cantidad_lecturas,datos)

eleccion=input('Desea ver el archivo de lecturas? (s/n): ')
if eleccion=='s':
    archivo=mg('temperaturas.txt')
    print(archivo.lectura())
else:
    print('Fin del programa')
    exit()