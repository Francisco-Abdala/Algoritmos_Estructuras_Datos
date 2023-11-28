import heapq

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        
    def agregar_nodo(self, valor):
        self.nodos.add(valor)
        self.aristas[valor] = {}
        
    def agregar_arista(self, desde, hacia, peso):
        self.aristas[desde][hacia] = peso
        self.aristas[hacia][desde] = peso

def dijkstra_unica_ruta(grafo, nodo_inicial, nodo_destino):
    distancia = {nodo: float('inf') for nodo in grafo.nodos}
    distancia[nodo_inicial] = 0

    heap = [(0, nodo_inicial)]
    padres = {nodo_inicial: None}

    while heap:
        (dist, nodo_actual) = heapq.heappop(heap)

        if nodo_actual == nodo_destino:
            # Construir la ruta si hemos llegado al nodo destino
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]
            return ruta

        for vecino, peso in grafo.aristas[nodo_actual].items():
            nueva_distancia = distancia[nodo_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    # Si no se encontró una ruta al nodo destino
    return None