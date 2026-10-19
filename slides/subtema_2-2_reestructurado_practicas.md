---
theme: default
title: "Subtema 2.2 | Algoritmos de búsqueda"
transition: fade
---

<div class="text-violet-700 font-bold tracking-widest">TEMA 2 · SUBTEMA 2.2</div>

# Algoritmos de búsqueda

<div class="text-2xl mt-10 font-semibold text-slate-700">Búsqueda lineal y búsqueda binaria</div>

<div class="mt-10 p-6 rounded-xl bg-violet-50 border-l-4 border-violet-600">
Concepto · Funcionamiento · Complejidad · Implementación modular en Python
</div>

---

# ¿Cómo se relacionan con las estructuras de datos?

<div class="grid grid-cols-2 gap-6 mt-8">
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200">
<h2 class="text-violet-800">Estructuras de datos</h2>
<p>Organizan y almacenan información: arreglos, listas y matrices.</p>
</div>
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200">
<h2 class="text-violet-800">Algoritmos de búsqueda</h2>
<p>Permiten localizar información dentro de una estructura.</p>
</div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100">La estructura elegida y la organización de sus datos condicionan qué búsquedas podemos aplicar y con qué eficiencia.</div>

---

# Estructura utilizada en ambas prácticas

`csv.reader()` permite cargar el inventario como una **lista de listas**.

```python
productos = [
    ["P001", "Mouse", "Perifericos", "250", "15"],
    ["P002", "Teclado", "Perifericos", "450", "10"],
    ["P003", "Monitor", "Pantallas", "3200", "6"]
]
```

| Expresión | Significado |
|---|---|
| `productos[1]` | Registro completo en el índice 1 |
| `productos[1][0]` | Código del registro: `P002` |
| `productos[1][1]` | Nombre del producto: `Teclado` |

<div class="mt-4 p-4 rounded-xl bg-violet-50 text-sm">Es una estructura bidimensional implementada con listas de Python, no un arreglo de NumPy. Los valores del CSV se leen como cadenas.</div>

---

<div class="text-violet-700 font-bold tracking-widest">ALGORITMO 1</div>

# Búsqueda lineal

## ¿Qué es?

Es un algoritmo que **examina los elementos de una colección uno por uno**, desde el inicio, hasta encontrar el dato buscado o llegar al final.

<div class="mt-8 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600 text-xl">
No necesita que los registros estén ordenados.
</div>

**Aplicación:** localizar un producto mediante su código dentro de una lista de registros.

---

# Búsqueda lineal · ¿Cómo funciona?

**Objetivo:** buscar `P004` en una lista desordenada.

<div class="mt-7 grid grid-cols-4 gap-3 text-center">
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 0</div><div class="font-bold text-xl">P005</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 1</div><div class="font-bold text-xl">P002</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 2</div><div class="font-bold text-xl">P008</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 3</div><div class="font-bold text-xl">P001</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 4</div><div class="font-bold text-xl">P006</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 5</div><div class="font-bold text-xl">P003</div><div>✗</div></div>
<div class="p-4 bg-violet-50 rounded-xl border"><div class="text-sm">Índice 6</div><div class="font-bold text-xl">P007</div><div>✗</div></div>
<div class="p-4 bg-green-50 rounded-xl border border-green-400"><div class="text-sm">Índice 7</div><div class="font-bold text-xl">P004</div><div>✓</div></div>
</div>

<div class="mt-6 p-4 rounded-xl bg-violet-100">Se comparan los códigos sucesivamente. En este caso, el objetivo aparece en la octava comparación.</div>

---

# Búsqueda lineal · Complejidad

| Escenario | Situación | Complejidad |
|---|---|---|
| Mejor caso | El primer registro coincide | **O(1)** |
| Peor caso | Está al final o no existe | **O(n)** |
| Caso promedio | Se revisa una parte de la lista | **O(n)** |

<div class="mt-8 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600">
<b>n</b> representa la cantidad de registros. A mayor cantidad de registros, mayor puede ser el número de comparaciones.
</div>

