---
background: /background3.jpg
title: Algoritmia y Estructura de Datos
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">

<div class="flex flex-col items-center gap-1 mb-5">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400 bg-amber-400/10 px-3 py-1 rounded-full border border-amber-400/20">
Instituto Tecnológico de Colima
</span>
<span class="text-sm text-slate-300 font-medium">
Ingeniería en Inteligencia Artificial
</span>
</div>

<h1 class="text-4xl font-black tracking-tight bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent !leading-tight mb-2">
Algoritmia y Estructura de Datos
</h1>

<div class="mt-3 mb-5">
<div class="text-xl font-semibold text-amber-300 tracking-tight">
1.2 Complejidad Algorítmica
</div>
</div>

<div class="mt-6 pt-5 border-t border-white/10 flex flex-col items-center gap-1">
<span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-400">
Catedrática
</span>
<div class="text-lg font-bold text-white mb-3">
Dra. Patricia Elizabeth Figueroa Millán
</div>

<div class="flex flex-wrap justify-center items-center gap-3 text-xs font-mono text-slate-300">
<span class="bg-white/10 px-3 py-1.5 rounded-lg border border-white/10">
correo: patricia.figueroa@colima.tecnm.mx
</span>
<span class="bg-white/10 px-3 py-1.5 rounded-lg border border-white/10">
instagram: @patricia.figueroa.tecnm.mx
</span>
</div>
</div>

</div>

---

# Introducción a la Complejidad Computacional

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
✓ Correcto no siempre significa eficiente
</div>

<p>
Un programa debe producir los <strong>resultados esperados</strong>, pero también debe hacerlo utilizando los recursos computacionales de manera eficiente.
</p>

<p class="mt-3">
La <strong>complejidad computacional</strong> —o complejidad algorítmica— estudia cómo cambia el consumo de recursos de un algoritmo cuando aumenta el tamaño del problema.
</p>

</div>

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
📈 El problema aparece cuando los datos crecen
</div>

<p>
Las computadoras actuales realizan millones de operaciones rápidamente, pero esto no compensa necesariamente un algoritmo ineficiente.
</p>

<p class="mt-3">
Con grandes volúmenes de datos, un algoritmo puede requerir cantidades excesivas de <strong>tiempo</strong> o <strong>memoria</strong>, incluso ejecutándose sobre hardware muy potente.
</p>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-white border border-slate-700">

<div class="font-bold text-amber-300 mb-2">
La complejidad permite anticipar el comportamiento
</div>

<p class="!text-white">
El análisis algorítmico proporciona herramientas conceptuales y matemáticas para estimar cómo se comportará una solución al escalar el problema, permitiendo comparar alternativas y tomar decisiones de diseño fundamentadas.
</p>

</div>


---

# La pregunta central de la complejidad

<div class="mt-5 p-5 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200">

<div class="text-center text-2xl font-semibold text-slate-800 leading-snug">
A medida que aumenta el tamaño de los datos de entrada,
<br>
<span class="text-amber-700">
¿cómo cambia el comportamiento del algoritmo?
</span>
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
🚫 No buscamos medir segundos
</div>

<p>
El tiempo físico de ejecución depende de factores externos como:
</p>

<ul class="mt-2">
<li>procesador y memoria disponible,</li>
<li>sistema operativo,</li>
<li>lenguaje y compilador,</li>
<li>otras aplicaciones en ejecución.</li>
</ul>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
✓ Analizamos el crecimiento
</div>

<p>
En lugar de medir cuánto tarda una computadora específica, estudiamos cómo aumenta la cantidad de operaciones necesarias cuando crece el tamaño de la entrada.
</p>

<div class="mt-4 text-center">
<span class="font-mono font-bold text-xl text-amber-800 bg-white px-4 py-2 rounded-lg border border-amber-200">
n → tamaño de la entrada
</span>
</div>

</div>

</div>

<div class="mt-5 text-center text-lg font-semibold text-slate-700">

El objetivo no es saber exactamente cuánto tardará un programa,<br>
sino entender <span class="text-amber-700">cómo escala su costo computacional.</span>

</div>

---

# ¿Cómo podemos comparar algoritmos?

<div class="mt-5 text-center">
<p class="text-lg">
Si el tiempo de ejecución depende de la computadora utilizada...
</p>
<div class="text-2xl font-semibold text-amber-700 mt-2">
¿cómo podemos analizar la eficiencia de un algoritmo de manera independiente del hardware?
</div>
</div>

<div class="grid grid-cols-2 gap-5 mt-6">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
⏱️ Medir el tiempo de ejecución
</div>

