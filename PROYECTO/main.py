from secuencias import *
import csv

class Seq():
    def __init__(self,dato,valor):
        self.secuencia = dato
        self.repeticion = valor
        self.calidad = 0

    def restar_calidad(self,valor):
        self.calidad = 100.00 - valor*0.01

crear_csv()
objetos = []
secu = []
with open("secuencias.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        seq = Seq(row)
        objetos.append(seq)
        secu.append(row)

print(secu)

#ORDENAR
#BUSCAR
#LLAMAR FUNCIÓN DE RESTAR CALIDAD

