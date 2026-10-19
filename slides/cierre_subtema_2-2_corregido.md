---
theme: default
title: "Cierre del subtema 2.2 - Estructuras y búsqueda"
class: text-slate-800
transition: fade
---

<div class="text-violet-700 font-bold text-sm tracking-widest">TEMA 2 · SUBTEMA 2.2</div>

# ¿Qué aprendimos con las búsquedas?

<div class="text-2xl mt-10 font-bold text-slate-700">
De almacenar datos a encontrar información de manera eficiente
</div>

<div class="mt-10 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600">
Cierre de las prácticas: <b>búsqueda lineal</b> y <b>búsqueda binaria</b> sobre un inventario de productos.
</div>

---

# Dos conceptos que trabajan juntos

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="p-6 rounded-xl border border-violet-200 bg-violet-50">
    <h2 class="text-violet-800">Estructuras de datos</h2>
    <p class="text-xl mt-4">¿Cómo organizamos y almacenamos la información?</p>
    <p class="mt-5">Arreglos, listas y matrices.</p>
  </div>
  <div class="p-6 rounded-xl border border-violet-200 bg-violet-50">
    <h2 class="text-violet-800">Algoritmos de búsqueda</h2>
    <p class="text-xl mt-4">¿Cómo localizamos un dato dentro de esa información?</p>
    <p class="mt-5">Búsqueda lineal y búsqueda binaria.</p>
  </div>
</div>

<div class="mt-8 p-5 rounded-xl bg-violet-100 text-lg">
La estructura de datos elegida influye en los algoritmos que podemos utilizar y en su eficiencia.
</div>

---

# Relación con las estructuras del tema 2.1

| Estructura | Búsqueda lineal | Búsqueda binaria |
|---|---|---|
| Arreglo (NumPy) | Sí | Sí, si está ordenado |
| Lista de Python | Sí | Sí, si está ordenada |
| Matriz | Sí, mediante un recorrido | Requiere definir un orden y una estrategia de acceso |

<div class="mt-8 p-5 rounded-xl bg-violet-50 border-l-4 border-violet-600">
No basta con saber que un algoritmo existe: debemos identificar <b>qué condiciones necesita</b> para funcionar correctamente.
</div>

---

# ¿Qué estructura utilizamos en las prácticas?

Leímos `productos.csv` con `csv.reader()` y almacenamos los registros en una **lista de listas**.

```python
productos = [
    ["P001", "Mouse", "Perifericos", "250", "15"],
    ["P002", "Teclado", "Perifericos", "450", "10"],
    ["P003", "Monitor", "Pantallas", "3200", "6"]
]
```

<div class="mt-5 p-4 rounded-xl bg-violet-50 text-sm">
Es una estructura bidimensional, similar a una matriz rectangular, implementada con listas de Python. No es un arreglo de NumPy. Los datos leídos del CSV llegan inicialmente como texto.
</div>

---

# Dos índices: registro y campo

| Registro | [0] Código | [1] Nombre | [2] Categoría | [3] Precio | [4] Existencia |
|---:|---|---|---|---:|---:|
| 0 | P001 | Mouse | Perifericos | 250 | 15 |
| 1 | P002 | Teclado | Perifericos | 450 | 10 |
| 2 | P003 | Monitor | Pantallas | 3200 | 6 |

```python
productos[1]       # Registro completo
productos[1][0]    # "P002": código
productos[1][1]    # "Teclado": nombre
```

<div class="mt-4 p-4 rounded-xl bg-violet-50">
El primer índice selecciona el <b>registro</b>; el segundo, el <b>campo</b> de ese registro.
</div>

---

# Práctica 1 · Búsqueda lineal

<div class="grid grid-cols-2 gap-6 mt-5">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Estrategia</h2>
<p>Examinar los registros uno por uno hasta encontrar el código solicitado o agotar la lista.</p>
<p><b>No requiere que estén ordenados.</b></p>
<p>Peor caso: <b>O(n)</b>.</p>
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

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Estrategia</h2>
<p>Comparar con el elemento central y descartar la mitad que no puede contener el objetivo.</p>
<p><b>Necesita datos ordenados por el campo de búsqueda.</b></p>
<p>Peor caso: <b>O(log n)</b>.</p>
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

# ¿Qué significa `lista[medio][0]`?

```python
medio = (inicio + fin) // 2

if lista[medio][0] == dato_objetivo:
    return medio, lista[medio]
```

<div class="grid grid-cols-3 gap-4 mt-7">
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>medio</h2><p>Índice del registro central.</p></div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>lista[medio]</h2><p>Registro completo.</p></div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>[0]</h2><p>Primer campo: código.</p></div>
</div>

<div class="mt-6 p-4 rounded-xl bg-violet-100">
El índice corresponde a la lista en memoria; después de ordenar, puede no coincidir con la fila original del CSV.
</div>

---

# La diferencia decisiva: el orden

<div class="grid grid-cols-2 gap-6 mt-5">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>CSV desordenado</h2>
<p class="font-mono mt-4">P005 · P002 · P008 · P001</p>
<p class="font-mono">P006 · P003 · P007 · P004</p>
<p class="mt-5">Podemos aplicar búsqueda lineal directamente.</p>
</div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Lista ordenada por código</h2>
<p class="font-mono mt-4">P001 · P002 · P003 · P004</p>
<p class="font-mono">P005 · P006 · P007 · P008</p>
<p class="mt-5">Ahora también podemos aplicar búsqueda binaria.</p>
</div>
</div>

```python
productos.sort(key=lambda producto: producto[0])
```

La búsqueda binaria no ordena los datos por sí misma.

---

# Mismo objetivo, distinto recorrido

**Buscar P007** en una lista ordenada de ocho registros:

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Lineal</h2>
<p class="font-mono mt-4">P001 → P002 → P003 → P004</p>
<p class="font-mono">P005 → P006 → <b>P007</b></p>
<p class="mt-5 text-xl"><b>7 comparaciones</b></p>
</div>
<div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
<h2>Binaria</h2>
<p class="font-mono mt-4">P004 → P006 → <b>P007</b></p>
<p class="mt-5 text-xl"><b>3 comparaciones</b></p>
</div>
</div>

<div class="mt-8 p-4 rounded-xl bg-violet-100">El resultado es el mismo; cambia la cantidad de elementos evaluados.</div>

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

# Así se integró nuestro proyecto modular

<div class="grid grid-cols-3 gap-5 mt-8">
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>datos/</h2><p><code>productos.csv</code></p><p>Fuente de información.</p></div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>utilidades/</h2><p><code>lector_csv.py</code></p><p>Carga una lista de listas.</p></div>
<div class="p-4 rounded-xl bg-violet-50 border border-violet-200"><h2>algoritmos/</h2><p>Archivo de búsqueda lineal o binaria.</p><p>Lógica de búsqueda.</p></div>
</div>

<div class="p-4 rounded-xl bg-violet-50 border border-violet-200 mt-5"><h2>main.py</h2><p>Coordina la carga, el ordenamiento cuando corresponde, la consulta y la presentación del resultado.</p></div>

<div class="mt-5 p-4 rounded-xl bg-violet-100">Una estructura almacena datos; un algoritmo los procesa; el programa integra ambos.</div>

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
