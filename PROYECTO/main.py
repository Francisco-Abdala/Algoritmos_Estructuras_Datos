from secuencia import *
import csv
import math
import numpy as np

crear_csv()

class Muestra():
    def __innit__(self,seq):
        self.secuencia = seq
        self.cantidad = 0
        self.valor_q =  0
        self.valor_p = 0
with open("secuencias.csv") as f:
    reader = csv.reader(f)


#ORDENAR
#BUSCAR
#LLAMAR FUNCIÓN DE RESTAR CALIDAD

