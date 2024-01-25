#Manejo de procesos de memoria
# Autor: José Pablo Hernández Alonso

from time import sleep

ListaTareas = []
DiccionarioMemoriaProcesos = {}

def AgregarMemoria(tarea):              
    for i in range(len(tarea)):                                 #Agrega a un diccionario para separar tareas de complejidad y crear subprocesos
        DiccionarioMemoriaProcesos[i+1]=int(tarea[i])
    #print(DiccionarioMemoriaProcesos)
    PROCESAR(DiccionarioMemoriaProcesos)                        #Manda a llamar a la función RISC para ejecutar los subprocesos

def PROCESAR(DiccionarioMemoriaProcesos):                       #Función para ejecutar los subprocesos
    print(f'\nSe tienen {len(DiccionarioMemoriaProcesos)} tarea(s) por ejecutar')
    for i in range(len(DiccionarioMemoriaProcesos)):
        print(f'\nEjecutando tarea_{i+1}')
        
        if DiccionarioMemoriaProcesos[i+1] > 20:
            print(f'La tarea_{i+1} es muy compleja no se puede ejecutar, se eliminará de la memoria')
            sleep(1)
            del DiccionarioMemoriaProcesos[i+1]
        elif DiccionarioMemoriaProcesos[i+1] > 8:
            print(f'La tarea_{i+1} es muy compleja para RISC, se ejecutará en CISC')
            CISC(DiccionarioMemoriaProcesos,i+1)
        else:
            RISC(DiccionarioMemoriaProcesos,i+1)
            # for j in range(DiccionarioMemoriaProcesos[i+1]):
            #     print(f'Ejecutando subproceso {j+1} de {DiccionarioMemoriaProcesos[i+1]} de tarea_{i+1} en RISC')
            #     sleep(0.5)
            # del DiccionarioMemoriaProcesos[i+1]
    print('Se han ejecutado todos los subprocesos')

def RISC(DiccionarioMemoriaProcesos,tarea):
    print(f'\nEjecutando tarea_{tarea} de complejidad {DiccionarioMemoriaProcesos[tarea]} en RISC')
    for j in range(DiccionarioMemoriaProcesos[tarea]):
        print(f'Ejecutando subproceso {j+1} de {DiccionarioMemoriaProcesos[tarea]} de tarea_{tarea} en RISC')
        sleep(0.5)
    del DiccionarioMemoriaProcesos[tarea]

def CISC(DiccionarioMemoriaProcesos,tarea):
    print(f'\nEjecutando tarea_{tarea} de complejidad {DiccionarioMemoriaProcesos[tarea]} en CISC')
    sleep(4)
    del DiccionarioMemoriaProcesos[tarea]
    print(f'Se ejecuto la tarea_{tarea} en CISC')

#----------Inicio del programa-----------------#
Tareas_por_realizar=input('Introduzca el número de tareas por realizar: ')
for i in range(int(Tareas_por_realizar)):
    tarea=int(input(f'Introduzca la complejidad de la tarea_{i+1}: '))
    ListaTareas.append(tarea)
#print(ListaTareas)
AgregarMemoria(ListaTareas)
#print(DiccionarioMemoriaProcesos)