<p>
Nos dice cuánto tardó una implementación concreta bajo determinadas condiciones.
</p>

<div class="mt-3 font-mono text-center text-slate-600">
algoritmo + hardware + software → segundos
</div>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
🔍 Analizar el algoritmo
</div>

<p>
Busca determinar cuántas operaciones requiere y cómo aumenta ese trabajo cuando crece el tamaño de la entrada.
</p>

<div class="mt-3 font-mono text-center text-amber-800">
tamaño n → número de operaciones
</div>

</div>

</div>

<div class="mt-6 p-4 rounded-xl bg-slate-900 text-white text-center">

<p class="!text-white">
Para comparar algoritmos necesitamos establecer <strong class="text-amber-300">qué operaciones contamos y qué costo asumimos para ellas.</strong>
</p>

<div class="mt-3 text-xl font-semibold text-amber-300">
→ Necesitamos un modelo de cómputo
</div>

</div>

---

# El modelo de cómputo estándar: RAMx

<div class="grid grid-cols-5 gap-5 mt-5 items-stretch">

<div class="col-span-3 card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
¿Por qué necesitamos un modelo?
</div>

<p>
Para predecir y comparar rigurosamente la eficiencia de los algoritmos necesitamos establecer <strong>condiciones comunes de análisis</strong>.
</p>

<p class="mt-3">
No sería práctico que nuestras conclusiones cambiaran dependiendo de la arquitectura de una CPU o de las características particulares de una computadora.
</p>

</div>

<div class="col-span-2 card bg-amber-50 border border-amber-200 flex flex-col justify-center text-center">

<div class="text-sm font-mono font-bold uppercase tracking-wider text-amber-700">
Modelo teórico estándar
</div>

<div class="text-2xl font-bold text-slate-800 mt-2">
RAM
</div>

<div class="text-lg font-semibold text-amber-800">
Random-Access Machine
</div>

<div class="mt-3 text-slate-600">
Máquina de Acceso Aleatorio
</div>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 border border-slate-700 text-white">

<div class="font-bold text-amber-300 mb-2">
Una abstracción para analizar algoritmos
</div>

<p class="!text-white">
El modelo RAM representa una computadora <strong>monoprocesador</strong> idealizada y establece un conjunto de reglas sobre cómo se ejecutan las instrucciones, cuánto cuestan las operaciones y cómo se accede a la memoria.
</p>

</div>

<div class="mt-4 text-center text-slate-700 font-semibold">
Así podemos comparar algoritmos bajo <span class="text-amber-700">los mismos supuestos computacionales.</span>
</div>

---

# Modelo RAM: ejecución y operaciones básicas

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
1. Ejecución secuencial
</div>

<p>
Las instrucciones se ejecutan <strong>una después de otra</strong>, siguiendo estrictamente su secuencia.
</p>

<div class="mt-4 flex justify-center items-center gap-2 font-mono font-bold text-slate-700">
<span class="bg-white border border-slate-300 px-3 py-2 rounded-lg">I₁</span>
<span>→</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded-lg">I₂</span>
<span>→</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded-lg">I₃</span>
<span>→</span>
<span>...</span>
</div>

<div class="mt-4 text-center text-slate-600 font-semibold">
Sin concurrencia · Sin paralelismo
</div>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
2. Costo constante
</div>

<p>
Cada instrucción básica o <strong>primitiva</strong> se considera una operación que requiere la misma cantidad constante de tiempo.
</p>

<div class="mt-4 text-center">
<span class="font-mono font-bold text-amber-800 bg-white px-4 py-2 rounded-lg border border-amber-200">
1 primitiva → costo constante
</span>
</div>

</div>

</div>

<div class="mt-5 mb-2 font-semibold text-slate-700">
¿Qué consideramos una operación básica?
</div>

<div class="grid grid-cols-3 gap-4">

<div class="card bg-blue-50 border border-blue-200 text-center">
<div class="card-title text-blue-800">
Aritmética
</div>
<p>
Suma, resta, multiplicación, división, residuo, <em>floor</em> y <em>ceiling</em>.
</p>
</div>

<div class="card bg-emerald-50 border border-emerald-200 text-center">
<div class="card-title text-emerald-800">
Movimiento de datos
</div>
<p>
Copiar valores, cargar (<em>load</em>) y almacenar (<em>store</em>).
</p>
</div>

<div class="card bg-violet-50 border border-violet-200 text-center">
<div class="card-title text-violet-800">
Control
</div>
<p>
Bifurcaciones, llamadas a subrutinas y retornos de funciones.
</p>
</div>

</div>

---

# Modelo RAM: acceso uniforme a memoria

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
3. Acceso uniforme a memoria
</div>

