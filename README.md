# Ordenar
El link de mi repositorio es https://github.com/crltsnch/Ordenar.git

El código del ejercicio 4 es:

```
from random import randint

def OrdenacionInsercion(lista):
    n = len(lista)
    for i in range(1, n):
        valorInsertar = lista[i]
        j = i-1
        while(j>= 0 and lista[j] > valorInsertar):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valorInsertar
    return lista

def main():
    lista = []
    n = int(input("¿Cuántos valores quieres que tenga?: "))

    for i in range(n):
        lista.append(randint(0, 100))
    
    print(lista)
    lista = OrdenacionInsercion(lista)
    print(lista)

if (__name__ == "__main__"):
    main()
``` 
El del ejercicio 5:
``` 
def ordenarTareas():
    .
    tareas = [1,2,3,4,5]
    tareas=["ponerse los calcetines", "ponerse las zapatillas", "atarse los cordones", "coger las llaves", "salir de casa"]
    lista = [(1,3), (3,5)]

    ordenada[]
    from Clases import ord
    ordenada = list(dict.fromkeys(ordenada))
    print(ordenada)

ordenarTareas()
```

Y el del ejercicio 6:
```
import random
lista = []
def creacion_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista

def segmentos(lista, i):
    segmento = []
    segmento.append(lista[i])
    while (len(lista) > 1) and (lista[i] >= lista[i + 1]):
        segmento.append(lista[i + 1])
        lista.pop(i + 1)
    lista.pop(i)
    return segmento

def lista_segmento(lista, grupodeSegmentos):
    while len(lista) > 1:
        segmento = []
        segmento = segmentos(lista, 0)
        print(segmento)
        grupodeSegmentos.append(segmento)
        print(" La lista resultante es " + str(lista))
    return grupodeSegmentos
```
