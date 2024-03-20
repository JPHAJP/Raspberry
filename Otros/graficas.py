import matplotlib.pyplot as plt
import random

n=10

x = [i for i in range(n)]
#print(x)
y = [random.randint(0,10) for _ in range(n)]
#print(y)

#graficar
plt.plot(x,y)
plt.title('Grafica de temperatura')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura')
plt.grid()
plt.show()
