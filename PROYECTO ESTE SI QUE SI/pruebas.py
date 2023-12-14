from secuencia import *
import csv
import timeit

crear_csv()

class Muestra():
    def __init__(self, nombre, seq, calidad):
        self.nombre = nombre
        self.secuencia = seq
        self.calidad = calidad
lista = []
with open("secuencias.csv") as f:
    numero = 0
    reader = csv.reader(f)
    for row in reader:
        numero += 1
        calidad = random.uniform(80.00, 100.00)
        nombre = f"Secuencia {numero}"
        muestra = Muestra(nombre,row,calidad)
        lista.append(muestra)

def secuencial(lista, info):
    pos = 0
    encontrado = False
    while pos < len(lista) and not encontrado:
        if round(lista[pos].calidad) == info:
            encontrado = True
        else:
            pos += 1
    return encontrado

def binariaIterativa(lista, info):
    izq = 0 
    der = len(lista) - 1
    encontrado = False
    while izq <= der and not encontrado:
        mitad = (izq+der)//2
        if round(lista[mitad].calidad) == info:
            encontrado = True
            return encontrado
        elif round(lista[mitad].calidad) > info:
            der = mitad-1
        else:
            izq = mitad+1
    return encontrado

def binariaRecursiva(lista, info, menor, mayor):
    encontrado = False
    if mayor >= menor and not encontrado:
        mitad = (mayor + menor) // 2
        if round(lista[mitad].calidad) == info:
            encontrado = True
            return encontrado
        elif round(lista[mitad].calidad) > info:
            return binariaRecursiva(lista, info, menor, mitad-1)
        else:
            return binariaRecursiva(lista, info, mitad+1, mayor)
    else:
        return encontrado
valor = lista[random.randint(0,(len(lista)-1))].calidad
tiempo = timeit.timeit("binariaRecursiva(lista,valor,0,len(lista)-1)", globals=globals(),number=1)
print(tiempo)
"""

def burbuja(lista):
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            if lista[j].calidad > lista[j + 1].calidad:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

            #print("Burbuja i[", i, "]-j[", j, "]: vector : ", lista)


def burbujaMejorada(lista):
    i = 0
    control = True
    while (i <= len(lista) - 2) and control:
        control = False
        for j in range(0, len(lista) - i - 1):
            if lista[j].calidad > lista[j + 1].calidad:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                control = True
            #print("Burbuja Mejorada i[", i, "]-j[", j, "]: vector : ", lista)
        i = i + 1


def burbujaBidireccional(lista):
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if lista[i].calidad > lista[i + 1].calidad:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                control = True
            ""print(
                "Burbuja Bidireccional f1 izq[",
                i,
                "]-der[",
                derecha,
                "]: vector : ",
                lista,
            )""
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if lista[j].calidad < lista[j - 1].calidad:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[i - 1] = aux
                control = True
            ""print(
                "Burbuja Bidireccional f2 izq[",
                izquierda,
                "]-der[",
                j,
                "]: vector : ",
                lista,
            )""
        izquierda += 1


def seleccion(lista):
    for i in range(0, len(lista) - 1):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j].calidad < lista[minimo].calidad:
                minimo = j
            ""print(
                "Seleccion i[",
                i,
                "]-j[",
                j,
                "] - minimo(",
                minimo,
                "): vector : ",
                lista,
            )""
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux


def insercion(lista):
    for i in range(1, len(lista) + 1):
        k = i - 1
        while (k > 0) and lista[k].calidad < lista[k - 1].calidad:
            aux = lista[k]
            lista[k] = lista[k - 1]
            lista[k - 1] = aux
            #print("Insercion i[", i, "]-k[", k, "]: vector : ", lista)
            k -= 1





def ordenamientoMezcla(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = ordenamientoMezcla(izquierda)
        derecha = ordenamientoMezcla(derecha)
        if izquierda[medio - 1].calidad <= derecha[0].calidad:
            izquierda += derecha
            return izquierda
        resultado = mezcla(izquierda, derecha)
        return resultado


def mezcla(izquierda, derecha):
    #print("mergeSort - izq", izquierda, "der", derecha)
    lista_mezclada = []
    while len(izquierda)>0 and (len(derecha) > 0):
        if izquierda[0].calidad < derecha[0].calidad:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

"""

# inicio = time.time()
# burbuja(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# burbujaMejorada(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# burbujaBidireccional(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# seleccion(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# insercion(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# ordenamientoRapido(lista,0,len(lista)-1)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)

# inicio = time.time()
# lista = ordenamientoMezcla(lista)
# fin = time.time()
# tiempo = fin-inicio
# print(tiempo)
