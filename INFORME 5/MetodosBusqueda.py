from v2 import *

def ordenamientoRapido(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while lista[izquierda] < lista[pivote] and izquierda <= derecha:
            izquierda += 1
        while lista[derecha] > lista[pivote] and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            aux = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = aux
    if lista[pivote] < lista[izquierda]:
        aux = lista[izquierda]
        lista[izquierda] = lista[pivote]
        lista[pivote] = aux
    if primero < izquierda:
        ordenamientoRapido(lista, primero, izquierda - 1)
    if ultimo > izquierda:
        ordenamientoRapido(lista, izquierda + 1, ultimo)

def secuencial(heap, info):
    pos = 0
    encontrado = False
    while pos < heap.tamanio and not encontrado:
        if heap.vector[pos] == info:
            encontrado = True
        else:
            pos += 1
    return encontrado

def binariaIterativa(heap, info):
    izq = 0 
    der = heap.tamanio -1
    encontrado = False
    while izq <= der and not encontrado:
        mitad = (izq+der)//2
        if heap.vector[mitad] == info:
            encontrado = True
            return encontrado
        elif heap.vector[mitad] > info:
            der = mitad-1
        else:
            izq = mitad+1
    return encontrado

def binariaRecursiva(heap, info, menor, mayor):
    encontrado = False
    if mayor >= menor and not encontrado:
        mitad = (mayor + menor) // 2
        if heap.vector[mitad] == info:
            encontrado = True
            return encontrado
        elif heap.vector[mitad] > info:
            return binariaRecursiva(heap, info, menor, mitad-1)
        else:
            return binariaRecursiva(heap, info, mitad+1, mayor)
    else:
        return encontrado