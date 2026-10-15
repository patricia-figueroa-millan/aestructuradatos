---
theme: default
title: "Cierre del subtema 2.2 | Estructuras de datos y algoritmos de búsqueda"
info: |
  Algoritmia y Estructuras de Datos · Tema 2
  Síntesis posterior a las prácticas de búsqueda lineal y binaria.
class: text-slate-800
transition: fade-out
mdc: true
fonts:
  sans: Arial
  mono: Consolas
---

<style>
.slidev-layout { background: #fff; color: #172033; font-family: Arial, sans-serif; padding: 2.5rem 3.2rem; }
h1 { color: #5b21b6; font-size: 2rem; font-weight: 800; margin-bottom: 1.1rem; }
h2 { color: #6d28d9; font-size: 1.28rem; font-weight: 700; }
p, li { line-height: 1.45; }
strong { color: #5b21b6; }
.card { border: 1px solid #ddd6fe; border-radius: 14px; background: #faf8ff; padding: 1rem 1.2rem; }
.callout { background: #f5f3ff; border-left: 5px solid #7c3aed; padding: .9rem 1.2rem; border-radius: 8px; }
.small { font-size: .84rem; }
code { color: #6d28d9; }
pre { border-radius: 12px !important; font-size: .87rem !important; }
table { width: 100%; font-size: .92rem; }
th { background: #ede9fe; color: #4c1d95; }
th, td { padding: .5rem .7rem; border-bottom: 1px solid #e5e7eb; }
.kicker { color: #7c3aed; font-size: .9rem; font-weight: 700; text-transform: uppercase; letter-spacing: .09em; }
</style>

<div class="kicker">Tema 2 · Subtema 2.2</div>

# ¿Qué aprendimos con las búsquedas?

<div class="text-2xl mt-10 font-bold text-slate-700">De almacenar datos a encontrar información de manera eficiente</div>

<div class="callout mt-12">
Cierre de las prácticas: <b>búsqueda lineal</b> y <b>búsqueda binaria</b> sobre un inventario de productos.
</div>

---

# Dos conceptos que trabajan juntos

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="card">
    <h2>Estructuras de datos</h2>
    <p class="text-xl mt-4">¿Cómo organizamos y almacenamos la información?</p>
    <p class="mt-5">Arreglos, listas y matrices.</p>
  </div>
  <div class="card">
    <h2>Algoritmos de búsqueda</h2>
    <p class="text-xl mt-4">¿Cómo localizamos un dato dentro de esa información?</p>
    <p class="mt-5">Búsqueda lineal y búsqueda binaria.</p>
  </div>
</div>

<div class="callout mt-8 text-lg">
La estructura de datos que elegimos influye en los algoritmos que podemos utilizar y en su eficiencia.
</div>

---

# Relación con las estructuras del tema 2.1

| Estructura | Búsqueda lineal | Búsqueda binaria |
|---|---|---|
| Arreglo (NumPy) | Sí | Sí, si está ordenado |
| Lista de Python | Sí | Sí, si está ordenada |
| Matriz | Sí, mediante un recorrido | Requiere definir un orden y una estrategia de acceso |

<div class="callout mt-7">
No basta con saber que un algoritmo existe: debemos identificar <b>qué condiciones necesita</b> para funcionar correctamente.
</div>

---

# ¿Qué estructura utilizamos en las prácticas?

Leímos <code>productos.csv</code> con <code>csv.reader()</code> y almacenamos los registros en una <b>lista de listas</b>.

```python
productos = [
    ["P001", "Mouse", "Perifericos", "250", "15"],
    ["P002", "Teclado", "Perifericos", "450", "10"],
    ["P003", "Monitor", "Pantallas", "3200", "6"]
]
```

<div class="callout mt-5 small">
Esta estructura es bidimensional, similar a una matriz rectangular, pero está implementada con listas de Python; no es un arreglo de NumPy. Los valores leídos del CSV llegan inicialmente como cadenas de texto.
</div>

---

# Dos índices: registro y campo

| Índice de registro | [0] Código | [1] Nombre | [2] Categoría | [3] Precio | [4] Existencia |
|---:|---|---|---|---:|---:|
| 0 | P001 | Mouse | Perifericos | 250 | 15 |
| 1 | P002 | Teclado | Perifericos | 450 | 10 |
| 2 | P003 | Monitor | Pantallas | 3200 | 6 |

```python
productos[1]       # Registro completo: P002, Teclado, ...
productos[1][0]    # Código del registro: "P002"
productos[1][1]    # Nombre del producto: "Teclado"
```

<div class="callout mt-4">
El primer índice selecciona el <b>registro</b>; el segundo, el <b>campo</b> dentro de ese registro.
</div>

---

# Práctica 1 · Búsqueda lineal

<div class="grid grid-cols-2 gap-7 mt-5">
<div>
  <div class="card">
    <h2>Estrategia</h2>
    <p>Examinar los registros uno por uno hasta encontrar el código solicitado o agotar la lista.</p>
    <p><b>No requiere que los registros estén ordenados.</b></p>
  </div>
  <div class="callout mt-5">En el peor caso revisa los <b>n</b> registros: O(n).</div>
</div>
<div>

```python
def busquedaLineal(lista, dato_objetivo):
    for i in range(len(lista)):
        if lista[i][0] == dato_objetivo:
            return i, lista[i]
    return None
```

</div>
</div>

---

# Práctica 2 · Búsqueda binaria

<div class="grid grid-cols-2 gap-7 mt-5">
<div>
  <div class="card">
    <h2>Estrategia</h2>
    <p>Comparar con el elemento central y descartar la mitad que no puede contener el objetivo.</p>
    <p><b>Necesita que los registros estén ordenados por el campo de búsqueda.</b></p>
  </div>
  <div class="callout mt-5">En el peor caso reduce el intervalo repetidamente: O(log n).</div>
</div>
<div>

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

</div>
</div>

---

# ¿Qué significa lista[medio][0]?

```python
medio = (inicio + fin) // 2

if lista[medio][0] == dato_objetivo:
    return medio, lista[medio]
```

<div class="grid grid-cols-3 gap-4 mt-7">
  <div class="card"><h2>medio</h2><p>Índice del registro central del intervalo actual.</p></div>
  <div class="card"><h2>lista[medio]</h2><p>Registro completo ubicado en esa posición.</p></div>
  <div class="card"><h2>[0]</h2><p>Primer campo del registro: código del producto.</p></div>
</div>

<div class="callout mt-6">
El índice corresponde a la <b>lista en memoria</b>; después de ordenar, puede no coincidir con la fila original del CSV.
</div>

---

# La diferencia decisiva: el orden

<div class="grid grid-cols-2 gap-6 mt-5">
  <div class="card">
    <h2>CSV desordenado</h2>
    <p class="font-mono text-lg mt-4">P005 · P002 · P008 · P001<br>P006 · P003 · P007 · P004</p>
    <p class="mt-5">Podemos aplicar búsqueda lineal directamente.</p>
  </div>
  <div class="card">
    <h2>Lista ordenada por código</h2>
    <p class="font-mono text-lg mt-4">P001 · P002 · P003 · P004<br>P005 · P006 · P007 · P008</p>
    <p class="mt-5">Ahora también podemos aplicar búsqueda binaria.</p>
  </div>
</div>

```python
productos.sort(key=lambda producto: producto[0])
```

<div class="callout mt-4 small">Ordenamos antes de llamar al algoritmo. La búsqueda binaria no ordena los datos por sí misma.</div>

---

# Mismo objetivo, distinto recorrido

**Buscar P007** en una lista ordenada de ocho registros:

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="card">
    <h2>Lineal</h2>
    <p class="font-mono mt-4">P001 → P002 → P003 → P004<br>P005 → P006 → <b>P007</b></p>
    <p class="mt-5 text-xl"><b>7 comparaciones</b></p>
  </div>
  <div class="card">
    <h2>Binaria</h2>
    <p class="font-mono mt-4">P004 → P006 → <b>P007</b></p>
    <p class="mt-5 text-xl"><b>3 comparaciones</b></p>
  </div>
</div>

<div class="callout mt-8">El resultado es el mismo; cambia la cantidad de elementos que necesitamos evaluar.</div>

---

# Recuperamos la complejidad de la Unidad 1

| Algoritmo | Mejor caso | Peor caso | Requisito |
|---|---:|---:|---|
| Lineal | O(1) | O(n) | Ningún orden previo |
| Binaria | O(1) | O(log n) | Datos ordenados por la clave |

<div class="card mt-7">
  <h2>Ejemplo: un millón de registros</h2>
  <p class="mt-3">La búsqueda lineal podría examinar hasta <b>1,000,000</b> registros. La binaria, sobre datos ya ordenados, necesita como máximo alrededor de <b>20</b> comparaciones.</p>
</div>

<div class="small mt-4 text-slate-600">Se compara únicamente el costo de la búsqueda, suponiendo acceso por índice O(1); no se incluye la carga ni el ordenamiento previo.</div>

---

# ¿La búsqueda binaria siempre es mejor?

<div class="grid grid-cols-2 gap-6 mt-7">
  <div class="card">
    <h2>Una búsqueda aislada</h2>
    <p>Tenemos pocos registros desordenados y solo buscamos una vez.</p>
    <p class="mt-4"><b>La búsqueda lineal puede ser más conveniente:</b> evita ordenar previamente.</p>
  </div>
  <div class="card">
    <h2>Búsquedas frecuentes</h2>
    <p>Tenemos muchos registros, ordenados por código, y realizamos numerosas consultas.</p>
    <p class="mt-4"><b>La búsqueda binaria puede aprovechar mejor ese orden.</b></p>
  </div>
</div>

<div class="callout mt-8 text-lg">Elegir un algoritmo también implica considerar el estado de los datos y el costo de prepararlos.</div>

---

# Así se integró nuestro proyecto modular

<div class="grid grid-cols-3 gap-5 mt-8">
  <div class="card"><h2>datos/</h2><p><code>productos.csv</code></p><p>Fuente de información.</p></div>
  <div class="card"><h2>utilidades/</h2><p><code>lector_csv.py</code></p><p>Convierte el archivo en una lista de listas.</p></div>
  <div class="card"><h2>algoritmos/</h2><p><code>abusquedaLineal.py</code> o <code>abusquedaBinaria.py</code></p><p>Contiene la lógica de búsqueda.</p></div>
</div>

<div class="card mt-5"><h2>main.py</h2><p>Coordina la carga, el ordenamiento cuando corresponde, la solicitud del código y la presentación del resultado.</p></div>

<div class="callout mt-5">Una estructura almacena datos; un algoritmo los procesa; el programa integra ambos.</div>

---

# Para discutir antes de cerrar

<div class="card mt-7">
  <p class="text-xl"><b>Situación:</b> recibimos un nuevo inventario desordenado y necesitamos localizar un solo producto por código.</p>
  <p class="text-xl mt-6">¿Ordenarías todos los registros para utilizar búsqueda binaria o aplicarías búsqueda lineal?</p>
</div>

<div class="mt-8 text-lg text-slate-700">Justifica tu decisión considerando:</div>

1. Cómo están organizados los datos.
2. Cuántas búsquedas necesitamos realizar.
3. Qué trabajo previo requiere cada algoritmo.

---

# Idea final

<div class="text-3xl font-bold text-center mt-15 text-violet-800 leading-relaxed">
No se trata solo de programar una búsqueda.<br><br>
Se trata de elegir una estructura de datos y un algoritmo adecuados para resolver el problema con eficiencia.
</div>

<div class="text-center mt-12 text-slate-600">Tema 2.1 + Tema 2.2 + análisis de complejidad de la Unidad 1</div>
