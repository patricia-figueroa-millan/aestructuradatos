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
<div class="text-xl font-semibold text-amber-300 tracking-tight">1.3 Análisis de la eficiencia de los algoritmos: tiempo y espacio</div>
</div>
<div class="mt-6 pt-5 border-t border-white/10 flex flex-col items-center gap-1">
<span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-400">Catedrática</span>
<div class="text-lg font-bold text-white mb-3">Dra. Patricia Elizabeth Figueroa Millán</div>
</div>
</div>

---

# De la complejidad al análisis de algoritmos

<div class="mt-3 text-center">
<p>En el tema anterior aprendimos a describir el costo mediante <strong>T(n)</strong> y a estudiar cómo cambia cuando aumenta el tamaño de la entrada.</p>
<div class="mt-2 text-xl font-semibold text-amber-700">Ahora utilizaremos esas ideas para analizar algoritmos concretos.</div>
</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">⏱️ Tiempo</div>
<p>Analizamos <strong>cuántas veces se ejecutan las operaciones</strong> relevantes conforme crece la entrada.</p>
<div class="mt-3 text-center font-mono font-bold text-blue-800">T(n)</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">💾 Espacio</div>
<p>Analizamos <strong>cuánta memoria necesita</strong> el algoritmo durante su ejecución conforme crece la entrada.</p>
<div class="mt-3 text-center font-mono font-bold text-violet-800">S(n)</div>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">La pregunta ya no es qué significa complejidad, sino <strong class="text-amber-300">cómo determinarla a partir de un algoritmo.</strong></p>
</div>

---

# ¿Cómo analizamos el tiempo?

Consideremos un algoritmo que suma los elementos de un arreglo:

```text
suma = 0

para i = 0 hasta n - 1:
    suma = suma + A[i]
```

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">¿Qué depende de n?</div>
<p>El cuerpo del ciclo se ejecuta una vez por cada elemento del arreglo.</p>
<div class="mt-3 text-center font-mono font-bold text-xl">n iteraciones</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">Trabajo por iteración</div>
<p>En cada iteración se realiza una cantidad constante de operaciones.</p>
<div class="mt-3 text-center font-mono font-bold text-xl">c operaciones</div>
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-xl text-amber-300">T(n) ≈ c · n + k → O(n)</div>
<p class="!text-white mt-2">Un recorrido completo de n elementos tiene crecimiento <strong>lineal</strong>.</p>
</div>

---

# Dos ciclos anidados

```text
para i = 0 hasta n - 1:
    para j = 0 hasta n - 1:
        procesar A[i], A[j]
```

<div class="grid grid-cols-3 gap-4 mt-4 items-center">

<div class="card bg-blue-50 border border-blue-200 text-center">
<div class="card-title text-blue-800">Ciclo exterior</div>
<div class="font-mono text-2xl font-bold my-2">n</div>
<p>iteraciones</p>
</div>

<div class="text-center">
<div class="text-3xl font-bold text-amber-600">×</div>
</div>

<div class="card bg-violet-50 border border-violet-200 text-center">
<div class="card-title text-violet-800">Ciclo interior</div>
<div class="font-mono text-2xl font-bold my-2">n</div>
<p>por cada iteración exterior</p>
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
<div class="font-mono font-bold text-2xl">n × n = n² → O(n²)</div>
</div>

<div class="mt-4 text-center font-semibold text-slate-700">
Si n se duplica, un trabajo cuadrático puede crecer aproximadamente <span class="text-amber-700">cuatro veces</span>.
</div>

---
background: /background3.jpg
title: Algoritmia y Estructura de Datos
transition: slide-left
---

# No basta con contar ciclos

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

Consideremos:

```text
i = 1

mientras i < n:
    i = i * 2
```

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200 mt-2">

<div class="card-title text-blue-800">¿Qué ocurre?</div>

`i = i * 2` hace que `i` se <strong>duplique</strong> en cada iteración.

</div>

</div>

<div class="card bg-slate-50 border border-slate-200">

<div class="card-title text-slate-800">Evolución de `i`</div>

| Iteraciones | Valor de `i` | Potencia |
|---:|---:|---:|
| Inicio | 1 | `2⁰` |
| 1 | 2 | `2¹` |
| 2 | 4 | `2²` |
| 3 | 8 | `2³` |
| 4 | 16 | `2⁴` |

