#Ejercicio 6: Especificación de está_explorado
import random
lista = []
def creacion_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista

