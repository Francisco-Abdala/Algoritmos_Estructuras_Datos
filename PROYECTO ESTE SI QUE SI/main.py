from secuencia import *
import csv
crear_csv()

class Muestra():
    def __init__(self, nombre, seq, calidad):
        self.nombre = nombre
        self.secuencia = seq
        self.calidad = calidad

lista = []

with open("secuencias.csv") as f:                   #O(1)          
    numero = 0                                      #O(1)
    reader = csv.reader(f)                          #O(1)
    for row in reader:                              #O(n)
        numero += 1                                 #O(1)
        calidad = random.uniform(80.00, 100.00)     #O(1)
        nombre = f"Secuencia {numero}"              #O(1)
        muestra = Muestra(nombre,row,calidad)       #O(1)
        lista.append(muestra)                       #O(1)
#Total: O(n)


def check_num():
    while True:                                                        #O(1)
        valor = input("Ingrese el valor de calidad de su secuencia: ") #O(1)
        try:                                                           #O(1)
            float_numero = float(valor)                                #O(1)
            if float_numero.is_integer():                              #O(1)
                return int(valor)                                      #O(1)
            else:                                                      #O(1)
                return float_numero                                    #O(1)
        except ValueError:                                             #O(1)
            return f"{valor} no es un número."                         #O(1)
    #Total: O(1)

def listar_seqNombre(lista):
    for i in range(len(lista)):     #O(n)
        print(lista[i].nombre)      #O(1)
    #Total: O(n)


def listar_seqCalidad(lista):
    for i in range(len(lista)):     #O(n)
        print(lista[i].calidad)     #O(1)
    #Total: O(n)


def listar_seq(lista):
    for i in range(len(lista)):     #O(n)
        print(lista[i].secuencia)   #O(1)
    #Total: O(n)

def insertar_seq(lista):
    nombre = input("Inserte el nombre de su secuencia: ")       #O(1)
    aux_row = input("Inserte la secuencia: ").upper()           #O(1)
    row = []                                                    #O(1)
    row.append(aux_row)                                         #O(1)
    calidad = check_num()                                       #O(1)
    Seq = Muestra(nombre,row,calidad)                           #O(1)
    lista.append(Seq)                                           #O(1)
    #Total: O(1)


def buscar_nombre(lista):
    nombre = input("Inserte el nombre de la secuencia a buscar: ").upper()      #O(1)
    validacion = False                                                          #O(1)
    for i in range(len(lista)):                                                 #O(n)
        if lista[i].nombre.upper() == nombre:                                   #O(1)
            validacion = True                                                   #O(1)
            print(f"""La información de esta secuencia es la siguiente:         
                    Secuencia: {lista[i].secuencia}
                    Calidad de la secuencia: {lista[i].calidad}% """)           #O(1)
        elif i == len(lista) and validacion == False:                           #O(1)
            print("No se encontraron coincidencias.")                           #O(1)
    #Total: O(n)
       

def buscar_calidad(lista):
    valor = check_num()                                                     #O(1)
    contador = 0                                                            #O(1)
    validacion = False                                                      #O(1)
    for i in range(len(lista)):                                             #O(n)
        if valor <= lista[i].calidad:                                       #O(1)
            validacion = True                                               #O(1)
            contador += 1                                                   #O(1)
            if contador == 1:                                               #O(1)
                print("Se han encontrado las siguientes secuencias:\n")     #O(1)
            print(f"""
                  Nombre: {lista[i].nombre}
                  Secuencia: {lista[i].secuencia}
                  Calidad: {lista[i].calidad}\n\n""")                       #O(1)
        elif i == len(lista) and validacion == False:                       #O(1)
            print("No se encontraron coincidencias.")                       #O(1)
    #Total: O(n)
            

def ordenamientoRapido(lista, primero, ultimo):
    izquierda = primero                                                                     #O(1)
    derecha = ultimo - 1                                                                    #O(1)
    pivote = ultimo                                                                         #O(1)
    while izquierda < derecha:                                                              #O(n)
        while lista[izquierda].calidad < lista[pivote].calidad and izquierda <= derecha:    #O(n)
            izquierda += 1                                                                  #O(1)
        while lista[derecha].calidad > lista[pivote].calidad and derecha >= izquierda:      #O(n)
            derecha -= 1                                                                    #O(1)
        if izquierda < derecha:                                                             #O(1)
            aux = lista[izquierda]                                                          #O(1)
            lista[izquierda] = lista[derecha]                                               #O(1)
            lista[derecha] = aux                                                            #O(1)
    if lista[pivote].calidad < lista[izquierda].calidad:                                    #O(1)
        aux = lista[izquierda]                                                              #O(1)
        lista[izquierda] = lista[pivote]                                                    #O(1)
        lista[pivote] = aux                                                                 #O(1)
    if primero < izquierda:                                                                 #O(log n)
        ordenamientoRapido(lista, primero, izquierda - 1)                                   #Recursividad
    if ultimo > izquierda:                                                                  #O(log n)
        ordenamientoRapido(lista, izquierda + 1, ultimo)                                    #Recursividad
    #Total: O(n log n)
    