<p>
Recuperar o almacenar un valor en <strong>cualquier posición de memoria</strong> requiere una cantidad constante de tiempo.
</p>

</div>

<div class="mt-4">

<div class="grid grid-cols-6 gap-2 text-center font-mono">

<div>
<div class="text-slate-500 mb-1">0</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">17</div>
</div>

<div>
<div class="text-slate-500 mb-1">1</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">8</div>
</div>

<div>
<div class="text-slate-500 mb-1">2</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">31</div>
</div>

<div>
<div class="text-slate-500 mb-1">3</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">4</div>
</div>

<div>
<div class="text-slate-500 mb-1">...</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">...</div>
</div>

<div>
<div class="text-slate-500 mb-1">n−1</div>
<div class="bg-white border-2 border-amber-300 rounded-lg p-2 font-bold">9</div>
</div>

</div>

<div class="mt-3 text-center">
<span class="inline-block font-mono font-bold text-amber-800 bg-amber-50 px-4 py-2 rounded-lg border border-amber-200">
Cualquier posición → mismo costo de acceso
</span>
</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
¿Qué supone el modelo?
</div>

<p>
El costo de acceder a una dirección de memoria <strong>no depende de su ubicación</strong> ni del tamaño total de la memoria utilizada.
</p>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
Ejemplo: un arreglo
</div>

<p>
Si conocemos el índice, podemos acceder directamente a un elemento sin recorrer los elementos anteriores.
</p>

</div>

</div>

<div class="mt-4 text-center font-semibold text-slate-700">
De este supuesto proviene el término <span class="text-amber-700">Random Access</span>: acceso directo bajo un mismo modelo de costo.
</div>

---

# Modelo RAM: representación de datos acotada

<div class="mt-3 p-3 rounded-xl bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
4. Representación de datos acotada
</div>

<p>
El modelo RAM no supone que una celda de memoria pueda almacenar información ilimitada. Los enteros se representan mediante <strong>palabras de tamaño acotado</strong>.
</p>

</div>

<div class="grid grid-cols-5 gap-4 mt-4 items-center">

<div class="col-span-2 text-center">

<div class="inline-block bg-amber-50 border-2 border-amber-200 rounded-2xl px-7 py-4">

<div class="font-semibold text-amber-700 mb-2">
Tamaño de una palabra
</div>

<div class="font-mono font-bold text-2xl text-slate-800">
c log₂ n bits
</div>

<div class="mt-1 font-mono text-slate-600">
c ≥ 1
</div>

</div>

</div>

<div class="col-span-3">

<p>
El tamaño de palabra debe ser suficiente para <strong>representar el tamaño de la entrada n</strong> y direccionar las posiciones de memoria necesarias para procesarla.
</p>

</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card bg-emerald-50 border border-emerald-200">

<div class="card-title text-emerald-800">
✓ Lo que permite
</div>

<p>
Representar valores y direcciones suficientemente grandes para trabajar con los datos de entrada.
</p>

</div>

<div class="card bg-red-50 border border-red-200">

<div class="card-title text-red-800">
✗ Lo que evita
</div>

<p>
Suponer que una sola palabra puede almacenar o procesar cantidades arbitrariamente grandes de información.
</p>

</div>

</div>

<div class="mt-4 text-center font-semibold text-slate-700">
Así, el modelo mantiene una abstracción simple <span class="text-amber-700">sin asumir recursos ilimitados.</span>
</div>

---

# ¿De qué depende el costo de un algoritmo?

<div class="mt-2 text-center">

<p>
El modelo RAM establece qué operaciones consideramos básicas y qué costo asumimos para ellas.
</p>

<div class="mt-2 text-xl font-semibold text-amber-700">
Pero... ¿un algoritmo realiza siempre la misma cantidad de operaciones?
</div>

</div>

<div class="grid grid-cols-3 gap-4 mt-4 items-center">

<div class="card bg-slate-100 border border-slate-200 text-center">

<div class="card-title text-slate-800">
Entrada pequeña
</div>

<div class="font-mono text-xl font-bold text-slate-700 my-2">
[ 8, 3, 5 ]
</div>

<p>
Pocos datos que procesar.
</p>

</div>

<div class="text-center">

<div class="text-4xl font-bold text-amber-600">
→
</div>

<div class="mt-1 font-semibold text-slate-600">
La entrada crece
</div>

</div>

<div class="card bg-amber-50 border border-amber-200 text-center">

<div class="card-title text-amber-800">
Entrada grande
</div>

<div class="font-mono text-xl font-bold text-amber-800 my-2">
[ 8, 3, 5, ..., 21 ]
</div>

