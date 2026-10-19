---
theme: default
title: "3.1 Algoritmos de ordenamiento"
class: text-slate-800
transition: fade
---

<div class="text-violet-700 font-bold text-sm tracking-widest">TEMA 3 · ALGORITMOS DE ORDENAMIENTO Y ESTRUCTURAS DE DATOS AVANZADAS</div>

# 3.1 Algoritmos de ordenamiento

<div class="mt-10 p-6 rounded-2xl bg-violet-50 border-l-4 border-violet-600">
  <p class="text-2xl font-semibold">¿Cómo podemos organizar los mismos datos utilizando estrategias diferentes?</p>
</div>

<div class="mt-8 font-mono text-xl text-center bg-slate-900 text-white rounded-xl p-5">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="mt-6 text-slate-600">Objetivo: reconocer los fundamentos, las operaciones y las estrategias de seis algoritmos de ordenamiento.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · FUNDAMENTOS</div>

# ¿Qué es ordenar datos?

El **ordenamiento** es el proceso algorítmico de reorganizar una colección según un **criterio establecido**.

<div class="grid grid-cols-2 gap-5 mt-8">
  <div class="p-5 bg-slate-100 rounded-xl">
    <div class="font-bold mb-3">Lista original</div>
    <div class="font-mono text-lg break-words">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>
  </div>
  <div class="p-5 bg-emerald-50 border border-emerald-200 rounded-xl">
    <div class="font-bold mb-3">Orden ascendente</div>
    <div class="font-mono text-lg break-words">[17, 20, 26, 31, 44, 54, 55, 77, 93]</div>
  </div>
</div>

<div class="mt-7 p-4 rounded-xl bg-violet-50 border-l-4 border-violet-500">Los valores se conservan; cambia su posición dentro de la colección.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · FUNDAMENTOS</div>

# Criterio ≠ algoritmo

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="p-5 bg-blue-50 border border-blue-200 rounded-xl">
    <h3 class="font-bold text-xl text-blue-800">Criterio de ordenamiento</h3>
    <p class="mt-3">Define <strong>cómo deben quedar</strong> organizados los datos: ascendente, descendente o según un atributo.</p>
  </div>
  <div class="p-5 bg-violet-50 border border-violet-200 rounded-xl">
    <h3 class="font-bold text-xl text-violet-800">Algoritmo de ordenamiento</h3>
    <p class="mt-3">Define <strong>qué pasos se siguen</strong> para alcanzar el orden deseado.</p>
  </div>
</div>

<div class="mt-7 bg-slate-900 text-white rounded-xl p-5 text-center">
  <div class="font-mono">Ascendente → [17, 20, 26, 31, 44, 54, 55, 77, 93]</div>
  <div class="font-mono mt-3">Descendente → [93, 77, 55, 54, 44, 31, 26, 20, 17]</div>
</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · APLICACIONES</div>

# Ordenar es parte del procesamiento de datos

<div class="grid grid-cols-2 gap-4 mt-7">
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>Consultar:</strong> presentar registros por fecha, precio o nombre.</div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>Analizar:</strong> identificar valores extremos o elementos próximos.</div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>Agrupar:</strong> acercar registros con claves iguales.</div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>Buscar:</strong> preparar datos para búsqueda binaria.</div>
</div>

<div class="mt-8 p-5 bg-amber-50 border-l-4 border-amber-500 rounded-xl">
  <strong>Importante:</strong> ordenar también cuesta tiempo. No siempre conviene ordenar antes de realizar una búsqueda.
</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · CONEXIÓN CON EL TEMA 2</div>

# ¿Ordenar antes de buscar?

