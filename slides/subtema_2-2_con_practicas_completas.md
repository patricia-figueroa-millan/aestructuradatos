---
theme: default
title: "Subtema 2.2 - Búsqueda lineal y binaria"
class: text-slate-800
transition: fade
---

<div class="text-violet-700 font-bold text-sm tracking-widest">TEMA 2 · SUBTEMA 2.2</div>

# Algoritmos de búsqueda

<div class="text-2xl mt-8 font-semibold text-slate-700">Búsqueda lineal y búsqueda binaria</div>

<div class="mt-10 p-6 rounded-xl bg-violet-50 border-l-4 border-violet-600 text-xl">
¿Qué hacen, cómo funcionan y cómo los implementamos en Python con módulos?
</div>

---

# ¿Qué es un algoritmo de búsqueda?

Es un conjunto de pasos para **localizar un dato** dentro de una colección.

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Entrada</h2><p>Una colección de registros y el dato que buscamos.</p><p class="font-mono mt-4">Objetivo: P007</p></div>
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Salida</h2><p>La posición y el registro encontrado; o <code>None</code> si no existe.</p></div>
</div>

<div class="mt-7 p-4 rounded-xl bg-violet-100">En las prácticas buscamos productos por su <b>código</b>.</div>

---

# Nuestros datos: una lista de listas

```python
productos = [
    ["P001", "Mouse", "Perifericos", "250", "15"],
    ["P002", "Teclado", "Perifericos", "450", "10"],
    ["P003", "Monitor", "Pantallas", "3200", "6"]
]
```

| Expresión | ¿Qué selecciona? | Resultado |
|---|---|---|
| `productos[1]` | Registro de índice 1 | Lista del teclado |
| `productos[1][0]` | Código de ese registro | `"P002"` |
| `productos[1][1]` | Nombre de ese registro | `"Teclado"` |

<div class="mt-4 p-4 rounded-xl bg-violet-50">El primer índice identifica el <b>registro</b> y el segundo identifica el <b>campo</b>.</div>

---

# Búsqueda lineal: ¿qué es?

La **búsqueda lineal** revisa los elementos **uno por uno**, desde el inicio, hasta encontrar el objetivo o terminar la colección.

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>Ventaja</h2><p>Funciona aunque los datos estén desordenados.</p></div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>Limitación</h2><p>En el peor caso necesita revisar todos los registros.</p></div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100 text-xl">Peor caso: <b>O(n)</b></div>

---

# ¿Cómo funciona la búsqueda lineal?

**Objetivo: P004**

<div class="grid grid-cols-4 gap-3 mt-8 text-center">
<div class="p-4 rounded-xl bg-slate-100 border border-slate-300"><b>0 · P001</b><p>¿P004? No</p></div>
<div class="p-4 rounded-xl bg-slate-100 border border-slate-300"><b>1 · P002</b><p>¿P004? No</p></div>
<div class="p-4 rounded-xl bg-slate-100 border border-slate-300"><b>2 · P003</b><p>¿P004? No</p></div>
<div class="p-4 rounded-xl bg-violet-100 border-2 border-violet-600"><b>3 · P004</b><p>¡Encontrado!</p></div>
</div>

<div class="mt-9 p-5 rounded-xl bg-violet-50">Se realizan <b>4 comparaciones</b>. El algoritmo devuelve <code>(3, registro)</code>.</div>

---

# Búsqueda lineal: implementación en Python

**Archivo:** `algoritmos/abusquedaLineal.py`

```python
def busquedaLineal(lista, dato_objetivo):
    # Recorrer cada registro por su índice
    for i in range(len(lista)):
        # Comparar el código (campo 0) con el objetivo
        if lista[i][0] == dato_objetivo:
            return i, lista[i]
    # No se encontró el código
    return None
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">El algoritmo <b>no lee el CSV</b> ni solicita datos: solo recibe una lista y un objetivo.</div>

---

# Búsqueda binaria: ¿qué es?

La **búsqueda binaria** examina el elemento central y **descarta la mitad** de los elementos que no pueden contener el objetivo.

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>Condición indispensable</h2><p>Los datos deben estar <b>ordenados</b> por el campo que buscamos.</p></div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>Ventaja</h2><p>Reduce el intervalo de búsqueda en cada iteración.</p></div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100 text-xl">Peor caso: <b>O(log n)</b>, una vez ordenados los datos.</div>

---

# Búsqueda binaria: paso a paso

**Lista ordenada:** `P001 P002 P003 P004 P005 P006 P007 P008`  
**Objetivo:** `P007`

| Paso | inicio | fin | medio | Código central | Decisión |
|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | P004 | P007 es mayor → derecha |
| 2 | 4 | 7 | 5 | P006 | P007 es mayor → derecha |
| 3 | 6 | 7 | 6 | P007 | ¡Encontrado! |

<div class="mt-7 p-5 rounded-xl bg-violet-50">Solo se realizan <b>3 comparaciones</b>. Se devuelve <code>(6, registro)</code>.</div>

---

# Búsqueda binaria: implementación en Python

**Archivo:** `algoritmos/abusquedaBinaria.py`

```python
def busquedaBinaria(lista, dato_objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0] == dato_objetivo:
            return medio, lista[medio]
        elif dato_objetivo < lista[medio][0]:
            fin = medio - 1
        else:
            inicio = medio + 1
    return None
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">`medio` es el índice del registro; `[0]` es el campo donde está el código.</div>

