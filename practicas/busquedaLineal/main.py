from pathlib import Path #para resolver la ruta del archivo csv
from algoritmos.abusquedaLineal import busquedaLineal
from utilidades.lector_csv import cargar_productos

def main():
    ruta = Path(__file__).resolve().parent/"datos"/"productos.csv"
    productos = cargar_productos(ruta)

    print("INGRESA EL CÓDIGO DEL PRODUCTO:")
    codigo = input()
    resultado = busquedaLineal(productos,codigo)

    if resultado is not None:
        posicion, producto = resultado
        print("Encontrado:", producto)
        print("Posición:", posicion)
        print("Nombre", producto[1])
        print("Categoria", producto[2])
        print("Precio", producto[3])
        print("Existencia", producto[4])
    else:
        print("Producto no encontrado!")


if __name__ == "__main__":
    main()