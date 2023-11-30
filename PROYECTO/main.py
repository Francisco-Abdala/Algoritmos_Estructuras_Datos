from secuencias import *
import csv

class Seq():
    def __init__(self,dato):
        self.secuencia = dato
        self.calidad = 100.00

    def restar_calidad(self):
        self.calidad = 100.00 - 0.01

crear_csv()
objetos = []

with open("secuencias.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        seq = Seq(row)
        objetos.append(seq)

print(len(objetos))