---

# ¿Qué hacen `inicio`, `fin` y `medio`?

<div class="grid grid-cols-3 gap-4 mt-7">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>inicio</h2><p>Primer índice del intervalo que aún podemos revisar.</p></div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>fin</h2><p>Último índice del intervalo.</p></div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200"><h2>medio</h2><p>Índice central calculado con división entera.</p></div>
</div>

```python
medio = (inicio + fin) // 2
```

<div class="mt-6 p-4 rounded-xl bg-violet-100">Si el objetivo es menor que el código central, cambia <code>fin</code>. Si es mayor, cambia <code>inicio</code>.</div>

---

# Antes de buscar: cargar y ordenar

**El archivo `productos.csv` puede estar desordenado.**

```python
# Cargar registros desde el CSV
productos = cargar_productos(ruta)

# Solo para búsqueda binaria: ordenar por código
productos.sort(key=lambda producto: producto[0])
```

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="p-4 rounded-xl bg-slate-100"><h2>Lineal</h2><p>Puede buscar directamente después de cargar.</p></div>
<div class="p-4 rounded-xl bg-violet-50"><h2>Binaria</h2><p>Primero requiere ordenar por el código.</p></div>
</div>

---

# Estructura modular de nuestras prácticas

```text
Practica_BusquedaBinaria/
├── main.py
├── datos/
│   └── productos.csv
├── utilidades/
│   ├── __init__.py
│   └── lector_csv.py
└── algoritmos/
    ├── __init__.py
    └── abusquedaBinaria.py
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">En la práctica lineal se conserva la misma organización, cambiando el módulo del algoritmo por <code>abusquedaLineal.py</code>.</div>

---

# Módulo de lectura: `lector_csv.py`

**Responsabilidad:** abrir el archivo y devolver los registros como una lista de listas.

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

<div class="mt-4 p-4 rounded-xl bg-violet-50">Este módulo se reutiliza <b>sin cambios</b> en ambas prácticas.</div>

---

# `main.py`: integrar los módulos

```python
from pathlib import Path
from algoritmos.abusquedaBinaria import busquedaBinaria
from utilidades.lector_csv import cargar_productos

def main():
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"
    productos = cargar_productos(ruta)
    productos.sort(key=lambda producto: producto[0])
    codigo = input("Código del producto: ").strip().upper()
    resultado = busquedaBinaria(productos, codigo)
    if resultado is not None:
        posicion, producto = resultado
        print("Posición:", posicion, "Producto:", producto)
    else:
        print("Producto no encontrado")

if __name__ == "__main__":
    main()
```

---

# ¿Qué cambia en `main.py` para búsqueda lineal?

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Se conserva</h2><p>La ruta del CSV, la lectura de productos, la solicitud del código y la presentación del resultado.</p></div>
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Se modifica</h2><p>Se importa y llama a <code>busquedaLineal</code>; ya no es necesario ordenar.</p></div>
</div>

```python
from algoritmos.abusquedaLineal import busquedaLineal