</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-mono font-bold text-xl text-amber-800">Después de k iteraciones → i = 2ᵏ</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="p-3 rounded-xl bg-slate-100 border border-slate-200 text-center">
<strong>2</strong> es el factor por el que multiplicamos `i` en cada iteración.
</div>

<div class="p-3 rounded-xl bg-slate-100 border border-slate-200 text-center">
<strong>k</strong> es el número de iteraciones realizadas.
</div>

</div>

---

# De `2ᵏ` a `log₂(n)`

<div class="text-center">

Después de `k` iteraciones: <span class="font-mono font-bold text-xl">i = 2ᵏ</span>

</div>

<div class="mt-2 p-2 rounded-xl bg-amber-50 border border-amber-200 text-center">

El ciclo termina cuando `i` alcanza aproximadamente a `n`:

<span class="font-mono font-bold text-xl ml-2">2ᵏ ≈ n</span>

</div>

<div class="mt-2 p-2 rounded-xl bg-blue-50 border border-blue-200 text-center">

<strong>¿A qué potencia debemos elevar 2 para obtener `n`?</strong>

El logaritmo responde esa pregunta:

<div class="font-mono font-bold text-xl text-blue-800 mt-1">k ≈ log₂(n)</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="p-2 rounded-xl bg-slate-50 border border-slate-200 text-center">

<div class="font-bold text-slate-800">Ejemplo: `n = 16`</div>

<div class="font-mono font-bold text-xl mt-1">2⁴ = 16</div>

<div>Se requieren <strong>4 iteraciones</strong>.</div>

</div>

<div class="p-2 rounded-xl bg-violet-50 border border-violet-200 text-center">

<div class="font-bold text-violet-800">Como logaritmo</div>

<div class="font-mono font-bold text-xl mt-1">log₂(16) = 4</div>

<div>El logaritmo indica cuántas <strong>duplicaciones</strong> necesitamos.</div>

</div>

</div>

<div class="mt-2 p-2 rounded-xl bg-slate-900 text-center">

<span class="font-mono font-bold text-lg text-amber-300">2ᵏ ≈ n ⇔ k ≈ log₂(n)</span>

<span class="!text-white ml-3">→ número de iteraciones: <strong class="text-amber-300">O(log n)</strong></span>

</div>

---

# Complejidad espacial

<div class="mt-3 p-4 rounded-xl bg-violet-50 border border-violet-200">
<p>La complejidad espacial estudia <strong>cómo crece la memoria utilizada</strong> por un algoritmo conforme aumenta el tamaño de la entrada.</p>
</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">
<div class="card-title text-slate-800">Memoria de entrada</div>
<p>Corresponde a los datos que el algoritmo recibe para resolver el problema.</p>
<div class="mt-3 text-center font-mono font-bold">A[0 ... n−1]</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">Espacio auxiliar</div>
<p>Es la <strong>memoria adicional</strong> que el algoritmo necesita para realizar su trabajo.</p>
<div class="mt-3 text-center font-semibold text-violet-800">variables · estructuras · pila</div>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">Al analizar algoritmos es frecuente reportar específicamente el <strong class="text-amber-300">espacio auxiliar</strong>.</p>
</div>

---

# Ejemplo: espacio auxiliar constante

```text
mayor = A[0]

para i = 1 hasta n - 1:
    si A[i] > mayor:
        mayor = A[i]
```

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-slate-100 border border-slate-200">
<div class="card-title text-slate-800">Entrada</div>
<p>El arreglo contiene <strong>n elementos</strong>.</p>
<div class="mt-3 text-center font-mono font-bold">A → O(n)</div>
</div>

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">Memoria adicional</div>
<p>El algoritmo solo necesita unas cuantas variables, independientemente de n.</p>
<div class="mt-3 text-center font-mono font-bold">mayor · i</div>
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<div class="font-mono font-bold text-2xl text-emerald-800">Espacio auxiliar: O(1)</div>
</div>

<div class="mt-3 text-center font-semibold text-slate-700">
Que la entrada ocupe O(n) <span class="text-emerald-700">no significa</span> que el algoritmo requiera O(n) de espacio auxiliar.
</div>

---

# Ejemplo: espacio auxiliar lineal

Supongamos que el algoritmo crea una copia del arreglo:

