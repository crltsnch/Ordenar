#Ejercicio 4: Ordenación por inserción dicotómica
import random

def OrdenacionInsercion(lista):
    n = len(lista)
    for i in range(1, n):
        valorInsertar = lista[i]
        j = i-1
        while(j>= 0 and lista[j] > valorInsertar):
            