# Dentro de main(), después de cargar los productos:
resultado = busquedaLineal(productos, codigo)
```

<div class="mt-5 p-4 rounded-xl bg-violet-100">Ambas funciones devuelven <code>(posición, registro)</code> o <code>None</code>: así, <code>main.py</code> puede procesar sus resultados de la misma manera.</div>

---

# ¿Qué responsabilidad tiene cada archivo?

| Archivo | Función |
|---|---|
| `productos.csv` | Almacenar los registros |
| `lector_csv.py` | Leer el CSV y crear la lista de listas |
| `abusquedaLineal.py` | Recorrer registros uno por uno |
| `abusquedaBinaria.py` | Buscar por mitades en datos ordenados |
| `main.py` | Coordinar módulos, entrada y salida |

<div class="mt-7 p-5 rounded-xl bg-violet-50">La separación modular permite <b>reutilizar componentes</b> y cambiar el algoritmo sin reescribir todo el programa.</div>

---

# Cierre: relacionamos estructuras y algoritmos

<div class="text-lg mt-5">Ya implementamos dos estrategias de búsqueda sobre la <b>misma estructura: una lista de listas</b>.</div>

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Estructura</h2><p>Determina cómo almacenamos y accedemos a los registros.</p></div>
<div class="p-5 rounded-xl border border-violet-200 bg-violet-50"><h2>Algoritmo</h2><p>Determina cómo recorremos o descartamos registros para encontrar el objetivo.</p></div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100">La organización de los datos condiciona la estrategia de búsqueda y su eficiencia.</div>

---

# Recuperamos la complejidad de la Unidad 1

| Algoritmo | Mejor caso | Peor caso | Requisito |
|---|---:|---:|---|
| Lineal | O(1) | O(n) | No necesita orden previo |
| Binaria | O(1) | O(log n) | Datos ordenados por la clave |

<div class="p-5 rounded-xl bg-violet-50 border border-violet-200 mt-7">
<h2>Ejemplo: un millón de registros</h2>
<p>La búsqueda lineal podría examinar hasta <b>1,000,000</b> registros. La binaria, con los datos ya ordenados, necesita como máximo alrededor de <b>20</b> comparaciones.</p>
</div>

<p class="text-sm mt-4 text-slate-600">Se considera únicamente el costo de buscar, con acceso por índice O(1); no se incluye la carga ni el ordenamiento previo.</p>

---

# ¿La búsqueda binaria siempre es mejor?

<div class="grid grid-cols-2 gap-6 mt-7">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Una búsqueda aislada</h2>
<p>Pocos registros desordenados y una sola consulta.</p>
<p class="mt-4"><b>La búsqueda lineal puede convenir:</b> evita ordenar previamente.</p>
</div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Búsquedas frecuentes</h2>
<p>Muchos registros ya ordenados y numerosas consultas.</p>
<p class="mt-4"><b>La búsqueda binaria aprovecha ese orden.</b></p>
</div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100 text-lg">Elegir un algoritmo también implica considerar el estado de los datos y el costo de prepararlos.</div>

---

# Para discutir antes de cerrar

<div class="p-6 rounded-xl bg-violet-50 border border-violet-200 mt-7">
<p class="text-xl"><b>Situación:</b> recibimos un nuevo inventario desordenado y necesitamos localizar un solo producto por código.</p>
<p class="text-xl mt-6">¿Ordenarías todos los registros para utilizar búsqueda binaria o aplicarías búsqueda lineal?</p>
</div>

<div class="mt-8 text-lg">Justifica tu decisión considerando:</div>

1. Cómo están organizados los datos.
2. Cuántas búsquedas necesitamos realizar.
3. Qué trabajo previo requiere cada algoritmo.

---

# Idea final

<div class="text-3xl font-bold text-center mt-16 text-violet-800 leading-relaxed">
<p>No se trata solo de programar una búsqueda.</p>
<p class="mt-8">Se trata de elegir una estructura de datos y un algoritmo adecuados para resolver el problema con eficiencia.</p>
</div>

<div class="text-center mt-12 text-slate-600">Tema 2.1 + Tema 2.2 + análisis de complejidad de la Unidad 1</div>

---

# Prácticas completas · Implementación modular

<div class="grid grid-cols-2 gap-6 mt-10">
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200"><h2>Práctica 1</h2><p class="text-xl">Búsqueda lineal</p><p>Inventario sin necesidad de ordenar.</p></div>
<div class="p-6 rounded-xl bg-violet-50 border border-violet-200"><h2>Práctica 2</h2><p class="text-xl">Búsqueda binaria</p><p>Inventario ordenado antes de buscar.</p></div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100">Cada práctica se desarrolla en una <b>carpeta independiente</b> y puede ejecutarse con <code>python main.py</code>.</div>

---

# Práctica 1 · Búsqueda lineal: estructura

```text
Practica_BusquedaLineal/
├── main.py
├── algoritmos/
│   ├── __init__.py
│   └── abusquedaLineal.py
├── datos/
│   └── productos.csv
└── utilidades/
    ├── __init__.py
    └── lector_csv.py
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Los archivos <code>__init__.py</code> se dejan vacíos. Los datos se cargan desde el CSV y se buscan sin ordenar.</div>

---

# Práctica 1 · `datos/productos.csv`

```csv
codigo,nombre,categoria,precio,existencia
P001,Mouse,Perifericos,250,15
P002,Teclado,Perifericos,450,10
P003,Monitor,Pantallas,3200,6
P004,Webcam,Perifericos,700,8
P005,Laptop,Computadoras,14500,4
P006,Impresora,Impresion,2800,5
P007,Memoria USB,Almacenamiento,180,25
P008,Disco SSD,Almacenamiento,1250,12
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">Cada fila contiene un registro; <code>csv.reader()</code> lo convertirá en una lista de cadenas.</div>

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

<div class="mt-4 p-4 rounded-xl bg-violet-50">Este módulo <b>solo lee</b> el archivo y devuelve una lista de listas; no busca productos.</div>

---

# Práctica 1 · `algoritmos/abusquedaLineal.py`

```python
def busquedaLineal(lista, dato_objetivo):
    # Revisar los registros uno por uno
    for i in range(len(lista)):
        # [0] corresponde al código del producto
        if lista[i][0] == dato_objetivo:
            return i, lista[i]

    # No se encontró el código solicitado
    return None
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Retorna <code>(posición, registro)</code> cuando encuentra el producto; de lo contrario, <code>None</code>.</div>