**Espacio adicional del algoritmo:** O(1), sin contar los datos ya cargados.

---

# Práctica 1 · Proyecto modular

**Objetivo:** buscar un producto por código en un archivo CSV, sin ordenar los registros.

```text
Practica_BusquedaLineal/
├── main.py
├── algoritmos/
│   ├── __init__.py
│   └── abusquedaLineal.py
├── utilidades/
│   ├── __init__.py
│   └── lector_csv.py
└── datos/
    └── productos.csv
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Los archivos <code>__init__.py</code> pueden permanecer vacíos. Cada módulo tiene una responsabilidad específica.</div>

---

# Práctica 1 · `datos/productos.csv`

**Contenido completo del inventario:**

```csv
codigo,nombre,categoria,precio,existencia
P005,Laptop,Computadoras,14500,4
P002,Teclado,Perifericos,450,10
P008,Disco SSD,Almacenamiento,1250,12
P001,Mouse,Perifericos,250,15
P006,Impresora,Impresion,2800,5
P003,Monitor,Pantallas,3200,6
P007,Memoria USB,Almacenamiento,180,25
P004,Webcam,Perifericos,700,8
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">Los registros están desordenados intencionalmente. La búsqueda lineal funciona sin modificar ese orden.</div>

---

# Práctica 1 · `utilidades/lector_csv.py`

```python
import csv


def cargar_productos(ruta_archivo):
    productos = []

    with open(ruta_archivo, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezados

        for fila in lector:
            productos.append(fila)

    return productos
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Este módulo solo lee el CSV y devuelve una lista de listas. No busca ni ordena registros.</div>

---

# Práctica 1 · `algoritmos/abusquedaLineal.py`

```python
def busquedaLineal(lista, dato_objetivo):
    # Revisar cada registro por su índice
    for i in range(len(lista)):
        # El campo [0] contiene el código
        if lista[i][0] == dato_objetivo:
            # Devolver posición y registro completo
            return i, lista[i]

    # No se encontró el código
    return None
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">El algoritmo recibe datos, realiza comparaciones y devuelve un resultado. No abre archivos ni solicita información al usuario.</div>

---

# Práctica 1 · `main.py` (1/2)

**Importaciones, carga y búsqueda:**

```python
from pathlib import Path

from algoritmos.abusquedaLineal import busquedaLineal
from utilidades.lector_csv import cargar_productos


def main():
    # Ubicar el archivo CSV dentro del proyecto
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"

    # Leer registros sin ordenarlos
    productos = cargar_productos(ruta)

    # Solicitar el código a localizar
    codigo = input("Ingrese el código del producto: ").strip().upper()

    # Ejecutar búsqueda lineal
    resultado = busquedaLineal(productos, codigo)
```

<div class="mt-3 text-sm text-slate-600">El archivo continúa en la siguiente diapositiva: ambas partes forman un único <code>main.py</code>.</div>

---

# Práctica 1 · `main.py` (2/2)

**Continuación dentro de `main()` y punto de entrada:**

```python
    # Mostrar los datos del producto encontrado
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
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">Conserva la indentación: el bloque <code>if resultado...</code> pertenece a <code>main()</code>.</div>

---

# Práctica 1 · Pruebas de ejecución

**Ejecutar desde la raíz del proyecto:**

```bash
python main.py
```

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">
<b>Producto existente</b>

```text
Ingrese el código del producto: P004

Producto encontrado
Posición: 7
Código: P004
Nombre: Webcam
Categoría: Perifericos
Precio: $ 700
Existencia: 8
```
</div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">
<b>Producto inexistente</b>

```text
Ingrese el código del producto: P010

