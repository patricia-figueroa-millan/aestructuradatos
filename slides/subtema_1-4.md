---
background: /background3.jpg
title: Algoritmia y Estructura de Datos
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<div class="flex flex-col items-center gap-1 mb-5">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400 bg-amber-400/10 px-3 py-1 rounded-full border border-amber-400/20">Instituto Tecnológico de Colima</span>
<span class="text-sm text-slate-300 font-medium">Ingeniería en Inteligencia Artificial</span>
</div>
<h1 class="text-4xl font-black tracking-tight bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent !leading-tight mb-2">Algoritmia y Estructura de Datos</h1>
<div class="mt-3 mb-5">
<div class="text-xl font-semibold text-amber-300 tracking-tight">1.4 Notación Big O y su importancia en la eficiencia de algoritmos</div>
</div>
<div class="mt-6 pt-5 border-t border-white/10 flex flex-col items-center gap-1">
<span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-400">Catedrática</span>
<div class="text-lg font-bold text-white mb-3">Dra. Patricia Elizabeth Figueroa Millán</div>
</div>
</div>

---

# ¿Qué es Big O?

<div class="mt-3 text-center">
<p>Ya sabemos que el costo de un algoritmo puede expresarse mediante una función del tamaño de la entrada:</p>
<div class="mt-3 inline-block font-mono text-3xl font-bold text-violet-800 bg-violet-50 border border-violet-200 rounded-xl px-6 py-3">T(n)</div>
</div>

<div class="grid grid-cols-3 gap-4 mt-5 items-center">
<div class="card bg-slate-100 border border-slate-200 text-center">
<div class="card-title text-slate-800">Costo detallado</div>
<div class="font-mono text-2xl font-bold my-3">2n + 3</div>
<p>Describe las operaciones consideradas.</p>
</div>
<div class="text-center">
<div class="text-4xl font-bold text-amber-600">→</div>
<div class="mt-2 font-semibold text-slate-600">abstraemos</div>
</div>
<div class="card bg-amber-50 border border-amber-200 text-center">
<div class="card-title text-amber-800">Orden de crecimiento</div>
<div class="font-mono text-2xl font-bold my-3 text-amber-800">O(n)</div>
<p>Describe cómo escala el costo cuando n crece.</p>
</div>
</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">Big O nos proporciona una forma compacta de expresar una <strong class="text-amber-300">cota superior del crecimiento asintótico.</strong></p>
</div>

# Definición e interpretación de Big O

<div class="mt-3 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">

<p class="text-lg">
<strong>Big O</strong> es una notación que utilizamos para describir
<strong>cómo crece el costo de un algoritmo</strong> a medida que aumenta
el tamaño de la entrada <strong>n</strong>.
</p>

</div>

<div class="mt-5 text-center">

<div class="inline-block bg-slate-900 rounded-xl px-8 py-4">

<div class="text-sm text-slate-300">Nos interesa observar</div>

<div class="mt-2 font-mono text-2xl font-bold text-white">
n aumenta → ¿cómo crece T(n)?
</div>

</div>

</div>

<div class="grid grid-cols-3 gap-4 mt-5">

<div class="card bg-blue-50 border border-blue-200 text-center">

<div class="font-bold text-xl text-blue-800">Tamaño de entrada</div>

<div class="mt-3 font-mono text-2xl font-bold">n</div>

<p class="mt-2">
Cantidad de datos que debe procesar el algoritmo.
</p>

</div>

<div class="card bg-violet-50 border border-violet-200 text-center">

<div class="font-bold text-xl text-violet-800">Costo</div>

<div class="mt-3 font-mono text-2xl font-bold">T(n)</div>

<p class="mt-2">
Representa las operaciones realizadas para un tamaño de entrada n.
</p>

</div>

<div class="card bg-amber-50 border border-amber-200 text-center">

<div class="font-bold text-xl text-amber-800">Orden de crecimiento</div>

<div class="mt-3 font-mono text-2xl font-bold">O( · )</div>

<p class="mt-2">
Describe la tendencia de crecimiento del costo cuando n aumenta.
</p>

</div>

</div>

<div class="mt-4 text-center font-semibold text-slate-700">
Big O se enfoca en la <span class="text-violet-700">tendencia de crecimiento</span>,
no en el número exacto de operaciones.
</div>


---

# Jerarquía de complejidades comunes

