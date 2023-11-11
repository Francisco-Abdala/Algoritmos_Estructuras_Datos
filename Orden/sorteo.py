from lista import *

def quicksort(lista, first, last):
    izq = first
    der = last - 1
    piv = last
    while izq < der:
        while lista.index(izq) < lista.index(piv) and izq <= der:
            izq += 1
        while lista.index(der) > lista.index(piv) and der >= izq:
            der -= 1
        if izq < der:
            aux = lista.index(izq)
            lista.reemplazar(izq, lista.index(der))
            lista.reemplazar(der, aux)
    if lista.index(piv) < lista.index(izq):
        aux = lista.index(izq)
        lista.reemplazar(izq, lista.index(piv))
        lista.reemplazar(piv, aux)
    if first < izq:
        quicksort(lista, last, izq - 1)
    if last > izq:
        quicksort(lista, izq + 1, last)

def mezcla(left, right):
    mezclada = Lista()
    while left.tamanio > 0 and (right.tamanio > 0):
        if left.index(0) < right.index(0):
            mezclada.insertar(left.obtener(0))
        else:
            mezclada.insertar(right.obtener(0))
    if left.tamanio > 0:
        for i in range(left.tamanio):
            mezclada.insertar(left.index(i))
    if right.tamanio > 0:
        for j in range(right.tamanio):
            mezclada.insertar(right.index(j))
    return mezclada


def merge(lista):
    if lista.tamanio <= 1:
        return lista
    else:
        mid = lista.tamanio // 2
        izq = Lista()
        for i in range(0, mid):
            izq.insertar(lista.index(i))
        der = Lista()
        for i in range(mid, lista.tamanio):
            der.insertar(lista.index(i))
        izq = merge(izq)
        der = merge(der)
        if izq.index(mid - 1) <= der.index(0):
            for i in range(der.tamanio):
                izq.insertar(der.index(i))
            return izq
        resultado = mezcla(izq, der)
        return resultado
    