<div class="font-mono text-lg mt-5 bg-slate-100 rounded-lg p-4 text-center">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="grid grid-cols-2 gap-5 mt-6">
  <div class="p-5 bg-blue-50 rounded-xl border border-blue-200">
    <h3 class="font-bold text-blue-800">Búsqueda lineal</h3>
    <p class="mt-2">No exige orden previo.</p>
    <p class="mt-2 font-mono">Peor caso: O(n)</p>
  </div>
  <div class="p-5 bg-violet-50 rounded-xl border border-violet-200">
    <h3 class="font-bold text-violet-800">Búsqueda binaria</h3>
    <p class="mt-2">Exige datos ordenados por la clave buscada.</p>
    <p class="mt-2 font-mono">Peor caso: O(log n)</p>
  </div>
</div>

<div class="mt-6 p-4 bg-amber-50 rounded-xl border-l-4 border-amber-500">Para una sola búsqueda, ordenar primero puede ser innecesario; para muchas búsquedas sobre datos que cambian poco, podría compensar.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · HERRAMIENTAS</div>

# Python puede ordenar, pero ¿cómo lo hace?

```python
numeros = [54, 26, 93, 17, 77, 31, 44, 55, 20]

numeros.sort()
print(numeros)
```

<div class="mt-5 p-4 bg-emerald-50 border border-emerald-200 rounded-xl font-mono text-lg">[17, 20, 26, 31, 44, 54, 55, 77, 93]</div>

<div class="mt-7 p-5 bg-violet-50 rounded-xl border-l-4 border-violet-600">
  <strong>Pregunta:</strong> ¿qué operaciones tuvo que realizar el algoritmo para producir este resultado?
</div>

<div class="mt-4 text-sm text-slate-600">Estudiaremos las estrategias de ordenamiento, aunque en la práctica Python ofrece herramientas optimizadas como <code>sort()</code>.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · ESTRATEGIAS</div>

# Un resultado, diferentes procedimientos

<div class="font-mono text-lg bg-slate-900 text-white rounded-xl p-4 mt-5 text-center">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="grid grid-cols-2 gap-5 mt-7">
  <div class="p-5 bg-blue-50 rounded-xl border border-blue-200">
    <h3 class="font-bold">Comparar vecinos</h3>
    <p class="mt-2">54 &gt; 26 → intercambiar.</p>
    <div class="font-mono mt-3 text-sm">[26, 54, 93, 17, 77, 31, 44, 55, 20]</div>
  </div>
  <div class="p-5 bg-violet-50 rounded-xl border border-violet-200">
    <h3 class="font-bold">Seleccionar el mínimo</h3>
    <p class="mt-2">El menor es 17 → llevarlo al inicio.</p>
    <div class="font-mono mt-3 text-sm">[17, 26, 93, 54, 77, 31, 44, 55, 20]</div>
  </div>
</div>

<div class="mt-6 p-4 bg-amber-50 rounded-xl">Ambas estrategias avanzan hacia el mismo resultado, pero no ejecutan las mismas operaciones.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · OPERACIONES</div>

# Comparaciones y movimientos

<div class="grid grid-cols-2 gap-5 mt-7">
  <div class="p-5 rounded-xl bg-blue-50 border border-blue-200">
    <h3 class="text-xl font-bold text-blue-800">Comparación</h3>
    <p class="mt-3">Determina el orden relativo de dos elementos.</p>
    <div class="font-mono mt-4 text-lg">54 &gt; 26</div>
    <p class="mt-3 text-sm">Comparar no modifica necesariamente la lista.</p>
  </div>
  <div class="p-5 rounded-xl bg-violet-50 border border-violet-200">
    <h3 class="text-xl font-bold text-violet-800">Intercambio</h3>
    <p class="mt-3">Cambia de posición dos elementos.</p>
    <div class="font-mono mt-4 text-lg">[54, 26] → [26, 54]</div>
    <p class="mt-3 text-sm">Otros algoritmos desplazan elementos o los copian.</p>
  </div>
</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · OPERACIONES EN PYTHON</div>

# Comparar e intercambiar

```python
numeros = [54, 26, 93, 17, 77, 31, 44, 55, 20]

if numeros[0] > numeros[1]:
    numeros[0], numeros[1] = numeros[1], numeros[0]

print(numeros)
```

