#Ejercicio 4: Ordenación por inserción dicotómica
from random import randint

def OrdenacionInsercion(lista):
    n = len(lista)
    for i in range(1, n):
        valorInsertar = lista[i]
        j = i-1
        while(j>= 0 and lista[j] > valorInsertar):
            lista[j] = lista[j+1]
            j -= 1

        lista[j+1] = valorInsertar
    return lista

def main():
    lista = []
    n = int(input("¿Cuántos valores quieres que tenga?: "))

    for i in range(n):
        lista.append(randint(0, 100))
