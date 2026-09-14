---
background: /background3.jpg
title: Algoritmia y Estructura de Datos
transition: slide-left
---

# Ejercicio integrador · Análisis guiado

Analizaremos paso a paso el siguiente algoritmo:

```text
contador = 0

para i = 0 hasta n - 1:
    para j = 0 hasta n - 1:
        contador = contador + 1
```

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-bold text-amber-300">Objetivo</div>

<p class="!text-white mt-1">
Determinar su <strong>complejidad temporal</strong> y su <strong>complejidad espacial auxiliar</strong>, justificando cada resultado.
</p>

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
<strong class="text-blue-800">⏱️ Tiempo</strong><br>
¿Cuántas veces se ejecuta el trabajo?
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
<strong class="text-violet-800">💾 Espacio</strong><br>
¿Cuánta memoria adicional se utiliza?
</div>

</div>

---

# Paso 1 · Identificar qué representa `n`

Observemos los límites de ambos ciclos:

```text
para i = 0 hasta n - 1
para j = 0 hasta n - 1
```

Cada variable recorre los valores:

```text
0, 1, 2, ..., n - 1
```

<div class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">¿Qué nos indica esto?</div>

Cada ciclo realiza exactamente <strong>n iteraciones</strong>.

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

En este algoritmo, `n` representa el <strong>número de posiciones que recorre cada ciclo</strong>.

</div>

<div class="mt-4 text-center font-semibold text-slate-700">

Primera conclusión: <span class="font-mono text-blue-800">ciclo exterior = n</span> y <span class="font-mono text-violet-800">ciclo interior = n</span>.

</div>

---

# Paso 2 · Analizar el ciclo exterior

Primero observemos únicamente el ciclo controlado por `i`:

```text
para i = 0 hasta n - 1:
    ...
```

Si `n = 4`, los valores de `i` serían:

```text
i = 0
i = 1
i = 2
i = 3
```

<div class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

<div class="font-mono font-bold text-xl text-blue-800">
El ciclo exterior se ejecuta n veces.
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-100 border border-slate-200">

Pero todavía no conocemos el trabajo total, porque <strong>dentro de cada una de esas iteraciones</strong> existe otro ciclo.

</div>

---

# Paso 3 · Analizar el ciclo interior

Ahora observemos:

```text
para j = 0 hasta n - 1:
    contador = contador + 1
```

Para cada valor de `i`, el ciclo controlado por `j` recorre nuevamente:

```text
0, 1, 2, ..., n - 1
```

<div class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

<div class="font-mono font-bold text-xl text-violet-800">
El ciclo interior se ejecuta n veces por cada iteración del ciclo exterior.
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

La instrucción:

<div class="font-mono font-bold text-xl mt-1">contador = contador + 1</div>

se ejecuta una vez en cada iteración del ciclo interior.

</div>

---

# Paso 4 · Contar cuántas veces se ejecuta la suma

Tenemos:

<div class="grid grid-cols-3 gap-4 mt-4 items-center">

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

<div class="font-bold text-blue-800">Ciclo exterior</div>

<div class="font-mono font-bold text-2xl mt-2">n</div>

</div>

<div class="text-center text-3xl font-bold text-amber-600">×</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

<div class="font-bold text-violet-800">Ciclo interior</div>

<div class="font-mono font-bold text-2xl mt-2">n</div>

</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-mono font-bold text-2xl text-amber-800">
n × n = n²
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
La instrucción <span class="font-mono text-amber-300">contador = contador + 1</span>
se ejecuta <strong class="text-amber-300">n² veces</strong>.
</p>

</div>

---

# Paso 5 · Comprobarlo con un ejemplo pequeño

Supongamos:

<div class="text-center font-mono font-bold text-2xl mt-2">n = 3</div>

Entonces:

```text
i = 0 → j = 0, 1, 2 → 3 ejecuciones
i = 1 → j = 0, 1, 2 → 3 ejecuciones
i = 2 → j = 0, 1, 2 → 3 ejecuciones
```

<div class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

<div class="font-mono font-bold text-xl text-blue-800">
3 × 3 = 9 ejecuciones
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

Y como:

<div class="font-mono font-bold text-xl mt-1">n² = 3² = 9</div>

el conteo coincide.

</div>

<div class="mt-3 text-center font-semibold text-slate-700">

El ejemplo numérico confirma el patrón general: <span class="font-mono">n × n = n²</span>.

</div>

---

# Paso 6 · Obtener la complejidad temporal

La operación dominante es:

```text
contador = contador + 1
```

y acabamos de determinar que se ejecuta:

<div class="text-center font-mono font-bold text-2xl mt-3">n² veces</div>