```text
crear B de tamaño n

para i = 0 hasta n - 1:
    B[i] = A[i]
```

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">Entrada</div>
<div class="mt-3 text-center font-mono font-bold text-xl">A → n elementos</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">Memoria adicional</div>
<div class="mt-3 text-center font-mono font-bold text-xl">B → n elementos</div>
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
<div class="font-mono font-bold text-2xl text-violet-800">Espacio auxiliar: O(n)</div>
</div>

<div class="mt-3 text-center font-semibold text-slate-700">
La memoria adicional crece <span class="text-violet-700">proporcionalmente al tamaño de la entrada</span>.
</div>

---

# Tiempo y espacio describen dimensiones diferentes

<div class="mt-2 text-center">
<p>Un mismo algoritmo debe analizarse desde <strong>ambas dimensiones</strong>.</p>
</div>

<div class="mt-4 p-4 rounded-xl bg-slate-100 border border-slate-200">

```text
mayor = A[0]

para i = 1 hasta n - 1:
    si A[i] > mayor:
        mayor = A[i]
```

</div>

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200 text-center">
<div class="card-title text-blue-800">⏱️ Tiempo</div>
<p>Se recorren los n elementos.</p>
<div class="mt-3 font-mono font-bold text-2xl text-blue-800">O(n)</div>
</div>

<div class="card bg-violet-50 border border-violet-200 text-center">
<div class="card-title text-violet-800">💾 Espacio auxiliar</div>
<p>Solo se mantienen unas cuantas variables.</p>
<div class="mt-3 font-mono font-bold text-2xl text-violet-800">O(1)</div>
</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">La complejidad temporal y espacial <strong class="text-amber-300">no tienen por qué crecer de la misma manera.</strong></p>
</div>

---

# El compromiso tiempo–espacio

<div class="mt-3 text-center">
<p>En algunos problemas podemos reducir el tiempo de ejecución <strong>utilizando memoria adicional</strong>, o ahorrar memoria realizando más trabajo.</p>
</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-blue-50 border border-blue-200 text-center">
<div class="card-title text-blue-800">Priorizar tiempo</div>
<div class="text-3xl my-3">⏱️ ↓</div>
<p>Podemos almacenar información adicional para evitar repetir cálculos o búsquedas.</p>
</div>

<div class="card bg-violet-50 border border-violet-200 text-center">
<div class="card-title text-violet-800">Priorizar espacio</div>
<div class="text-3xl my-3">💾 ↓</div>
<p>Podemos evitar estructuras auxiliares, aunque sea necesario realizar más operaciones.</p>
</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<div class="text-xl font-bold text-amber-300">Trade-off tiempo–espacio</div>
<p class="!text-white mt-2">No existe una solución universalmente mejor: depende de las restricciones del problema.</p>
</div>

---

# Ejemplo de trade-off: detectar repetidos

<div class="mt-2 text-center">
<p>Queremos determinar si un arreglo contiene valores repetidos.</p>
</div>

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">Estrategia A · Comparar pares</div>

```text
para cada elemento:
    comparar con los siguientes
```

<div class="mt-3">
<strong>Tiempo:</strong> <span class="font-mono">O(n²)</span><br>
<strong>Espacio auxiliar:</strong> <span class="font-mono">O(1)</span>
</div>
</div>

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">Estrategia B · Recordar lo visto</div>

```text
para cada elemento:
    comprobar si está en vistos
    agregarlo a vistos
```

<div class="mt-3">
<strong>Tiempo promedio:</strong> <span class="font-mono">O(n)</span>*<br>
<strong>Espacio auxiliar:</strong> <span class="font-mono">O(n)</span>
</div>
</div>

</div>

<div class="mt-4 text-sm text-slate-600">
*Suponiendo operaciones promedio O(1) de consulta e inserción en una tabla hash.
</div>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">La estrategia B <strong class="text-amber-300">intercambia memoria adicional por una reducción del tiempo esperado.</strong></p>
</div>

---

# Entonces, ¿cuál algoritmo es mejor?

<div class="mt-2 text-center">
<p>La notación de complejidad permite comparar alternativas, pero <strong>la decisión depende del contexto</strong>.</p>
</div>

