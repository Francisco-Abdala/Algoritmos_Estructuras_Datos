import random
import csv 
import os

nombre = "secuencias.csv"

def crear_csv():
    bases = ["A","T","C","G","N","R","Y"]
    lista_seq = []
    n = 0
    while n < 500:
        seq = ""
        for i in range(10000):
            aux = random.randint(0,6)
            aux2 = bases[aux]
            seq += aux2
        lista_seq.append(seq)
        n += 1
    
    with open("secuencias.csv","w", newline="") as file:
        writer = csv.writer(file,delimiter="\n")
        writer.writerow(lista_seq)

if os.path.isfile(nombre):
    print("todo bien")
else:
    crear_csv()