Producto no encontrado
```
</div>
</div>

---

<div class="text-violet-700 font-bold tracking-widest">ALGORITMO 2</div>

# Búsqueda binaria

## ¿Qué es?

Es un algoritmo que **localiza un elemento en una colección ordenada**, comparándolo con el elemento central y reduciendo el intervalo de búsqueda a la mitad en cada paso.

<div class="mt-8 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600 text-xl">
Requiere que los registros estén ordenados por la misma clave utilizada en la comparación.
</div>

**Aplicación:** localizar un producto mediante su código dentro de una lista previamente ordenada.

---

# Búsqueda binaria · ¿Cómo funciona?

**Objetivo:** buscar `P007` en la lista ordenada.

| Iteración | Inicio | Fin | Medio | Código evaluado | Decisión |
|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | P004 | Buscar a la derecha |
| 2 | 4 | 7 | 5 | P006 | Buscar a la derecha |
| 3 | 6 | 7 | 6 | P007 | Encontrado |

<div class="mt-7 p-5 rounded-xl bg-violet-50">
<p><b>Lista:</b> P001 · P002 · P003 · P004 · P005 · P006 · P007 · P008</p>
<p class="mt-3"><b>Regla:</b> si el objetivo es menor que el elemento central, se busca a la izquierda; si es mayor, a la derecha.</p>
</div>

**Resultado:** se encuentra `P007` en el índice 6 después de 3 comparaciones.

---

# Búsqueda binaria · Complejidad

| Escenario | Situación | Complejidad |
|---|---|---|
| Mejor caso | El elemento central coincide | **O(1)** |
| Peor caso | Se reduce el intervalo hasta agotarlo | **O(log n)** |
| Caso promedio | Se descartan mitades sucesivas | **O(log n)** |

<div class="mt-8 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600">
La búsqueda binaria realiza pocas comparaciones incluso con listas grandes, <b>pero el ordenamiento previo tiene un costo</b>.
</div>

**Espacio adicional de la búsqueda iterativa:** O(1). El ordenamiento es una operación separada.

---

# Práctica 2 · Proyecto modular

**Objetivo:** buscar un producto por código después de ordenar los registros.

```text
Practica_BusquedaBinaria/
├── main.py
├── algoritmos/
│   ├── __init__.py
│   └── abusquedaBinaria.py
├── utilidades/
│   ├── __init__.py
│   └── lector_csv.py
└── datos/
    └── productos.csv
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Es un proyecto independiente de la búsqueda lineal. Reutilizamos el lector CSV, pero implementamos otro algoritmo.</div>

---

# Práctica 2 · `datos/productos.csv`

**Contenido completo del inventario (desordenado):**

```csv
codigo,nombre,categoria,precio,existencia
P005,Laptop,Computadoras,14500,4
P002,Teclado,Perifericos,450,10
P008,Disco SSD,Almacenamiento,1250,12
P001,Mouse,Perifericos,250,15
P006,Impresora,Impresion,2800,5
P003,Monitor,Pantallas,3200,6
P007,Memoria USB,Almacenamiento,180,25
P004,Webcam,Perifericos,700,8
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">El CSV permanece desordenado. Ordenaremos la lista <b>en memoria</b> desde <code>main.py</code>, antes de buscar.</div>

---

# Práctica 2 · `utilidades/lector_csv.py`

**Este módulo se reutiliza sin modificaciones:**

```python
import csv