Si cada ejecución tiene costo constante:

<div class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

<div class="font-mono font-bold text-xl text-blue-800">
T(n) ≈ c · n² + k
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-mono font-bold text-2xl text-amber-300">
Complejidad temporal: O(n²)
</div>

</div>

<div class="mt-3 text-center font-semibold text-slate-700">

El algoritmo tiene crecimiento <strong>cuadrático</strong>.

</div>

---

# Paso 7 · Identificar la memoria utilizada

Ahora analizamos el espacio.

El algoritmo utiliza:

```text
contador
i
j
```

<div class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200">

<div class="card-title text-violet-800">Pregunta clave</div>

¿La cantidad de variables utilizadas aumenta cuando aumenta `n`?

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-100 border border-slate-200 text-center">

No. Aunque los ciclos se ejecuten más veces, seguimos utilizando las mismas tres variables.

</div>

<div class="mt-4 text-center font-semibold">

`contador`, `i` y `j` ocupan una cantidad fija de memoria.

</div>

---

# Paso 8 · Obtener la complejidad espacial

La memoria auxiliar no depende del tamaño `n`.

<div class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

Si `n = 10`, usamos:

<div class="font-mono font-bold text-xl mt-1">contador · i · j</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

Si `n = 1 000 000`, seguimos usando:

<div class="font-mono font-bold text-xl mt-1">contador · i · j</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-mono font-bold text-2xl text-amber-300">
Espacio auxiliar: O(1)
</div>

<p class="!text-white mt-1">
La memoria adicional permanece <strong>constante</strong>.
</p>

</div>

---

# Paso 9 · Integrar ambos resultados

Ya podemos describir el algoritmo en sus dos dimensiones.

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="p-4 rounded-xl bg-blue-50 border border-blue-200 text-center">

<div class="font-bold text-blue-800">⏱️ Complejidad temporal</div>

<div class="font-mono font-bold text-3xl mt-3 text-blue-800">O(n²)</div>

<p class="mt-2">La operación principal se ejecuta n² veces.</p>

</div>

<div class="p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">

<div class="font-bold text-violet-800">💾 Espacio auxiliar</div>

<div class="font-mono font-bold text-3xl mt-3 text-violet-800">O(1)</div>

<p class="mt-2">La cantidad de memoria adicional no crece con n.</p>

</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
El algoritmo realiza <strong class="text-amber-300">más trabajo</strong> conforme crece la entrada,
pero no requiere <strong class="text-amber-300">más memoria auxiliar</strong>.
</p>

</div>

---

# Paso 10 · Respuesta completa

<div class="mt-2 p-3 rounded-xl bg-slate-50 border border-slate-200">

<strong class="text-slate-800">1. ¿Qué representa `n`?</strong><br>
El número de posiciones que recorre cada ciclo.

</div>

<div class="mt-2 p-3 rounded-xl bg-blue-50 border border-blue-200">

<strong class="text-blue-800">2. ¿Cuántas veces se ejecuta la suma?</strong><br>
`n × n = n²` veces.

</div>

<div class="mt-2 p-3 rounded-xl bg-blue-50 border border-blue-200">

<strong class="text-blue-800">3. ¿Cuál es la complejidad temporal?</strong><br>
`O(n²)`, porque el trabajo dominante crece cuadráticamente.

</div>

<div class="mt-2 p-3 rounded-xl bg-violet-50 border border-violet-200">

<strong class="text-violet-800">4. ¿La memoria auxiliar aumenta con `n`?</strong><br>
No. El algoritmo siempre utiliza las mismas variables auxiliares.

</div>

<div class="mt-2 p-3 rounded-xl bg-violet-50 border border-violet-200">

<strong class="text-violet-800">5. ¿Cuál es la complejidad espacial auxiliar?</strong><br>
`O(1)`, porque la memoria adicional permanece constante.

</div>

---

# Método que acabamos de aplicar

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<strong>1.</strong> Identificar qué representa `n`.
</div>

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<strong>2.</strong> Localizar las operaciones que dependen de `n`.
</div>

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
<strong>3.</strong> Determinar cuántas veces se ejecutan.
</div>

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
<strong>4.</strong> Obtener el orden de crecimiento temporal.
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200">
<strong>5.</strong> Identificar la memoria adicional utilizada.
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200">
<strong>6.</strong> Determinar cómo crece esa memoria con `n`.
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-bold text-amber-300">Resultado del ejercicio</div>

<div class="font-mono font-bold text-xl !text-white mt-1">
Tiempo: O(n²) &nbsp;&nbsp; | &nbsp;&nbsp; Espacio auxiliar: O(1)
</div>

</div>