<p>
Más datos pueden implicar más operaciones y mayor consumo de recursos.
</p>

</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 border border-slate-700 text-center">

<p class="!text-white">
Para predecir cómo aumenta el costo, necesitamos expresarlo en función del <strong class="text-amber-300">tamaño del problema.</strong>
</p>

<div class="mt-2">
<span class="inline-block font-mono font-bold text-xl text-amber-300 bg-white/10 px-4 py-1.5 rounded-lg border border-white/10">
n = tamaño de la entrada
</span>
</div>

</div>

---

# El tamaño de la entrada: n

<div class="mt-4 p-4 rounded-xl bg-amber-50 border border-amber-200">

<p class="text-center">
El costo de un algoritmo se expresa en función del <strong>tamaño de la entrada</strong>, representado convencionalmente mediante:
</p>

<div class="text-center mt-3">
<span class="inline-block font-mono font-bold text-3xl text-amber-800 bg-white px-5 py-2 rounded-xl border border-amber-200">
n
</span>
</div>

</div>

<div class="mt-4 text-center font-semibold text-slate-700">
Pero <span class="text-amber-700">n no significa siempre “número de elementos”.</span><br>
Su definición depende de la naturaleza del problema.
</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
🔎 Ordenación y búsqueda
</div>

<p>
El tamaño de la entrada corresponde al <strong>número de elementos</strong> contenidos en la lista o arreglo sobre el que opera el algoritmo.
</p>

<div class="mt-4 text-center font-mono">

<div class="flex justify-center gap-1">
<span class="bg-white border border-slate-300 px-3 py-2 rounded">14</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded">7</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded">21</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded">3</span>
<span class="bg-white border border-slate-300 px-3 py-2 rounded">9</span>
</div>

<div class="mt-3 font-bold text-slate-700">
n = 5 elementos
</div>

</div>

</div>

<div class="card bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">
🔢 Problemas numéricos
</div>

<p>
Cuando se opera con números, el tamaño de la entrada puede medirse mediante el <strong>número de bits necesarios para representar la información</strong>.
</p>

<div class="mt-4 text-center">

<div class="font-mono font-bold text-xl text-blue-800 bg-white border border-blue-200 rounded-lg px-4 py-2 inline-block">
11010110
</div>

<div class="mt-3 font-mono font-bold text-blue-800">
n = 8 bits
</div>

</div>

</div>

</div>

---

# Cuando una sola variable no es suficiente

<div class="mt-4 text-center">

<p>
Algunos problemas poseen entradas cuya dimensión no puede describirse adecuadamente mediante un único valor <strong>n</strong>.
</p>

<div class="text-xl font-semibold text-amber-700 mt-2">
Los grafos son un ejemplo importante.
</div>

</div>

<div class="grid grid-cols-5 gap-5 mt-5 items-stretch">

<div class="col-span-2 card bg-slate-100 border border-slate-200 flex flex-col justify-center">

<div class="card-title text-slate-800">
🌐 Problemas sobre grafos
</div>

<p>
El tamaño de un grafo se describe utilizando simultáneamente dos parámetros:
</p>

<div class="mt-4 space-y-3">

<div class="bg-white border border-slate-200 rounded-lg p-3">
<span class="font-mono font-bold text-xl text-amber-700">V</span>
<span class="ml-2 font-semibold">número de vértices o nodos</span>
</div>

<div class="bg-white border border-slate-200 rounded-lg p-3">
<span class="font-mono font-bold text-xl text-amber-700">E</span>
<span class="ml-2 font-semibold">número de aristas o conexiones</span>
</div>

</div>

</div>

<div class="col-span-3 card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800 text-center">
Ejemplo
</div>

<div class="relative h-44 mt-2">

<div class="absolute left-[45%] top-1 w-10 h-10 rounded-full bg-white border-2 border-amber-500 flex items-center justify-center font-bold">A</div>
<div class="absolute left-[20%] top-[45%] w-10 h-10 rounded-full bg-white border-2 border-amber-500 flex items-center justify-center font-bold">B</div>
<div class="absolute left-[70%] top-[45%] w-10 h-10 rounded-full bg-white border-2 border-amber-500 flex items-center justify-center font-bold">C</div>
<div class="absolute left-[32%] top-[78%] w-10 h-10 rounded-full bg-white border-2 border-amber-500 flex items-center justify-center font-bold">D</div>
<div class="absolute left-[58%] top-[78%] w-10 h-10 rounded-full bg-white border-2 border-amber-500 flex items-center justify-center font-bold">E</div>