<div class="grid grid-cols-3 gap-4 mt-5">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">n muy grande</div>
<p>Reducir el orden temporal puede justificar el uso de memoria adicional.</p>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">Memoria limitada</div>
<p>Puede ser preferible reducir el espacio aunque aumente el trabajo.</p>
</div>

<div class="card bg-slate-100 border border-slate-200">
<div class="card-title text-slate-800">n pequeño</div>
<p>Las diferencias asintóticas pueden tener poca relevancia práctica.</p>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
<div class="font-bold text-amber-800">Eficiencia no significa únicamente “ser más rápido”.</div>
<p class="mt-2">Debemos considerar <strong>tiempo, espacio, tamaño de entrada y restricciones del problema</strong>.</p>
</div>

---

# Método para analizar un algoritmo

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">1. Definir la entrada</div>
<p>¿Qué cantidad crece y qué representa n?</p>
</div>

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">2. Identificar el trabajo</div>
<p>¿Qué operaciones dependen del tamaño de la entrada?</p>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">3. Contar ejecuciones</div>
<p>¿Cuántas veces se realizan esas operaciones?</p>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">4. Determinar el crecimiento</div>
<p>¿Cuál es el orden temporal resultante?</p>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">5. Analizar memoria</div>
<p>¿Qué espacio adicional requiere y cómo crece?</p>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">6. Evaluar el trade-off</div>
<p>¿La mejora en un recurso justifica el costo en el otro?</p>
</div>

</div>

---
background: /background3.jpg
title: Ejercicio integrador guiado
transition: slide-left
---

# Ejercicio integrador guiado

Analizaremos paso a paso el siguiente algoritmo:

```text
contador = 0

para i = 1 hasta n:
    para j = 1 hasta i:
        contador = contador + 1
```

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

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">
<p class="!text-white">
Aplicaremos los <strong class="text-amber-300">6 pasos del método de análisis</strong>.
</p>
</div>

---

# Paso 1 · Definir la entrada

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿Qué representa <strong>n</strong>?</p>
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
<div class="font-bold text-blue-800">1.1 Localizamos n</div>

```text
para i = 1 hasta n:
```

`n` aparece como límite del ciclo exterior.
</div>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
<div class="font-bold text-amber-800">1.2 Probamos</div>

Si `n = 5`, entonces:

```text
i = 1, 2, 3, 4, 5
```

El ciclo exterior hace 5 iteraciones.
</div>

</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 1:</strong><br>
`n` representa el tamaño de la entrada y determina cuántas veces se ejecuta el ciclo exterior.
</div>

</v-click>

---

# Paso 2 · Identificar el trabajo relevante

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿Qué operaciones dependen de <strong>n</strong>?</p>
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-bold text-slate-800">Ocurre una vez</div>

```text
contador = 0
```

No depende del tamaño `n`.
</div>

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
<div class="font-bold text-blue-800">Se repite dentro de los ciclos</div>

```text
contador = contador + 1
```

Su número de ejecuciones sí depende de `n`.
</div>

</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 2:</strong><br>
La operación relevante es <span class="font-mono">contador = contador + 1</span>.
</div>

</v-click>

---

# Paso 3 · Contar ejecuciones

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿Cuántas veces se realiza la operación relevante?</p>
</div>

<div class="mt-4 text-center">
Para observarlo claramente, fijaremos:
</div>

<div class="mt-3 text-center">
<span class="inline-block font-mono font-bold text-3xl text-amber-800 bg-amber-50 border border-amber-200 rounded-xl px-6 py-2">
n = 5
</span>
</div>

<v-click>

<div class="mt-5 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
Cada <strong>●</strong> representará una ejecución de:
<span class="font-mono font-bold">contador = contador + 1</span>
</div>

</v-click>

---

# Paso 3.1 · Primera vuelta exterior

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-center mb-2">
<strong>n = 5</strong> y ahora <strong>i = 1</strong>
</div>

```text
contador = 0

para i = 1 hasta 5:
    para j = 1 hasta 1:
        contador = contador + 1
```

</div>

<div>

<v-click>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="font-bold text-amber-800">Ejecución interna</div>

```text
j = 1
contador = 0 + 1 = 1
```

</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-amber-300">
i = 1 → ● → contador = 1
</div>
</div>

</v-click>

</div>

</div>

---

# Paso 3.2 · Segunda vuelta exterior

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-center mb-2">
<strong>n = 5</strong> y ahora <strong>i = 2</strong>
</div>

