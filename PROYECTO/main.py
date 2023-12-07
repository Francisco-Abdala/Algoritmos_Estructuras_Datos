from secuencia import *
import csv
import math
import numpy as np

crear_csv()

class Muestra():
    def __init__(self,seq,p,q):
        self.secuencia = seq
        self.cantidad = 0
        self.valor_q =  q
        self.valor_p = p
lista = []
with open("secuencias.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        valor_p = random.uniform(0,1)
        valor_q = -10* math.log(valor_p,10)
        muestra = Muestra(row,valor_p,valor_q)
        lista.append(muestra)

for i in range(len(lista)):
    print(lista[i].valor_q) 


#ORDENAR
#BUSCAR
#LLAMAR FUNCIÓN DE RESTAR CALIDAD