<svg class="absolute inset-0 w-full h-full -z-0" viewBox="0 0 400 180">
<line x1="200" y1="25" x2="95" y2="90" stroke="#94a3b8" stroke-width="3"/>
<line x1="200" y1="25" x2="305" y2="90" stroke="#94a3b8" stroke-width="3"/>
<line x1="95" y1="90" x2="145" y2="150" stroke="#94a3b8" stroke-width="3"/>
<line x1="305" y1="90" x2="255" y2="150" stroke="#94a3b8" stroke-width="3"/>
<line x1="145" y1="150" x2="255" y2="150" stroke="#94a3b8" stroke-width="3"/>
<line x1="95" y1="90" x2="305" y2="90" stroke="#94a3b8" stroke-width="3"/>
</svg>

</div>

<div class="text-center mt-2">
<span class="font-mono font-bold text-lg text-amber-800 bg-white px-4 py-2 rounded-lg border border-amber-200">
|V| = 5 &nbsp;&nbsp; |E| = 6
</span>
</div>

</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
La medida del tamaño de la entrada debe reflejar las <strong class="text-amber-300">características relevantes del problema que estamos analizando.</strong>
</p>

</div>

---

# Del tamaño de entrada al crecimiento

<div class="mt-4 text-center">

<p>
Ya podemos describir el costo de un algoritmo en función del <strong>tamaño de su entrada n</strong>.
</p>

<div class="mt-3 text-2xl font-semibold text-amber-700">
Pero conocer una fórmula de costo no es suficiente...
</div>

</div>

<div class="grid grid-cols-3 gap-4 mt-6 items-center">

<div class="card bg-slate-100 border border-slate-200 text-center">

<div class="card-title text-slate-800">
Tamaño de entrada
</div>

<div class="my-3 font-mono font-bold text-3xl text-slate-700">
n
</div>

<p>
Representa cuánto debe procesar el algoritmo.
</p>

</div>

<div class="text-center">

<div class="text-4xl font-bold text-amber-600">
→
</div>

<div class="mt-2 font-semibold text-slate-600">
determina
</div>

</div>

<div class="card bg-amber-50 border border-amber-200 text-center">

<div class="card-title text-amber-800">
Costo
</div>

<div class="my-3 font-mono font-bold text-3xl text-amber-800">
T(n)
</div>

<p>
Expresa la cantidad de trabajo requerido para una entrada de tamaño n.
</p>

</div>

</div>

<div class="mt-6 p-4 rounded-xl bg-slate-900 border border-slate-700 text-center">

<p class="!text-white">
Ahora nos interesa una pregunta diferente:
</p>

<div class="mt-2 text-xl font-semibold text-amber-300">
¿Qué tan rápido crece T(n) cuando n se hace cada vez más grande?
</div>

</div>

---

# Eficiencia asintótica

<div class="mt-4 p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

<p>
El análisis de complejidad se concentra en el comportamiento del algoritmo cuando el <strong>tamaño de la entrada crece considerablemente</strong>.
</p>

<div class="mt-3 inline-block bg-white border border-amber-200 rounded-xl px-6 py-3">

<div class="font-mono font-bold text-2xl text-amber-800">
n → ∞
</div>

</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
🔬 En pequeña escala
</div>

<p>
Los costos de inicialización, las constantes y pequeñas diferencias entre operaciones pueden influir apreciablemente en el tiempo de ejecución.
</p>

<div class="mt-4 text-center font-mono text-slate-600">
n pequeño → los detalles importan
</div>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
📈 A gran escala
</div>

<p>
Cuando <strong>n crece</strong>, esos detalles pierden relevancia y comienza a dominar la tendencia de crecimiento del costo.
</p>

<div class="mt-4 text-center font-mono font-bold text-amber-800">
n grande → domina el crecimiento
</div>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
La <strong class="text-amber-300">eficiencia asintótica</strong> estudia cómo crece el consumo de tiempo o memoria de un algoritmo cuando <strong>n tiende a infinito.</strong>
</p>

</div>


---

# ¿Qué conservamos y qué ignoramos?

<div class="mt-3 text-center">

<p>
En el análisis asintótico buscamos capturar la <strong>tendencia dominante de crecimiento</strong>, no reproducir cada detalle del costo.
</p>

</div>

<div class="mt-4 text-center">

<div class="inline-block bg-slate-100 border border-slate-200 rounded-xl px-7 py-3">
<span class="font-mono font-bold text-2xl text-slate-800">
T(n) = 3n² + 10n + 50
</span>
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
1. Ignoramos coeficientes constantes
</div>

<p>
Las constantes multiplicativas pueden reflejar diferencias de implementación, lenguaje o plataforma y no modifican la tendencia fundamental de crecimiento.
</p>

