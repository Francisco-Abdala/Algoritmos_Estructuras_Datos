from lista import *
from sorteo import *
import random
from arbol import *
import time
lista = Lista()

for j in range(2000): #Crea los n-datos
    lista.insertar(random.randint(0,5000))


arbol = nodoArbol(lista.index(0))

def generar_arbol(lista, arbol):

    for j in range(1,lista.tamanio):
        arbol.insertarNodo(lista.index(j))

#Métodos de sorteo

#lista.burbuja(lista)
#lista.burbujaMej(lista)
#lista.burbujabidir(lista)
#lista.seleccion(lista)
#lista.insercion(lista)
#quicksort(lista,0, lista.tamanio - 1 )
#merge(lista)

inicio = time.time()
generar_arbol(lista,arbol)

fin = time.time()
print(fin-inicio)