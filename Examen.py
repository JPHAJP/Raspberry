import random
from time import sleep
from datetime import datetime, timedelta
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

def lecturas(cantidad):
    temperaturas=[]
    humendades=[]
    presiones=[]
    for i in range(cantidad):
        temperaturas.append(sensor_temp())
        humendades.append(sensor_humedad())
        presiones.append(sensor_presion())  
    return temperaturas, humendades, presiones

def estadisticos(datos):
    return round(sum(datos)/len(datos),2), max(datos), min(datos)

def guardar(cantidad,datos,nombre):
    fecha=datetime.now()
    archivo=mg(nombre)
    archivo.escritura_remplazo('Tiempo\t\t\t\t\t\tTemperatura\tHumedad\tPresion\n')
    for i in range(cantidad):
        fecha=fecha+timedelta(minutes=1)
        archivo.escritura(f'{fecha},\t{datos[0][i]},\t\t{datos[1][i]},\t{datos[2][i]}')

def reporte(datos, tipo):
    estad=estadisticos(datos)
    print(f'\nLa {tipo} promedio es: {estad[0]}')
    print(f'La {tipo} máxima es: {estad[1]}')
    print(f'La {tipo} mínima es: {estad[2]}')

#----------Inicio del programa-----------------#
#generar lecturas
#cantidad_lecturas=int(input('Introduzca la cantidad de lecturas a realizar: '))
cantidad_lecturas=10
datos=lecturas(cantidad_lecturas)

#guradar lecturas en archivo
print('\nGuardando lecturas en archivo...')
guardar(cantidad_lecturas,datos,'temperaturas.txt')
print('Lecturas guardadas en archivo')

#verificar archivo
print(f'\nLas lecturas realizadas son: {datos}')

#reporte de temperaturas, humedades y presiones
reporte(datos[0],'temperatura')
reporte(datos[1],'humedad')
reporte(datos[2],'presion')

#graficar temperaturas, presiones y humedades
graficar(cantidad_lecturas,datos)

eleccion=input('Desea ver el archivo de lecturas? (s/n): ')
if eleccion=='s':
    archivo=mg('temperaturas.txt')
    print(archivo.lectura())
else:
    print('Fin del programa')
    exit()