```text
contador = 1

para i = 2 hasta 5:
    para j = 1 hasta 2:
        contador = contador + 1
```

</div>

<div>

<v-click>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="font-bold text-amber-800">Ejecución interna</div>

```text
j = 1 → contador = 1 + 1 = 2
j = 2 → contador = 2 + 1 = 3
```

</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-amber-300">
i = 1 → ● &nbsp;&nbsp; contador = 1<br>
i = 2 → ● ● &nbsp; contador = 3
</div>
</div>

</v-click>

</div>

</div>

---

# Paso 3.3 · Tercera vuelta exterior

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-center mb-2">
<strong>n = 5</strong> y ahora <strong>i = 3</strong>
</div>

```text
contador = 3

para i = 3 hasta 5:
    para j = 1 hasta 3:
        contador = contador + 1
```

</div>

<div>

<v-click>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="font-bold text-amber-800">Ejecución interna</div>

```text
j = 1 → contador = 4
j = 2 → contador = 5
j = 3 → contador = 6
```

</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-amber-300">
i = 1 → ● &nbsp;&nbsp;&nbsp;&nbsp; contador = 1<br>
i = 2 → ● ● &nbsp;&nbsp; contador = 3<br>
i = 3 → ● ● ● contador = 6
</div>
</div>

</v-click>

</div>

</div>

---

# Paso 3.4 · Cuarta vuelta exterior

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-center mb-2">
<strong>n = 5</strong> y ahora <strong>i = 4</strong>
</div>

```text
contador = 6

para i = 4 hasta 5:
    para j = 1 hasta 4:
        contador = contador + 1
```

</div>

<div>

<v-click>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="font-bold text-amber-800">Ejecución interna</div>

```text
j = 1 → contador = 7
j = 2 → contador = 8
j = 3 → contador = 9
j = 4 → contador = 10
```

</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-amber-300">
i = 1 → ● &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; contador = 1<br>
i = 2 → ● ● &nbsp;&nbsp;&nbsp;&nbsp; contador = 3<br>
i = 3 → ● ● ● &nbsp; contador = 6<br>
i = 4 → ● ● ● ● contador = 10
</div>
</div>

</v-click>

</div>

</div>

---

# Paso 3.5 · Quinta vuelta exterior

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-center mb-2">
<strong>n = 5</strong> y ahora <strong>i = 5</strong>
</div>

```text
contador = 10

para i = 5 hasta 5:
    para j = 1 hasta 5:
        contador = contador + 1
```

</div>

<div>

<v-click>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="font-bold text-amber-800">Ejecución interna</div>

```text
j = 1 → contador = 11
j = 2 → contador = 12
j = 3 → contador = 13
j = 4 → contador = 14
j = 5 → contador = 15
```

</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-amber-300">
i = 5 → ● ● ● ● ● → contador = 15
</div>
<div class="!text-white mt-1">Aquí `j` sí llega hasta `n`, pero solo en la última vuelta.</div>
</div>

</v-click>

</div>

</div>

---

# Paso 3.6 · Ver el patrón completo

<v-click>

<table class="w-full text-center border-collapse mt-2">
<thead>
<tr class="bg-slate-900 text-white">
<th class="p-2">i</th>
<th class="p-2">Valores de j</th>
<th class="p-2">Incrementos</th>
<th class="p-2">contador</th>
</tr>
</thead>
<tbody>
<tr><td class="p-2 border">1</td><td class="p-2 border">1</td><td class="p-2 border">1</td><td class="p-2 border font-bold">1</td></tr>
<tr><td class="p-2 border">2</td><td class="p-2 border">1, 2</td><td class="p-2 border">2</td><td class="p-2 border font-bold">3</td></tr>
<tr><td class="p-2 border">3</td><td class="p-2 border">1, 2, 3</td><td class="p-2 border">3</td><td class="p-2 border font-bold">6</td></tr>
<tr><td class="p-2 border">4</td><td class="p-2 border">1, 2, 3, 4</td><td class="p-2 border">4</td><td class="p-2 border font-bold">10</td></tr>
<tr><td class="p-2 border">5</td><td class="p-2 border">1, 2, 3, 4, 5</td><td class="p-2 border">5</td><td class="p-2 border font-bold">15</td></tr>
</tbody>
</table>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
El total no es <strong>5 × 5</strong>, porque el ciclo interior no realiza 5 iteraciones en cada vuelta.
</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-xl text-amber-300">
1 + 2 + 3 + 4 + 5 = 15
</div>
</div>