<div class="mt-2 text-center">
<p>Las clases Big O permiten comparar qué tan rápido crece el costo de distintos algoritmos.</p>
</div>

<div class="mt-5 flex justify-center">
<div class="inline-flex items-center gap-2 font-mono font-bold">
<span class="bg-emerald-50 border border-emerald-200 px-3 py-2 rounded-lg">O(1)</span>
<span>→</span>
<span class="bg-emerald-50 border border-emerald-200 px-3 py-2 rounded-lg">O(log n)</span>
<span>→</span>
<span class="bg-blue-50 border border-blue-200 px-3 py-2 rounded-lg">O(n)</span>
<span>→</span>
<span class="bg-blue-50 border border-blue-200 px-3 py-2 rounded-lg">O(n log n)</span>
<span>→</span>
<span class="bg-amber-50 border border-amber-200 px-3 py-2 rounded-lg">O(n²)</span>
<span>→</span>
<span class="bg-red-50 border border-red-200 px-3 py-2 rounded-lg">O(2ⁿ)</span>
<span>→</span>
<span class="bg-red-50 border border-red-200 px-3 py-2 rounded-lg">O(n!)</span>
</div>
</div>

<div class="mt-6 grid grid-cols-2 gap-4">
<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">Crecimiento lento o moderado</div>
<p>O(1), O(log n) y O(n) suelen escalar favorablemente frente a entradas grandes.</p>
</div>
<div class="card bg-red-50 border border-red-200">
<div class="card-title text-red-800">Crecimiento rápido</div>
<p>O(n²), O(2ⁿ) y O(n!) pueden aumentar rápidamente el costo.</p>
</div>
</div>

---

# Complejidades de crecimiento bajo o moderado

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">O(1) · Constante</div>
<p>El número de operaciones no crece con n.</p>
<div class="mt-3 bg-white border border-emerald-200 rounded-lg p-2 text-center font-mono">A[5]</div>
<div class="mt-2 text-center font-semibold">Acceso directo a un arreglo</div>
</div>

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">O(log n) · Logarítmica</div>
<p>El problema se reduce por un factor constante en cada paso.</p>
<div class="mt-3 bg-white border border-emerald-200 rounded-lg p-2 text-center font-mono">1024 → 512 → 256 → ...</div>
<div class="mt-2 text-center font-semibold">Búsqueda binaria</div>
</div>

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">O(n) · Lineal</div>
<p>El trabajo crece aproximadamente en proporción a n.</p>
<div class="mt-3 bg-white border border-blue-200 rounded-lg p-2 text-center font-mono">1 recorrido → n elementos</div>
<div class="mt-2 text-center font-semibold">Búsqueda secuencial</div>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">En O(log n), por ejemplo, una entrada de 1,024 elementos puede reducirse a 1 en aproximadamente <strong class="text-amber-300">10 pasos</strong>.</p>
</div>

---

# Complejidades de mayor crecimiento

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">O(n log n) · Lineal-logarítmica</div>
<p>Común en algoritmos eficientes de ordenamiento por comparación.</p>
<div class="mt-2 text-center font-semibold">Ejemplo: Merge Sort</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">O(n²) · Cuadrática</div>
<p>Frecuente cuando el trabajo depende de dos recorridos de tamaño n.</p>
<div class="mt-2 text-center font-semibold">Ejemplo: Bubble Sort</div>
</div>

<div class="card bg-red-50 border border-red-200">
<div class="card-title text-red-800">O(2ⁿ) · Exponencial</div>
<p>El costo puede duplicarse al aumentar n una unidad.</p>
<div class="mt-2 text-center font-mono font-bold">2²⁰ = 1,048,576</div>
</div>

<div class="card bg-red-50 border border-red-200">
<div class="card-title text-red-800">O(n!) · Factorial</div>
<p>Puede aparecer al explorar todas las permutaciones posibles.</p>
<div class="mt-2 text-center font-mono font-bold">10! = 3,628,800</div>
</div>

</div>

<div class="mt-4 text-center font-semibold text-red-800">Los órdenes exponencial y factorial se vuelven costosos muy rápidamente.</div>

---

# ¿Qué tan grande es la diferencia?

<div class="mt-2 text-center">
<p>Comparemos el número aproximado de operaciones para <strong>n = 1,000</strong>.</p>
</div>

