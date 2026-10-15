from pathlib import Path
from algoritmos.abusquedaLineal import busqueda_lineal
from utilidades.lector_csv import cargar_productos

def main():
    ruta = Path(__file__).resolve().parent/"datos"/"productos.csv"
    productos=cargar_productos(ruta)

    print("Ingrese el codigo del producto a buscar:")
    codigo = input()

    resultado = busqueda_lineal(productos,codigo)
    #print(resultado)
    #print(type(resultado))

    if resultado is not None:
        posicion, producto = resultado
        #print(f"Dato {valor} encontrado en la posicion {posicion}")
        print("Código del producto: ", producto[0])
        print("Nombre del producto: ", producto[1])
        print("Categoría del producto: ", producto[2])
        print("Precio del producto: ", producto[3])
        print("Existencias del producto: ", producto[4])
    else:
        print("Dato no encontrado!")

if __name__ == "__main__":
    main()