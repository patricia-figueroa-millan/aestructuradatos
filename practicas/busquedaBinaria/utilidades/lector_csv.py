import csv

def cargar_productos(ruta_archivo):
    productos = []
    with open(ruta_archivo, mode="r", encoding="utf-8", 
              newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector) #omitir encabezados del archivo csv.

        for fila in lector:
            productos.append(fila)
    return productos