<table class="w-full text-center border-collapse mt-4">
<thead>
<tr class="bg-slate-900 text-white">
<th class="p-2">Complejidad</th>
<th class="p-2">Operaciones aproximadas</th>
<th class="p-2">Crecimiento</th>
</tr>
</thead>
<tbody>
<tr><td class="p-2 border font-mono font-bold">O(1)</td><td class="p-2 border">1</td><td class="p-2 border">Constante</td></tr>
<tr><td class="p-2 border font-mono font-bold">O(log₂ n)</td><td class="p-2 border">≈ 10</td><td class="p-2 border">Logarítmico</td></tr>
<tr><td class="p-2 border font-mono font-bold">O(n)</td><td class="p-2 border">1,000</td><td class="p-2 border">Lineal</td></tr>
<tr><td class="p-2 border font-mono font-bold">O(n log₂ n)</td><td class="p-2 border">≈ 10,000</td><td class="p-2 border">Lineal-logarítmico</td></tr>
<tr><td class="p-2 border font-mono font-bold">O(n²)</td><td class="p-2 border">1,000,000</td><td class="p-2 border">Cuadrático</td></tr>
</tbody>
</table>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
<p>Una diferencia aparentemente pequeña en el orden de crecimiento puede convertirse en una <strong>diferencia enorme</strong> cuando aumenta n.</p>
</div>

---

# Reglas para simplificar Big O

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">1. Ignorar factores constantes</div>
<div class="mt-3 text-center font-mono text-xl font-bold">2n → O(n)</div>
<div class="mt-3 text-center font-mono text-xl font-bold">½n² → O(n²)</div>
<p class="mt-3">La constante afecta el costo real, pero no cambia el orden de crecimiento.</p>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">2. Conservar el término dominante</div>
<div class="mt-3 text-center font-mono text-xl font-bold">n² + 100n + 500</div>
<div class="mt-2 text-center text-2xl font-bold text-violet-700">↓</div>
<div class="text-center font-mono text-xl font-bold">O(n²)</div>
<p class="mt-3">El término de mayor orden domina cuando n crece.</p>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">Primero identifica <strong class="text-amber-300">qué término crece más rápido</strong>; después elimina su factor constante.</p>
</div>

---

# Big O no significa necesariamente peor caso

<div class="mt-3 p-3 rounded-xl bg-red-50 border border-red-200 text-center">
<p>Big O y peor caso son conceptos relacionados, pero <strong>no son equivalentes</strong>.</p>
</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">Big O</div>
<p>Es una <strong>notación matemática</strong> que describe una cota superior del crecimiento de una función.</p>
<div class="mt-3 text-center font-mono font-bold text-violet-800">T(n) ∈ O(g(n))</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">Peor caso</div>
<p>Es un <strong>escenario de análisis</strong>: considera la entrada de tamaño n que produce el mayor costo.</p>
<div class="mt-3 text-center font-semibold text-amber-800">máximo costo para tamaño n</div>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">Big O puede expresar el crecimiento del <strong class="text-amber-300">peor caso, caso promedio u otra función de costo</strong>, siempre indicando qué estamos analizando.</p>
</div>

---

# ¿Por qué Big O es importante?

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">⚙️ Independencia del hardware</div>
<p>Permite analizar el crecimiento sin depender de una computadora específica.</p>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">⚖️ Comparación</div>
<p>Permite comparar alternativas según cómo aumenta su costo.</p>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">📈 Escalabilidad</div>
<p>Ayuda a anticipar si una solución seguirá siendo viable al crecer los datos.</p>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="text-xl font-semibold text-amber-300">El algoritmo también es tecnología</div>
<p class="!text-white mt-2">Mejorar el orden de crecimiento puede producir una ganancia mayor que simplemente ejecutar el mismo algoritmo en hardware más rápido.</p>
</div>

---

# En resumen · Big O

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">¿Qué representa?</div>
<p>Una <strong>cota superior asintótica</strong> del crecimiento de una función.</p>
</div>

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">¿Cómo se simplifica?</div>
<p>Ignoramos factores constantes y conservamos el término dominante.</p>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">¿Qué clases usamos?</div>
<p>O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) y O(n!).</p>
</div>

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">¿Para qué sirve?</div>
<p>Para comparar algoritmos y anticipar su <strong>escalabilidad</strong>.</p>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="text-xl font-semibold text-amber-300">Pregunta clave</div>
<p class="!text-white mt-2">¿Qué ocurrirá con el costo de este algoritmo cuando el tamaño del problema crezca?</p>
</div>
