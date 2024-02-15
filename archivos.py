class manejador:
    def __init__(self, nombre):
        self.nombre = nombre

    def lectura(self):
        with open(self.nombre,'r') as archivo:
            data = archivo.read()
            return data

    def escritura_remplazo(self,x):
        with open(self.nombre,'w') as archivo:
            archivo.write(x)

    def escritura(self,x):
        with open(self.nombre,'a') as archivo:
            archivo.write(x+'\n')