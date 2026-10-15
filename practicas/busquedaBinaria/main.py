from pathlib import Path

from algoritmos.abusquedaBinaria import busquedaBinaria
from utilidades.lector_csv import cargar_productos


def main():

    # 1. Definir la ruta del archivo CSV
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"

    # 2. Cargar los productos
    productos = cargar_productos(ruta)

    # 3. Ordenar los productos por código
    productos.sort(key=lambda producto: producto[0])

    # 4. Solicitar el código del producto
    codigo = input("Ingrese el código del producto: ").strip().upper()

    # 5. Ejecutar la búsqueda binaria
    resultado = busquedaBinaria(productos, codigo)

    # 6. Mostrar el resultado
    if resultado is not None:

        posicion, producto = resultado

        print("\nProducto encontrado")
        print("Posición:", posicion)
        print("Código:", producto[0])
        print("Nombre:", producto[1])
        print("Categoría:", producto[2])
        print("Precio: $", producto[3])
        print("Existencia:", producto[4])

    else:
        print("\nProducto no encontrado")


if __name__ == "__main__":
    main()