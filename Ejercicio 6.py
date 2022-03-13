#Ejercicio 6: Especificación de está_explorado
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
