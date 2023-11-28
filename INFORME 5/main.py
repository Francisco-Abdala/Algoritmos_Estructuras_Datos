import random
from v2 import *
from MetodosBusqueda import *
from Dijkstra import *
import timeit

heap = Heap(10)
heap.tamanio = 10

def crear_lista():
    lista = []
    while heap.tamanio != len(lista):
        x = random.randint(0,1000000000000000)
        if x not in lista:
            lista.append(x)
        else:
            x = 0
            continue
      
    return lista
    
heap.vector = crear_lista()


#PARTE A
"""
inicio = time.time()

fin = time.time()
print(fin - inicio)
"""

#PARTE B
monticulizar(heap)
HeapSort(heap)
valor = heap.vector[0]
print("ESTÁ ORDENADO")
print("-"*10)
"""
inicio1 = time.time()
secuencial(heap,valor)
fin1 = time.time()

print(fin1 - inicio1)

inicio2 = time.time()
binariaIterativa(heap,valor)
fin2 = time.time()
print(fin2- inicio2)

"""

tiempo = timeit.timeit("binariaRecursiva(heap,valor,0,heap.tamanio-1)", globals=globals(),number=1)

#Parte C


grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_nodo('2 sur')
grafo_ejemplo.agregar_nodo('30 oriente')
grafo_ejemplo.agregar_nodo('11 oriente')
grafo_ejemplo.agregar_nodo('6 oriente')
grafo_ejemplo.agregar_nodo('16 sur')
grafo_ejemplo.agregar_nodo('2 norte')
grafo_ejemplo.agregar_nodo('26 sur')
grafo_ejemplo.agregar_nodo('26 1/2 sur')
grafo_ejemplo.agregar_nodo('6 poniente')
grafo_ejemplo.agregar_nodo('22 poniente')


grafo_ejemplo.agregar_arista('2 sur', '30 oriente', 15)
grafo_ejemplo.agregar_arista('2 sur', '16 sur', 20)
grafo_ejemplo.agregar_arista('30 oriente', '6 oriente', 6)
grafo_ejemplo.agregar_arista('30 oriente', '11 oriente', 8)
grafo_ejemplo.agregar_arista('6 oriente', '22 poniente', 10)
grafo_ejemplo.agregar_arista('11 oriente', '6 poniente', 7)
grafo_ejemplo.agregar_arista('16 sur', '2 norte', 5)
grafo_ejemplo.agregar_arista('16 sur', '26 sur', 3)
grafo_ejemplo.agregar_arista('16 sur', '6 poniente', 2)
grafo_ejemplo.agregar_arista('2 norte', '26 1/2 sur', 7)
grafo_ejemplo.agregar_arista('26 sur', '26 1/2 sur', 1)
grafo_ejemplo.agregar_arista('6 poniente', '22 poniente', 5)
grafo_ejemplo.agregar_arista('26 1/2 sur', '22 poniente', 4)



nodo_inicial = '2 sur'
nodo_destino = '22 poniente'

ruta_eficiente = dijkstra_unica_ruta(grafo_ejemplo, nodo_inicial, nodo_destino)

if ruta_eficiente:
    print(f"Camino con menos gasto de bencina desde {nodo_inicial} hasta {nodo_destino}:")
    for i in ruta_eficiente:
        print(i)
else:
    print(f"No hay ruta desde {nodo_inicial} hasta {nodo_destino}")