<div class="mt-4 text-center font-mono font-bold text-lg">
<span class="text-slate-400 line-through">3</span><span class="text-amber-700">n²</span>
</div>

</div>

<div class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">
2. Conservamos el término dominante
</div>

<p>
Cuando <strong>n</strong> es suficientemente grande, el término de mayor orden domina el costo total y los términos de menor crecimiento pierden relevancia.
</p>

<div class="mt-4 text-center font-mono font-bold text-lg">
<span class="text-amber-800">n²</span>
<span class="text-slate-400"> + </span>
<span class="text-slate-400 line-through">10n + 50</span>
</div>

</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-mono font-bold text-xl text-white">
3n² + 10n + 50
<span class="text-amber-300 mx-3">→</span>
n²
</div>

<p class="!text-white mt-2">
Nos interesa el <strong class="text-amber-300">orden de crecimiento</strong> que domina cuando n aumenta.
</p>

</div>

---

# El orden de crecimiento importa

<div class="mt-3 text-center">

<p>
Dos algoritmos pueden resolver correctamente el mismo problema y comportarse de manera similar para entradas pequeñas.
</p>

<div class="mt-2 text-xl font-semibold text-amber-700">
La diferencia se vuelve evidente cuando el problema escala.
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-emerald-50 border border-emerald-200 text-center">

<div class="card-title text-emerald-800">
Algoritmo A
</div>

<div class="font-mono font-bold text-2xl text-emerald-800 my-3">
T(n) = n
</div>

<p>
Si duplicamos el tamaño de la entrada, el trabajo requerido crece proporcionalmente.
</p>

<div class="mt-3 bg-white rounded-lg border border-emerald-200 p-2 font-mono">
n = 1,000 → 1,000
</div>

</div>

<div class="card bg-red-50 border border-red-200 text-center">

<div class="card-title text-red-800">
Algoritmo B
</div>

<div class="font-mono font-bold text-2xl text-red-800 my-3">
T(n) = n²
</div>

<p>
El crecimiento del trabajo es mucho más rápido conforme aumenta el tamaño de la entrada.
</p>

<div class="mt-3 bg-white rounded-lg border border-red-200 p-2 font-mono">
n = 1,000 → 1,000,000
</div>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-white text-center">

<p class="!text-white">
Para entradas pequeñas, las constantes y otros factores pueden hacer que un algoritmo con peor orden de crecimiento sea incluso más rápido.
</p>

<div class="mt-3 text-xl font-semibold text-amber-300">
Pero, para valores suficientemente grandes de n, el orden de crecimiento termina dominando el comportamiento.
</div>

</div>

---

# ¿El tamaño de la entrada determina todo?

<div class="mt-3 text-center">

<p>
Hasta ahora hemos expresado el costo de un algoritmo en función del <strong>tamaño de la entrada n</strong>.
</p>

<div class="mt-2 text-xl font-semibold text-amber-700">
Pero dos entradas del mismo tamaño pueden requerir cantidades muy diferentes de trabajo.
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-emerald-50 border border-emerald-200 text-center">

<div class="card-title text-emerald-800">
Mismo tamaño: n = 6
</div>

<div class="font-mono font-bold text-lg my-3">
[ 21, 8, 14, 5, 9, 3 ]
</div>

<p>
Buscamos <strong>21</strong>: aparece en la primera posición.
</p>

<div class="mt-3 bg-white rounded-lg border border-emerald-200 p-2 font-semibold">
1 comparación
</div>

</div>

<div class="card bg-red-50 border border-red-200 text-center">

<div class="card-title text-red-800">
Mismo tamaño: n = 6
</div>

<div class="font-mono font-bold text-lg my-3">
[ 21, 8, 14, 5, 9, 3 ]
</div>

<p>
Buscamos <strong>3</strong>: aparece en la última posición.
</p>

<div class="mt-3 bg-white rounded-lg border border-red-200 p-2 font-semibold">
6 comparaciones
</div>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
El costo no depende únicamente de <strong class="text-amber-300">cuántos datos</strong> recibimos, sino también de las <strong class="text-amber-300">características de esa entrada.</strong>
</p>

<div class="mt-3 text-xl font-semibold text-amber-300">
Entonces, ¿qué comportamiento de T(n) debemos analizar?
</div>

</div>


---

# Escenarios de análisis de complejidad

<div class="mt-3 text-center">

<p>
Para una entrada de tamaño <strong>n</strong>, un algoritmo puede presentar diferentes costos dependiendo de las características de los datos.
</p>

</div>

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="card bg-red-50 border border-red-200">