</v-click>

---

# Paso 3.7 · Generalizar el conteo

<v-click>

<div class="grid grid-cols-3 gap-4 mt-3 text-center">

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
<div class="font-bold text-blue-800">Si n = 5</div>
<div class="font-mono mt-2">1+2+3+4+5</div>
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200">
<div class="font-bold text-violet-800">Si n = 6</div>
<div class="font-mono mt-2">1+2+3+4+5+6</div>
</div>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
<div class="font-bold text-amber-800">Si n cambia</div>
<div class="font-mono mt-2">1+2+...+n</div>
</div>

</div>

</v-click>

<v-click>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-2xl text-amber-300">
1 + 2 + 3 + ... + n
</div>
<p class="!text-white mt-1">
Esta suma representa todas las ejecuciones de la operación relevante.
</p>
</div>

</v-click>

---

# Paso 3.8 · Calcular la suma

<v-click>

<div class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
La suma de los primeros `n` números naturales se calcula con:
<div class="font-mono font-bold text-2xl text-blue-800 mt-2">
1 + 2 + ... + n = n(n+1)/2
</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
<div class="font-bold text-slate-800">Comprobación con n = 5</div>
<div class="font-mono mt-2">
5(5+1)/2<br>
= 5(6)/2<br>
= 30/2<br>
= 15
</div>
</div>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
<div class="font-bold text-amber-800">Coincide con el conteo</div>
<div class="font-mono font-bold text-xl mt-3">
1+2+3+4+5 = 15
</div>
</div>

</div>

</v-click>

---

# Paso 3.9 · Obtener T(n)

<v-click>

<div class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
Partimos de:
<div class="font-mono font-bold text-2xl text-blue-800 mt-1">
T(n) = n(n+1)/2
</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-3 mt-4 text-center">

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-bold">Multiplicamos</div>
<div class="font-mono mt-2">n(n+1) = n²+n</div>
</div>

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-bold">Dividimos entre 2</div>
<div class="font-mono mt-2">(n²+n)/2</div>
</div>

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
<div class="font-bold text-amber-800">Separamos términos</div>
<div class="font-mono mt-2">½n² + ½n</div>
</div>

</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 3:</strong><br>
La operación relevante se ejecuta <span class="font-mono">n(n+1)/2</span> veces, por lo que:
<div class="font-mono font-bold text-xl mt-1">T(n) = ½n² + ½n</div>
</div>

</v-click>

---

# Paso 4 · Determinar el crecimiento

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿Cómo crece el trabajo cuando aumenta <strong>n</strong>?</p>
</div>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
Ya obtuvimos:
<div class="font-mono font-bold text-2xl text-blue-800 mt-1">
T(n) = ½n² + ½n
</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
<div class="font-bold text-amber-800">Término cuadrático</div>
<div class="font-mono font-bold text-2xl mt-2">½n²</div>
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
<div class="font-bold text-violet-800">Término lineal</div>
<div class="font-mono font-bold text-2xl mt-2">½n</div>
</div>

</div>

</v-click>

---

# Paso 4.1 · Comparar n contra n²

<v-click>

<table class="w-full text-center border-collapse mt-3">
<thead>
<tr class="bg-slate-900 text-white">
<th class="p-2">n</th>
<th class="p-2">n</th>
<th class="p-2">n²</th>
</tr>
</thead>
<tbody>
<tr><td class="p-2 border">10</td><td class="p-2 border">10</td><td class="p-2 border font-bold">100</td></tr>
<tr><td class="p-2 border">100</td><td class="p-2 border">100</td><td class="p-2 border font-bold">10,000</td></tr>
<tr><td class="p-2 border">1,000</td><td class="p-2 border">1,000</td><td class="p-2 border font-bold">1,000,000</td></tr>
</tbody>
</table>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Cuando `n` crece, <strong>n²</strong> aumenta mucho más rápido que <strong>n</strong>.
</div>

</v-click>

<v-click>

