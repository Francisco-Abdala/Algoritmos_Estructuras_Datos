import random
import time
# ayuda = matriz1[x][y] * matriz2[x][x] + matriz1[x][y+1] * matriz2[y+1][x]


def multiplicar_matrices(matriz1,matriz2,matriz_final):
    inicio = time.time()

    for x in range(len(matriz1)):

        for y in range(len(matriz2)):

            for z in range(len(matriz1)):

                matriz_final[x][y] += matriz1[x][z] * matriz2 [z] [y]

    final = time.time()

    tiempo = final - inicio
    
    return matriz_final, tiempo




def crear_matrices(tamanio):
    matriz_1= [[random.randint(0,200) for _ in range(tamanio)]for _ in range(tamanio)]
    matriz_2= [[random.randint(0,200) for _ in range(tamanio)]for _ in range(tamanio)]
    matriz_resultante = [[0 for _ in range(tamanio)] for _ in range (tamanio)]
    return matriz_1,matriz_2,matriz_resultante



def main():
    tamanio = input("Ingrese el tamaño de su matriz: ")
    while not tamanio.isnumeric():
        tamanio = input("Ingrese un número,por favor. ")

    tamanio_int = int(tamanio)
    matriz,matriz2,matriz_final = crear_matrices(tamanio_int)
    resultado, tiempo = multiplicar_matrices(matriz,matriz2,matriz_final)
    print(tiempo)

    
main()