<div class="card-title text-red-800">
🔴 Peor caso · Worst-Case
</div>

<p>
Determina la <strong>cantidad máxima de recursos</strong> que puede requerir el algoritmo entre todas las entradas posibles de tamaño n.
</p>

</div>

<div class="card bg-emerald-50 border border-emerald-200">

<div class="card-title text-emerald-800">
🟢 Mejor caso · Best-Case
</div>

<p>
Determina la <strong>cantidad mínima de recursos</strong> requerida ante la entrada más favorable de tamaño n.
</p>

</div>

<div class="card bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">
🔵 Caso promedio · Average-Case
</div>

<p>
Estudia el <strong>comportamiento esperado</strong> considerando una distribución de probabilidad sobre las posibles entradas.
</p>

</div>

<div class="card bg-violet-50 border border-violet-200">

<div class="card-title text-violet-800">
🟣 Complejidad amortizada
</div>

<p>
Distribuye el costo de operaciones ocasionalmente costosas a lo largo de una <strong>secuencia completa de operaciones.</strong>
</p>

</div>

</div>

<div class="mt-5 p-3 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
Cada escenario responde una <strong class="text-amber-300">pregunta diferente sobre el comportamiento del algoritmo.</strong>
</p>

</div>

---

# Peor caso y mejor caso

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-red-50 border border-red-200">

<div class="card-title text-red-800">
🔴 Peor caso · Worst-Case
</div>

<p>
Representa el <strong>máximo costo</strong> que puede alcanzar el algoritmo para cualquier entrada de tamaño n.
</p>

<div class="mt-3 bg-white rounded-lg border border-red-200 p-3">

<div class="font-mono text-center font-bold">
[ 12, 7, 25, 9, 18, 4 ]
</div>

<div class="mt-2 text-center">
Buscar <strong>4</strong> → 6 comparaciones
</div>

</div>

<p class="mt-3">
Proporciona una <strong>garantía superior</strong>: ninguna entrada de ese tamaño requerirá más recursos que el límite establecido.
</p>

</div>

<div class="card bg-emerald-50 border border-emerald-200">

<div class="card-title text-emerald-800">
🟢 Mejor caso · Best-Case
</div>

<p>
Representa el <strong>mínimo costo</strong> posible ante la entrada más favorable de tamaño n.
</p>

<div class="mt-3 bg-white rounded-lg border border-emerald-200 p-3">

<div class="font-mono text-center font-bold">
[ 12, 7, 25, 9, 18, 4 ]
</div>

<div class="mt-2 text-center">
Buscar <strong>12</strong> → 1 comparación
</div>

</div>

<p class="mt-3">
Permite conocer el comportamiento más favorable, pero <strong>no garantiza el rendimiento</strong> ante entradas generales.
</p>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
El <strong class="text-red-300">peor caso</strong> es especialmente importante cuando necesitamos garantizar que un algoritmo no excederá cierto límite de recursos.
</p>

<div class="mt-2 text-amber-300 font-semibold">
Ej.: sistemas de tiempo real, equipos médicos o sistemas aeronáuticos.
</div>

</div>

---

# Caso promedio · Average-Case

<div class="mt-4 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center">

<p>
El caso promedio busca determinar el <strong>costo esperado</strong> del algoritmo considerando las diferentes entradas posibles de tamaño n.
</p>

<div class="mt-3 text-xl font-semibold text-blue-800">
No significa simplemente “sumar varios tiempos y dividir”.
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
🎲 Requiere un modelo probabilístico
</div>

<p>
Debemos establecer qué probabilidad tiene cada posible entrada o conjunto de entradas.
</p>

<p class="mt-3">
Por ejemplo, podríamos asumir que las distintas posiciones de un elemento buscado son <strong>igualmente probables.</strong>
</p>

</div>

<div class="card bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">
⚠️ La distribución importa
</div>

<p>
El resultado del análisis depende de que el modelo probabilístico utilizado represente razonablemente el comportamiento de los datos reales.
</p>

<p class="mt-3">
Si las entradas reales siguen otra distribución, el costo esperado calculado puede dejar de ser representativo.
</p>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
<strong class="text-blue-300">Average-Case</strong> responde:
</p>

<div class="mt-2 text-xl font-semibold text-amber-300">
¿Qué costo esperamos bajo una determinada distribución de entradas?
</div>

</div>

---

# Complejidad amortizada

<div class="mt-3 text-center">

<p>
En algunas estructuras dinámicas, la mayoría de las operaciones son baratas, pero <strong>ocasionalmente aparece una operación mucho más costosa.</strong>
</p>

</div>