<div class="mt-3 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 4:</strong><br>
El algoritmo presenta <strong>crecimiento cuadrático</strong>, porque el término que domina es <span class="font-mono">n²</span>.
</div>

</v-click>

---

# Paso 5 · Analizar memoria adicional

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿Cuánta memoria adicional requiere el algoritmo?</p>
</div>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200">
<div class="font-bold text-violet-800">Variables auxiliares utilizadas</div>

```text
contador
i
j
```

</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-3 mt-4 text-center">

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-mono font-bold">n = 5</div>
contador, i, j
</div>

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-mono font-bold">n = 100</div>
contador, i, j
</div>

<div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
<div class="font-mono font-bold">n = 1,000,000</div>
contador, i, j
</div>

</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 5:</strong><br>
La memoria auxiliar no aumenta con `n`; el espacio auxiliar es constante:
<span class="font-mono font-bold">O(1)</span>.
</div>

</v-click>

---

# Paso 6 · Evaluar el trade-off

<div class="mt-2 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-bold text-amber-300">Pregunta guía</div>
<p class="!text-white mt-1">¿La mejora en un recurso justifica el costo en el otro?</p>
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
<div class="font-bold text-blue-800">Tiempo</div>
<div class="font-mono font-bold text-2xl mt-2">crecimiento cuadrático</div>
</div>

<div class="p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
<div class="font-bold text-violet-800">Espacio auxiliar</div>
<div class="font-mono font-bold text-2xl mt-2">O(1)</div>
</div>

</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Un trade-off aparece cuando usamos <strong>más memoria para reducir tiempo</strong> o aceptamos <strong>más trabajo para ahorrar memoria</strong>.
</div>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
<strong class="text-emerald-800">Respuesta del paso 6:</strong><br>
Aquí no hay un trade-off explícito: el principal costo está en el tiempo, mientras que la memoria auxiliar permanece constante.
</div>

</v-click>

---

# Resultado del ejercicio

<v-click>

<table class="w-full text-left border-collapse mt-2">
<thead>
<tr class="bg-slate-900 text-white">
<th class="p-2">Paso</th>
<th class="p-2">Pregunta</th>
<th class="p-2">Respuesta</th>
</tr>
</thead>
<tbody>
<tr><td class="p-2 border">1</td><td class="p-2 border">¿Qué representa n?</td><td class="p-2 border">Tamaño de entrada</td></tr>
<tr><td class="p-2 border">2</td><td class="p-2 border">¿Qué operaciones dependen de n?</td><td class="p-2 border">contador = contador + 1</td></tr>
<tr><td class="p-2 border">3</td><td class="p-2 border">¿Cuántas veces se realizan?</td><td class="p-2 border">n(n+1)/2</td></tr>
<tr><td class="p-2 border">4</td><td class="p-2 border">¿Cómo crece el trabajo?</td><td class="p-2 border">Cuadráticamente</td></tr>
<tr><td class="p-2 border">5</td><td class="p-2 border">¿Cuánta memoria adicional?</td><td class="p-2 border">Constante: O(1)</td></tr>
<tr><td class="p-2 border">6</td><td class="p-2 border">¿Hay trade-off?</td><td class="p-2 border">No explícito</td></tr>
</tbody>
</table>

</v-click>

<v-click>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-xl text-amber-300">T(n) = ½n² + ½n</div>
<p class="!text-white mt-1">
Siguiente pregunta: ¿por qué esta función puede expresarse como <strong class="text-amber-300">O(n²)</strong>?
</p>
</div>

</v-click>

---

# Síntesis · Tiempo y espacio

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">⏱️ Complejidad temporal</div>
<p>Analiza cómo crece el <strong>trabajo realizado</strong>.</p>
<div class="mt-3 text-center font-mono font-bold text-xl text-blue-800">T(n) → O(...)</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">💾 Complejidad espacial</div>
<p>Analiza cómo crece la <strong>memoria requerida</strong>.</p>
<div class="mt-3 text-center font-mono font-bold text-xl text-violet-800">S(n) → O(...)</div>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="font-mono font-bold text-lg text-amber-300">Algoritmo → Tiempo + Espacio → Trade-off → Decisión</div>
<p class="!text-white mt-2">Analizar eficiencia permite comparar soluciones considerando no solo si resuelven el problema, sino <strong>qué recursos necesitan para hacerlo.</strong></p>
</div>
