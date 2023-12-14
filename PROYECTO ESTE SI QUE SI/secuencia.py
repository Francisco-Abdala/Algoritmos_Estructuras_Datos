import random
import csv
import os

nombre = "secuencias.csv"

def crear_csv():
    if os.path.isfile(nombre):
            print("TODO BIEN AMANDA")
    else:
        bases = ["A","T","C","G","N"]
        n = 0
        seq_list = []
        while n < 500:
                n += 1 
                seq = ""
                for _ in range(100):
                        aux = random.randint(0,4)
                        aux2 = bases[aux]
                        seq += aux2
                seq_list.append(seq)
                    
        with open("secuencias.csv","w", newline="") as file:
                writer = csv.writer(file,delimiter="\n")
                writer.writerow(seq_list)
       




                    