---

# Práctica 1 · `main.py` (solución completa)

```python
from pathlib import Path
from algoritmos.abusquedaLineal import busquedaLineal
from utilidades.lector_csv import cargar_productos


def main():
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"
    productos = cargar_productos(ruta)

    codigo = input("Ingrese el código del producto: ").strip().upper()
    resultado = busquedaLineal(productos, codigo)

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

---

# Práctica 1 · Comprobar el resultado

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Producto existente</h2>
<pre class="text-sm">Ingrese el código del producto: P007

Producto encontrado
Posición: 6
Código: P007
Nombre: Memoria USB
Categoría: Almacenamiento
Precio: $ 180
Existencia: 25</pre>
</div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Producto inexistente</h2>
<pre class="text-sm">Ingrese el código del producto: P010

Producto no encontrado</pre>
</div>
</div>

---

# Práctica 2 · Búsqueda binaria: estructura

```text
Practica_BusquedaBinaria/
├── main.py
├── algoritmos/
│   ├── __init__.py
│   └── abusquedaBinaria.py
├── datos/
│   └── productos.csv
└── utilidades/
    ├── __init__.py
    └── lector_csv.py
```

<div class="mt-5 p-4 rounded-xl bg-violet-50">Se reutiliza <code>lector_csv.py</code> sin cambios. El archivo CSV estará desordenado para demostrar por qué debemos ordenar antes de la búsqueda binaria.</div>

---

# Práctica 2 · `datos/productos.csv`

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

<div class="mt-4 p-4 rounded-xl bg-violet-50">El CSV está <b>desordenado por código</b>. La función de búsqueda binaria no debe ejecutarse directamente sobre este orden.</div>

---

# Práctica 2 · `utilidades/lector_csv.py`

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

<div class="mt-4 p-4 rounded-xl bg-violet-50">Es el <b>mismo módulo</b> de la práctica lineal: la lectura del archivo es independiente del algoritmo de búsqueda.</div>

---

# Práctica 2 · `algoritmos/abusquedaBinaria.py`

```python
def busquedaBinaria(lista, dato_objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio][0] == dato_objetivo:
            return medio, lista[medio]
        elif dato_objetivo < lista[medio][0]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return None
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">La lista debe llegar <b>ordenada por código</b>. <code>medio</code> es el índice del registro central; <code>[0]</code> selecciona su código.</div>

---

# Práctica 2 · `main.py` (solución completa)

```python
from pathlib import Path
from algoritmos.abusquedaBinaria import busquedaBinaria
from utilidades.lector_csv import cargar_productos


def main():
    ruta = Path(__file__).resolve().parent / "datos" / "productos.csv"
    productos = cargar_productos(ruta)
    productos.sort(key=lambda producto: producto[0])

    codigo = input("Ingrese el código del producto: ").strip().upper()
    resultado = busquedaBinaria(productos, codigo)

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

---

# Práctica 2 · Comprobar el resultado

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Producto existente</h2>
<pre class="text-sm">Ingrese el código del producto: P007

Producto encontrado
Posición: 6
Código: P007
Nombre: Memoria USB
Categoría: Almacenamiento
Precio: $ 180
Existencia: 25</pre>
</div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Producto inexistente</h2>
<pre class="text-sm">Ingrese el código del producto: P010

Producto no encontrado</pre>
</div>
</div>

<div class="mt-5 p-4 rounded-xl bg-violet-100">La posición mostrada corresponde a la <b>lista ordenada en memoria</b>, no a la fila original del CSV.</div>

---

# Cierre de las prácticas · ¿Qué cambia?

| Componente | Búsqueda lineal | Búsqueda binaria |
|---|---|---|
| `datos/productos.csv` | Orden no indispensable | Se ordena en memoria |
| `utilidades/lector_csv.py` | Se reutiliza | Se reutiliza |
| `algoritmos/` | `abusquedaLineal.py` | `abusquedaBinaria.py` |
| `main.py` | Carga y busca | Carga, ordena y busca |
| Complejidad de búsqueda | O(n) | O(log n) |

<div class="mt-7 p-5 rounded-xl bg-violet-100 text-lg">La estructura almacena los datos; el algoritmo determina cómo buscarlos; <code>main.py</code> integra las partes.</div>

