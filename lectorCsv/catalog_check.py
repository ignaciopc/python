import csv
from pathlib import Path

ruta = Path("productos.csv")

if ruta.exists() :
    with open("productos.csv","r",newline="") as f:
        archivo = csv.DictReader(f)

        for fila in archivo :
            print(fila)