<div class="mt-5 flex justify-center items-end gap-3">

<div class="text-center">
<div class="h-12 w-16 bg-emerald-100 border border-emerald-300 rounded-lg flex items-center justify-center font-bold">1</div>
<div class="mt-1 text-sm">barata</div>
</div>

<div class="text-center">
<div class="h-12 w-16 bg-emerald-100 border border-emerald-300 rounded-lg flex items-center justify-center font-bold">1</div>
<div class="mt-1 text-sm">barata</div>
</div>

<div class="text-center">
<div class="h-12 w-16 bg-emerald-100 border border-emerald-300 rounded-lg flex items-center justify-center font-bold">1</div>
<div class="mt-1 text-sm">barata</div>
</div>

<div class="text-center">
<div class="h-28 w-20 bg-red-100 border border-red-300 rounded-lg flex items-center justify-center font-bold text-red-800">COSTOSA</div>
<div class="mt-1 text-sm">ocasional</div>
</div>

<div class="text-center">
<div class="h-12 w-16 bg-emerald-100 border border-emerald-300 rounded-lg flex items-center justify-center font-bold">1</div>
<div class="mt-1 text-sm">barata</div>
</div>

<div class="text-center">
<div class="h-12 w-16 bg-emerald-100 border border-emerald-300 rounded-lg flex items-center justify-center font-bold">1</div>
<div class="mt-1 text-sm">barata</div>
</div>

</div>

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card bg-violet-50 border border-violet-200">

<div class="card-title text-violet-800">
La idea del “prepago”
</div>

<p>
Conceptualmente, las operaciones baratas pueden acumular <strong>crédito</strong> que permite cubrir el costo de una operación cara cuando esta ocurre.
</p>

</div>

<div class="card bg-slate-100 border border-slate-200">

<div class="card-title text-slate-800">
Una garantía sobre la secuencia
</div>

<p>
El costo total se analiza sobre una <strong>secuencia de n operaciones</strong>, distribuyendo entre ellas el efecto de las operaciones ocasionalmente costosas.
</p>

</div>

</div>

<div class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<p class="!text-white">
La complejidad amortizada proporciona una garantía <strong class="text-amber-300">determinista</strong>; no requiere asumir una distribución probabilística de las entradas.
</p>

</div>---

# Complejidad algorítmica · Conceptos clave

<div class="mt-3 text-center">
<p>
Analizar un algoritmo significa estudiar <strong>cómo escala el consumo de recursos</strong> conforme aumenta el tamaño del problema.
</p>
</div>

<div class="grid grid-cols-3 gap-4 mt-5">

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">
1. Modelo de cómputo
</div>
<p>
El modelo <strong>RAM</strong> establece supuestos comunes sobre ejecución, operaciones básicas y acceso a memoria para analizar algoritmos independientemente del hardware.
</p>
</div>

<div class="card bg-blue-50 border border-blue-200">
<div class="card-title text-blue-800">
2. Tamaño de la entrada
</div>
<p>
<strong>n</strong> representa el tamaño del problema, pero su significado depende de la entrada: elementos, bits o incluso múltiples parámetros como <strong>V</strong> y <strong>E</strong>.
</p>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="card-title text-violet-800">
3. Costo T(n)
</div>
<p>
Expresamos el trabajo requerido como una <strong>función del tamaño de la entrada</strong>, en lugar de depender del tiempo físico de una computadora particular.
</p>
</div>

<div class="card bg-emerald-50 border border-emerald-200">
<div class="card-title text-emerald-800">
4. Eficiencia asintótica
</div>
<p>
Cuando <strong>n crece</strong>, nos interesa la tendencia dominante: ignoramos coeficientes constantes y términos de menor orden.
</p>
</div>

<div class="card bg-orange-50 border border-orange-200">
<div class="card-title text-orange-800">
5. Orden de crecimiento
</div>
<p>
Permite caracterizar la <strong>escalabilidad</strong> del algoritmo y comparar cómo aumenta su costo para entradas suficientemente grandes.
</p>
</div>

<div class="card bg-slate-100 border border-slate-200">
<div class="card-title text-slate-800">
6. Escenarios de análisis
</div>
<p>
El comportamiento puede estudiarse como <strong>peor caso, mejor caso, caso promedio</strong> o mediante <strong>complejidad amortizada</strong>.
</p>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<div class="font-mono font-bold text-lg text-amber-300">
Entrada n → Costo T(n) → Crecimiento → Escalabilidad
</div>

<p class="!text-white mt-2">
La pregunta fundamental permanece: <strong>¿qué ocurre con el costo del algoritmo cuando el problema crece?</strong>
</p>

</div>