def cargar_productos(ruta_archivo):
    productos = []

    with open(ruta_archivo, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezados

        for fila in lector:
            productos.append(fila)

    return productos
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">El lector desconoce si posteriormente utilizaremos búsqueda lineal o binaria.</div>

---

# Práctica 2 · `algoritmos/abusquedaBinaria.py`

```python
def busquedaBinaria(lista, dato_objetivo):
    inicio = 0                   # Primer índice del intervalo
    fin = len(lista) - 1        # Último índice del intervalo

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Índice central

        if lista[medio][0] == dato_objetivo:
            return medio, lista[medio]  # Encontrado
        elif dato_objetivo < lista[medio][0]:
            fin = medio - 1             # Mitad izquierda
        else:
            inicio = medio + 1          # Mitad derecha

    return None  # No encontrado
```

<div class="mt-3 p-3 rounded-xl bg-violet-50 text-sm"><code>lista[medio][0]</code>: <code>medio</code> selecciona el registro y <code>[0]</code> selecciona su código.</div>

---

# Práctica 2 · `main.py` (1/2)

**Importaciones, carga, ordenamiento y búsqueda:**

```python
from pathlib import Path

from algoritmos.abusquedaBinaria import busquedaBinaria
from utilidades.lector_csv import cargar_productos


def main():
    # Ubicar y leer el archivo CSV
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"
    productos = cargar_productos(ruta)

    # Ordenar por código: primer campo de cada registro
    productos.sort(key=lambda producto: producto[0])

    # Solicitar código y ejecutar búsqueda binaria
    codigo = input("Ingrese el código del producto: ").strip().upper()
    resultado = busquedaBinaria(productos, codigo)
```

<div class="mt-3 text-sm text-slate-600">El archivo continúa en la siguiente diapositiva: ambas partes forman un único <code>main.py</code>.</div>

---

# Práctica 2 · `main.py` (2/2)

**Continuación dentro de `main()` y punto de entrada:**

```python
    # Mostrar el resultado de la búsqueda
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
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">La posición mostrada corresponde a la <b>lista ordenada en memoria</b>, no a la fila original del CSV.</div>

---

# Práctica 2 · Pruebas de ejecución

**Ejecutar desde la raíz del proyecto:**

```bash
python main.py
```

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">
<b>Producto existente</b>

```text
Ingrese el código del producto: P007

Producto encontrado
Posición: 6
Código: P007
Nombre: Memoria USB
Categoría: Almacenamiento
Precio: $ 180
Existencia: 25
```
</div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">
<b>Producto inexistente</b>

```text
Ingrese el código del producto: P010

Producto no encontrado
```
</div>
</div>

---

# Comparación de ambas implementaciones

| Aspecto | Búsqueda lineal | Búsqueda binaria |
|---|---|---|
| Datos | Lista de listas | Lista de listas |
| Archivo CSV | Puede estar desordenado | Puede estar desordenado |
| Preparación en `main.py` | No requiere ordenar | Ordena por código |
| Módulo de búsqueda | `abusquedaLineal.py` | `abusquedaBinaria.py` |
| Peor caso de búsqueda | **O(n)** | **O(log n)** |
| Resultado | `(posición, registro)` o `None` | `(posición, registro)` o `None` |

<div class="mt-6 p-5 rounded-xl bg-violet-100">La estructura modular permite <b>reutilizar la lectura y la presentación</b> y cambiar solamente la estrategia de búsqueda.</div>

---

# ¿Cuál algoritmo elegirías?

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200">
<h2>Una búsqueda aislada</h2>
<p>Inventario pequeño, desordenado y una sola consulta.</p>
<p class="mt-4"><b>La búsqueda lineal puede ser más conveniente.</b></p>
</div>
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200">
<h2>Búsquedas frecuentes</h2>
<p>Inventario grande, ordenado y numerosas consultas.</p>
<p class="mt-4"><b>La búsqueda binaria aprovecha ese orden.</b></p>
</div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100">No solo importa cuánto cuesta buscar: también debemos considerar cómo están organizados los datos y cuánto cuesta prepararlos.</div>

---

# Cierre · Estructuras y algoritmos

<div class="p-6 rounded-xl bg-violet-50 border border-violet-200 mt-8 text-xl">
<b>Pregunta:</b> si recibimos un inventario desordenado y necesitamos localizar un solo producto, ¿ordenarías todo para aplicar búsqueda binaria o utilizarías búsqueda lineal?
</div>

<div class="mt-9 text-2xl font-bold text-center text-violet-800">
Una estructura almacena información. Un algoritmo la procesa. Un programa integra ambos para resolver un problema.
</div>

<div class="mt-10 text-center text-slate-600">Tema 2.1 + Tema 2.2 + complejidad de la Unidad 1</div>
