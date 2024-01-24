#Manejo de procesos de memoria
# Autor: José Pablo Hernández Alonso

from time import sleep

ListaTareas = []
DiccionarioMemoriaProcesos = {}

def AgregarMemoria(tarea):              
    for i in range(len(tarea)):                             #Agrega a un diccionario para separar tareas de complejidad y crear subprocesos
        DiccionarioMemoriaProcesos[i+1]=int(tarea[i])
    #print(DiccionarioMemoriaProcesos)
    RISC(DiccionarioMemoriaProcesos)                        #Manda a llamar a la función RISC para ejecutar los subprocesos


def RISC(DiccionarioMemoriaProcesos):                       #Función para ejecutar los subprocesos
    print(f'\nSe tienen {len(DiccionarioMemoriaProcesos)} subprocesos en RISC')
    for i in range(len(DiccionarioMemoriaProcesos)):
        print(f'\nEjecutando tarea_{i+1}')
        if DiccionarioMemoriaProcesos[i+1] > 8:
            print(f'La tarea_{i+1} es muy compleja para RISC, se ejecutará en CISC')
            CISC(DiccionarioMemoriaProcesos,i+1)
        else:
            for j in range(DiccionarioMemoriaProcesos[i+1]):
                print(f'Ejecutando subproceso {j+1} de {DiccionarioMemoriaProcesos[i+1]} de tarea_{i+1} en RISC')
                sleep(0.5)
            del DiccionarioMemoriaProcesos[i+1]
    print('Se han ejecutado todos los subprocesos')

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

#----------Otro-----------------#
# AgregarMemoria(tarea1)
# AgregarMemoria(tarea2)
#print(ListaMemoriaProcesos)
#RISC(ListaMemoriaProcesos)
#print(ListaRISC)


    # for i in range(len(lista)):
    #     ListaRISC.append(lista[i])
    # print(f'Se tienen {len(ListaRISC)} subprocesos en RISC')
    # print('Ejecutando subprocesos de RISC')
    # for i in range(len(lista)):
    #     print(f'Ejecutando subproceso {i+1} de {len(lista)} en RISC')
    #     ListaRISC.pop()
    #     sleep(1)
    # print('Se han ejecutado todos los subprocesos de RISC')