<div class="mt-5 bg-emerald-50 border border-emerald-200 p-4 rounded-xl font-mono">[26, 54, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="mt-6 p-4 bg-slate-100 rounded-xl">En este fragmento: <strong>1 comparación</strong> y <strong>1 intercambio</strong>. Todavía no hemos ordenado toda la lista.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · COMPLEJIDAD</div>

# ¿Qué pasa cuando aumenta n?

<div class="mt-6 p-5 bg-violet-50 rounded-xl border-l-4 border-violet-600">
  La <strong>complejidad algorítmica</strong> describe cómo crecen los recursos necesarios conforme aumenta el tamaño de entrada <strong>n</strong>.
</div>

<div class="grid grid-cols-2 gap-5 mt-7">
  <div class="p-5 bg-blue-50 border border-blue-200 rounded-xl">
    <h3 class="font-bold text-xl">Tiempo</h3>
    <p class="mt-3">Comparaciones, movimientos y recorridos que requiere el algoritmo.</p>
  </div>
  <div class="p-5 bg-emerald-50 border border-emerald-200 rounded-xl">
    <h3 class="font-bold text-xl">Espacio</h3>
    <p class="mt-3">Memoria adicional utilizada durante el ordenamiento.</p>
  </div>
</div>

<div class="mt-6 text-slate-600">Un algoritmo puede reorganizar la lista original; otro puede necesitar listas auxiliares.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · CRITERIOS DE ANÁLISIS</div>

# ¿Cómo estudiaremos cada algoritmo?

| Aspecto | Pregunta guía |
|---|---|
| Estrategia | ¿Qué idea utiliza para ordenar? |
| Funcionamiento | ¿Qué ocurre en cada paso? |
| Comparaciones y movimientos | ¿Cómo reorganiza los elementos? |
| Tiempo | ¿Cómo crece el trabajo al aumentar n? |
| Espacio | ¿Cuánta memoria adicional requiere? |
| Implementación | ¿Cómo se programa en Python? |

<div class="mt-5 p-4 rounded-xl bg-amber-50 border-l-4 border-amber-500">La cantidad de operaciones depende del algoritmo y, en algunos casos, del orden inicial de los datos.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · SEIS ALGORITMOS</div>

# Mismo problema, seis estrategias

<div class="mt-5 font-mono text-base bg-slate-900 text-white rounded-xl p-4 text-center">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="grid grid-cols-3 gap-4 mt-7">
  <div class="p-4 bg-violet-50 border rounded-xl"><strong>Bubble Sort</strong><p class="mt-2 text-sm">Comparar vecinos.</p></div>
  <div class="p-4 bg-violet-50 border rounded-xl"><strong>Selection Sort</strong><p class="mt-2 text-sm">Elegir el mínimo.</p></div>
  <div class="p-4 bg-violet-50 border rounded-xl"><strong>Insertion Sort</strong><p class="mt-2 text-sm">Insertar en orden.</p></div>
  <div class="p-4 bg-blue-50 border rounded-xl"><strong>Shell Sort</strong><p class="mt-2 text-sm">Ordenar por intervalos.</p></div>
  <div class="p-4 bg-blue-50 border rounded-xl"><strong>Merge Sort</strong><p class="mt-2 text-sm">Dividir y mezclar.</p></div>
  <div class="p-4 bg-blue-50 border rounded-xl"><strong>Quick Sort</strong><p class="mt-2 text-sm">Particionar con pivote.</p></div>
</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · BUBBLE SORT</div>

# Burbuja: comparar vecinos

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> comparar elementos consecutivos e intercambiarlos si están fuera de orden.</div>

<div class="mt-7 space-y-4 font-mono text-lg">
  <div class="p-3 bg-slate-100 rounded-lg">[<span class="text-rose-600 font-bold">54, 26</span>, 93, 17, 77, 31, 44, 55, 20]</div>
  <div class="text-center text-violet-700">54 &gt; 26 → intercambio</div>
  <div class="p-3 bg-emerald-50 rounded-lg">[<span class="text-emerald-700 font-bold">26, 54</span>, 93, 17, 77, 31, 44, 55, 20]</div>
</div>

<div class="mt-7 text-slate-600">Al completar un recorrido, el mayor elemento de la zona aún no ordenada queda al final de esa zona.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · SELECTION SORT</div>

# Selección: elegir el mínimo

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> buscar el menor elemento de la parte pendiente y colocarlo en su posición definitiva.</div>

<div class="mt-7 space-y-4 font-mono text-lg">
  <div class="p-3 bg-slate-100 rounded-lg">[54, 26, 93, <span class="text-rose-600 font-bold">17</span>, 77, 31, 44, 55, 20]</div>
  <div class="text-center text-violet-700">Mínimo = 17 → intercambiar con 54</div>
  <div class="p-3 bg-emerald-50 rounded-lg">[<span class="text-emerald-700 font-bold">17</span>, 26, 93, 54, 77, 31, 44, 55, 20]</div>
</div>

<div class="mt-7 text-slate-600">La zona ordenada crece una posición en cada iteración.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · INSERTION SORT</div>

# Inserción: ampliar la zona ordenada

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> tomar un elemento e insertarlo donde corresponde dentro de la zona ya ordenada.</div>

<div class="mt-7 space-y-3 font-mono text-lg">
  <div class="p-3 bg-slate-100 rounded-lg"><span class="text-violet-700 font-bold">[54]</span> | [26, 93, 17, 77, 31, 44, 55, 20]</div>
  <div class="text-center text-violet-700">Insertar 26 antes de 54</div>
  <div class="p-3 bg-emerald-50 rounded-lg"><span class="text-emerald-700 font-bold">[26, 54]</span> | [93, 17, 77, 31, 44, 55, 20]</div>
  <div class="text-center text-violet-700">Insertar 93</div>
  <div class="p-3 bg-emerald-50 rounded-lg"><span class="text-emerald-700 font-bold">[26, 54, 93]</span> | [17, 77, 31, 44, 55, 20]</div>
</div>

<div class="mt-5 text-slate-600">La parte izquierda permanece ordenada en cada paso.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · SHELL SORT</div>

# Shell: ordenar por intervalos

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> aplicar inserción sobre elementos separados por una distancia (<em>gap</em>) y reducirla progresivamente.</div>

<div class="mt-7 p-4 bg-slate-100 rounded-xl font-mono text-lg">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="grid grid-cols-2 gap-5 mt-6">
  <div class="p-5 bg-blue-50 border border-blue-200 rounded-xl">
    <strong>Ejemplo: gap = 4</strong>
    <p class="mt-3 font-mono">Índices: 0, 4, 8</p>
    <p class="font-mono">Valores: 54, 77, 20</p>
  </div>
  <div class="p-5 bg-emerald-50 border border-emerald-200 rounded-xl">
    <strong>Grupo ordenado</strong>
    <p class="mt-3 font-mono">20, 54, 77</p>
    <p class="mt-2 text-sm">También se ordenan los demás grupos.</p>
  </div>
</div>

<div class="mt-6 text-slate-600">Al llegar a <code>gap = 1</code>, se completa el ordenamiento por inserción.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · MERGE SORT</div>

# Mezcla: dividir y combinar

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> dividir la lista hasta obtener partes mínimas y combinarlas en orden.</div>

<div class="mt-7 space-y-4 text-center font-mono text-lg">
  <div class="p-3 bg-slate-100 rounded-lg">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>
  <div class="text-violet-700">↓ dividir</div>
  <div class="grid grid-cols-2 gap-4">
    <div class="p-3 bg-blue-50 rounded-lg">[54, 26, 93, 17]</div>
    <div class="p-3 bg-blue-50 rounded-lg">[77, 31, 44, 55, 20]</div>
  </div>
  <div class="text-violet-700">↓ seguir dividiendo y mezclar ordenadamente</div>
  <div class="p-3 bg-emerald-50 rounded-lg">[54] + [26] → [26, 54]</div>
</div>

<div class="mt-5 text-slate-600">Estrategia: <strong>divide y vencerás</strong>. La mezcla combina subsecuencias ya ordenadas.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · QUICK SORT</div>

# Rápido: particionar con un pivote

<div class="mt-5 p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Idea clave:</strong> elegir un pivote, separar los valores menores y mayores y ordenar las partes resultantes.</div>

<div class="mt-7 p-3 bg-slate-100 rounded-lg text-center font-mono text-lg">[54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="mt-5 text-center font-bold text-violet-700">Ejemplo: pivote = 54</div>

<div class="grid grid-cols-3 gap-3 mt-5 text-center">
  <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl"><strong>Menores</strong><div class="font-mono text-sm mt-3">[26, 17, 31, 44, 20]</div></div>
  <div class="p-4 bg-violet-100 border border-violet-200 rounded-xl"><strong>Pivote</strong><div class="font-mono text-2xl mt-3">54</div></div>
  <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl"><strong>Mayores</strong><div class="font-mono text-sm mt-3">[93, 77, 55]</div></div>
</div>

<div class="mt-6 text-slate-600">La separación es conceptual; algunas implementaciones particionan directamente en la lista original.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · COMPARACIÓN</div>

# Seis formas de abordar el mismo problema

| Algoritmo | Estrategia central |
|---|---|
| **Bubble Sort** | Comparar e intercambiar vecinos. |
| **Selection Sort** | Seleccionar el mínimo restante. |
| **Insertion Sort** | Insertar en una sección ordenada. |
| **Shell Sort** | Aplicar inserción con intervalos decrecientes. |
| **Merge Sort** | Dividir y mezclar partes ordenadas. |
| **Quick Sort** | Particionar alrededor de un pivote. |

<div class="mt-5 p-4 bg-amber-50 border-l-4 border-amber-500 rounded-xl">Una estrategia más elaborada no es necesariamente mejor en todos los casos: analizaremos su costo y sus condiciones de uso.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · EXPOSICIONES</div>

# ¿Cómo presentará cada equipo su algoritmo?

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>1. ¿Qué es?</strong><p class="mt-2 text-sm">Definición e idea clave.</p></div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>2. ¿Cómo funciona?</strong><p class="mt-2 text-sm">Explicación visual paso a paso.</p></div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>3. ¿Cómo se implementa?</strong><p class="mt-2 text-sm">Código Python y ejecución.</p></div>
  <div class="p-4 bg-slate-50 border rounded-xl"><strong>4. ¿Qué costo tiene?</strong><p class="mt-2 text-sm">Complejidad temporal y espacial.</p></div>
</div>

<div class="mt-6 bg-slate-900 text-white rounded-xl p-4 text-center font-mono">numeros = [54, 26, 93, 17, 77, 31, 44, 55, 20]</div>

<div class="mt-4 text-sm text-slate-600">Todos los equipos utilizan la misma entrada para facilitar la comparación entre algoritmos.</div>

---

<div class="text-violet-700 font-bold text-sm tracking-widest">3.1 · CIERRE</div>

# ¿Qué aprendimos?

<div class="space-y-4 mt-8">
  <div class="p-4 bg-violet-50 border-l-4 border-violet-600 rounded-xl"><strong>Ordenar</strong> significa reorganizar datos según un criterio.</div>
  <div class="p-4 bg-blue-50 border-l-4 border-blue-600 rounded-xl"><strong>La estrategia</strong> determina cómo se consigue ese orden.</div>
  <div class="p-4 bg-emerald-50 border-l-4 border-emerald-600 rounded-xl"><strong>La eficiencia</strong> depende del trabajo y la memoria que requiere cada algoritmo.</div>
</div>

<div class="mt-8 p-5 bg-slate-900 text-white rounded-xl text-center text-xl font-bold">Si todos llegan al mismo resultado, ¿cuál lo consigue con menor costo?</div>

<div class="mt-6 text-xs text-slate-500">Referencia: Runestone Academy · Problem Solving with Algorithms and Data Structures using Python · Sorting.</div>