def eliminar_muestra(lista):
    nombre = input("Inserte el nombre de la secuencia a eliminar: ").upper()        #O(1)
    validacion = False                                                              #O(1)
    i = 0                                                                           #O(1)
    while i < len(lista):                                                           #O(n)
        if lista[i].nombre.upper() == nombre:                                       #O(1)
            validacion = True                                                       #O(1)
            lista.pop(i)                                                            #O(n)
        else:                                                                       #O(1)
            i += 1                                                                  #O(1)
    if not validacion:                                                              #O(1)
        print("No se encontraron coincidencias.")                                   #O(1)
    #Total: O(n^2)

def modificar_valor(lista):
    nombre = input("Inserte el nombre de la secuencia a modificar: ").upper()       #O(1)
    validacion = False                                                              #O(1)
    for i in range(len(lista)):                                                     #O(n)
        if nombre == lista[i].nombre.upper():                                       #O(1)
            validacion = True                                                       #O(1)
            nombre_nuevo = input("Inserte el nombre nuevo: ")                       #O(1)
            seq_nueva = input("Inserte la secuencia nueva: ").upper()               #O(1)
            row = []                                                                #O(1)
            row.append(seq_nueva)                                                   #O(1)
            valor = check_num()                                                     #O(1)
            lista[i].nombre = nombre_nuevo                                          #O(1)
            lista[i].secuencia = row                                                #O(1)
            lista[i].calidad = valor                                                #O(1)
        elif i == len(lista) and validacion == False:                               #O(1)
            print("No se encontraron coincidencias.")                               #O(1)
    #Total: O(n)


def buscar_calidad_noOrdenada(lista):
    validacion = False                                                          #O(1)
    calidad = check_num()                                                       #O(1)
    for i in range(len(lista)):                                                 #O(n)
        if lista[i].calidad == calidad:                                         #O(1)
            validacion = True                                                   #O(1)
            print(f"""La información de esta secuencia es la siguiente:
                    Nombre: {lista[i].nombre}
                    Secuencia: {lista[i].secuencia}
                    Calidad de la secuencia: {lista[i].calidad}% """)           #O(1)
        elif i == len(lista) and validacion == False:                           #O(1)
            print("No se encontraron coincidencias.")                           #O(1)
    #Total: O(n)


def buscar_calidad_ordenada(lista):
    info = check_num()                                                          #O(1)
    izq = 0                                                                     #O(1)
    der = len(lista) - 1                                                        #O(1)
    encontrado = False                                                          #O(1)
    while izq <= der and not encontrado:                                        #O(log n)
        mitad = (izq+der)//2                                                    #O(1)
        if lista[mitad].calidad == info:                                        #O(1)
            encontrado = True                                                   #O(1)
            print(f"""La información de esta secuencia es la siguiente:
                    Nombre: {lista[mitad].nombre}
                    Secuencia: {lista[mitad].secuencia}
                    Calidad de la secuencia: {lista[mitad].calidad}% """)        #O(1)
        elif lista[mitad].calidad > info:                                        #O(1)
            der = mitad-1                                                        #O(1)
        else:                                                                    #O(1)
            izq = mitad+1                                                        #O(1)
    print(encontrado)                                                            #O(1)
    #Total: O(log n)
                                                       

def secuencias_utiles(lista):
    valor = 95.00                                                           #O(1)
    contador = 0                                                            #O(1)
    validacion = False                                                      #O(1)
    for i in range(len(lista)):                                             #O(n)
        if valor <= lista[i].calidad:                                       #O(1)
            validacion = True                                               #O(1)
            contador += 1                                                   #O(1)
            if contador == 1:                                               #O(1)
                print("Se han encontrado las siguientes secuencias:\n")     #O(1)
            print(f"""
                  Nombre: {lista[i].nombre}
                  Secuencia: {lista[i].secuencia}
                  Calidad: {lista[i].calidad}\n\n""")                       #O(1)
                  
        elif i == len(lista) and validacion == False:                       #O(1)
            print("No se encontraron coincidencias.")                       #O(1)
    #Total: O(n)

while True:
    print("""Acciones:
          1.- Listar por secuencia.
          2.- Listar por calidad (%).
          3.- Listar por nombre.
          4.- Insertar secuencia.
          5.- Buscar secuencia por nombre. (Secuencial dado que no es el elemento por el cual se ordena)
          6.- Información dado el valor de calidad. (Entrega las secuencias con un valor de calidad mayor o igual a ese valor)
          7.- Ordenar por valor de calidad. 
          8.- Eliminar una secuencia.
          9.- Modificar información.
          10.- Buscar por valor de calidad en la lista no ordenada.
          11.- Buscar por valor de calidad en la lista ordenada. (Búsqueda binaria iterativa)
          12.- Mostrar secuencias útiles (calidad >= 95%).
          Para salir, ingrese una tecla cualquiera.""")
    accion = input("Ingrese el número de la acción que quiera realizar: ")
    match accion:
        case "1": listar_seq(lista)
        case "2": listar_seqCalidad(lista)
        case "3": listar_seqNombre(lista)
        case "4": insertar_seq(lista)
        case "5": buscar_nombre(lista)
        case "6": buscar_calidad(lista)
        case "7": ordenamientoRapido(lista,0,len(lista) - 1)
        case "8": eliminar_muestra(lista)
        case "9": modificar_valor(lista)
        case "10": buscar_calidad_noOrdenada(lista)
        case "11": buscar_calidad_ordenada(lista)
        case "12": secuencias_utiles(lista)
        case _ : break
