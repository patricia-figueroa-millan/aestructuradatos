---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
title: Algoritmia y Estructura de Datos
transition: slide-left
---

::: {.max-w-2xl .mx-auto .p-8 .rounded-2xl .bg-slate-900/80 .backdrop-blur-md .border .border-white/10 .shadow-2xl .text-white}
::: {.flex .flex-col .items-center .gap-1 .mb-5}
[Instituto Tecnológico de Colima]{.text-xs .font-mono .font-bold
.uppercase .tracking-widest .text-amber-400 .bg-amber-400/10 .px-3 .py-1
.rounded-full .border .border-amber-400/20} [Ingeniería en Inteligencia
Artificial]{.text-sm .text-slate-300 .font-medium}
:::

```{=html}
<h1 class="text-4xl font-black tracking-tight bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent !leading-tight mb-2">
```
Algoritmia y Estructura de Datos
```{=html}
</h1>
```
::: {.mt-3 .mb-5}
::: {.text-xl .font-semibold .text-amber-300 .tracking-tight}
1.2 Complejidad Algorítmica
:::
:::

::: {.mt-6 .pt-5 .border-t .border-white/10 .flex .flex-col .items-center .gap-1}
[Catedrática]{.text-xs .font-mono .font-bold .uppercase .tracking-wider
.text-slate-400}

::: {.text-lg .font-bold .text-white .mb-3}
Dra. Patricia Elizabeth Figueroa Millán
:::

::: {.flex .flex-wrap .justify-center .items-center .gap-3 .text-xs .font-mono .text-slate-300}
[correo: patricia.figueroa@colima.tecnm.mx]{.bg-white/10 .px-3 .py-1.5
.rounded-lg .border .border-white/10} [instagram:
@patricia.figueroa.tecnm.mx]{.bg-white/10 .px-3 .py-1.5 .rounded-lg
.border .border-white/10}
:::
:::
:::

------------------------------------------------------------------------

# Introducción a la Complejidad Computacional

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
✓ Correcto no siempre significa eficiente
:::

```{=html}
<p>
```
Un programa debe producir los `<strong>`{=html}resultados
esperados`</strong>`{=html}, pero también debe hacerlo utilizando los
recursos computacionales de manera eficiente.
```{=html}
</p>
```
```{=html}
<p class="mt-3">
```
La `<strong>`{=html}complejidad computacional`</strong>`{=html} ---o
complejidad algorítmica--- estudia cómo cambia el consumo de recursos de
un algoritmo cuando aumenta el tamaño del problema.
```{=html}
</p>
```
:::

::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
📈 El problema aparece cuando los datos crecen
:::

```{=html}
<p>
```
Las computadoras actuales realizan cálculos rápidamente, pero esto no
compensa necesariamente un algoritmo ineficiente.
```{=html}
</p>
```
```{=html}
<p class="mt-3">
```
Con grandes volúmenes de datos, un algoritmo puede requerir cantidades
excesivas de `<strong>`{=html}tiempo`</strong>`{=html} o
`<strong>`{=html}memoria`</strong>`{=html}, incluso sobre hardware
potente.
```{=html}
</p>
```
:::
:::

::: {.mt-5 .p-4 .rounded-xl .bg-slate-900 .border .border-slate-700}
::: {.font-bold .text-amber-300 .mb-2}
La complejidad permite anticipar el comportamiento
:::

```{=html}
<p class="!text-white">
```
El análisis algorítmico permite estimar cómo se comportará una solución
al escalar el problema, comparar alternativas y tomar decisiones de
diseño fundamentadas.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# La pregunta central de la complejidad

::: {.mt-5 .p-5 .rounded-2xl .bg-gradient-to-r .from-amber-50 .to-orange-50 .border .border-amber-200}
::: {.text-center .text-2xl .font-semibold .text-slate-800 .leading-snug}
A medida que aumenta el tamaño de los datos de entrada,`<br>`{=html}
[¿cómo cambia el comportamiento del algoritmo?]{.text-amber-700}
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
🚫 No buscamos medir solo segundos
:::

```{=html}
<p>
```
El tiempo físico depende del procesador, memoria, sistema operativo,
lenguaje, compilador y entorno de ejecución.
```{=html}
</p>
```
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
✓ Analizamos el crecimiento
:::

```{=html}
<p>
```
Estudiamos cómo aumenta la cantidad de operaciones o la memoria
necesaria cuando crece la entrada.
```{=html}
</p>
```
::: {.mt-4 .text-center}
[n → tamaño de la entrada]{.font-mono .font-bold .text-xl
.text-amber-800 .bg-white .px-4 .py-2 .rounded-lg .border
.border-amber-200}
:::
:::
:::

::: {.mt-5 .text-center .text-lg .font-semibold .text-slate-700}
El objetivo es entender [cómo escala el costo
computacional.]{.text-amber-700}
:::

------------------------------------------------------------------------

# ¿Cómo podemos comparar algoritmos?

::: {.mt-5 .text-center}
```{=html}
<p class="text-lg">
```
Si el tiempo de ejecución depende de la computadora utilizada...
```{=html}
</p>
```
::: {.text-2xl .font-semibold .text-amber-700 .mt-2}
¿cómo analizamos la eficiencia de manera independiente del hardware?
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-6}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
⏱️ Medir el tiempo de ejecución
:::

```{=html}
<p>
```
Indica cuánto tardó una implementación concreta bajo determinadas
condiciones.
```{=html}
</p>
```
::: {.mt-3 .font-mono .text-center .text-slate-600}
algoritmo + hardware + software → segundos
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
🔍 Analizar el algoritmo
:::

```{=html}
<p>
```
Busca determinar cuántas operaciones requiere y cómo aumenta ese trabajo
cuando crece la entrada.
```{=html}
</p>
```
::: {.mt-3 .font-mono .text-center .text-amber-800}
tamaño n → número de operaciones
:::
:::
:::

::: {.mt-6 .p-4 .rounded-xl .bg-slate-900 .border .border-slate-700 .text-center}
```{=html}
<p class="!text-white">
```
Para comparar algoritmos necesitamos establecer
`<strong class="text-amber-300">`{=html}qué operaciones contamos y qué
costo asumimos para ellas.`</strong>`{=html}
```{=html}
</p>
```
::: {.mt-3 .text-xl .font-semibold .text-amber-300}
→ Necesitamos un modelo de cómputo
:::
:::

------------------------------------------------------------------------

# El modelo de cómputo estándar: RAM

::: {.grid .grid-cols-5 .gap-5 .mt-5 .items-stretch}
::: {.col-span-3 .card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
¿Por qué necesitamos un modelo?
:::

```{=html}
<p>
```
Para predecir y comparar rigurosamente la eficiencia necesitamos
establecer `<strong>`{=html}condiciones comunes de
análisis`</strong>`{=html}.
```{=html}
</p>
```
```{=html}
<p class="mt-3">
```
No sería práctico que nuestras conclusiones dependieran de la
arquitectura particular de una CPU.
```{=html}
</p>
```
:::

::: {.col-span-2 .card .bg-amber-50 .border .border-amber-200 .flex .flex-col .justify-center .text-center}
::: {.text-sm .font-mono .font-bold .uppercase .tracking-wider .text-amber-700}
Modelo teórico estándar
:::

::: {.text-2xl .font-bold .text-slate-800 .mt-2}
RAM
:::

::: {.text-lg .font-semibold .text-amber-800}
Random-Access Machine
:::

::: {.mt-3 .text-slate-600}
Máquina de Acceso Aleatorio
:::
:::
:::

::: {.mt-5 .p-4 .rounded-xl .bg-slate-900 .border .border-slate-700}
::: {.font-bold .text-amber-300 .mb-2}
Una abstracción para analizar algoritmos
:::

```{=html}
<p class="!text-white">
```
Representa una computadora
`<strong>`{=html}monoprocesador`</strong>`{=html} idealizada y fija
reglas sobre instrucciones, costo de operaciones y acceso a memoria.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# Modelo RAM: ejecución y operaciones básicas

```{=html}
<div class="grid grid-cols-2 gap-5 mt-4">
```
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
1.  Ejecución secuencial
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    Las instrucciones se ejecutan `<strong>`{=html}una después de
    otra`</strong>`{=html}.
    ```{=html}
    </p>
    ```
    ```{=html}
    <div class="mt-4 flex justify-center items-center gap-2 font-mono font-bold text-slate-700">
    ```
    [I₁]{.bg-white .border .border-slate-300 .px-3 .py-2 .rounded-lg}→
    [I₂]{.bg-white .border .border-slate-300 .px-3 .py-2 .rounded-lg}→
    [I₃]{.bg-white .border .border-slate-300 .px-3 .py-2 .rounded-lg}→
    ...
:::

::: {.mt-4 .text-center .text-slate-600 .font-semibold}
Sin concurrencia · Sin paralelismo
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
2.  Costo constante
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    Cada instrucción básica o
    `<strong>`{=html}primitiva`</strong>`{=html} se considera de costo
    constante.
    ```{=html}
    </p>
    ```
    ::: {.mt-4 .text-center}
    [1 primitiva → costo constante]{.font-mono .font-bold
    .text-amber-800 .bg-white .px-4 .py-2 .rounded-lg .border
    .border-amber-200}
    :::
:::
:::

::: {.mt-4 .mb-2 .font-semibold .text-slate-700}
¿Qué consideramos una operación básica?
:::

::: {.grid .grid-cols-3 .gap-4}
::: {.card .bg-blue-50 .border .border-blue-200 .text-center}
::: {.card-title .text-blue-800}
Aritmética
:::

```{=html}
<p>
```
Suma, resta, multiplicación, división, residuo,
`<em>`{=html}floor`</em>`{=html} y `<em>`{=html}ceiling`</em>`{=html}.
```{=html}
</p>
```
:::

::: {.card .bg-emerald-50 .border .border-emerald-200 .text-center}
::: {.card-title .text-emerald-800}
Movimiento de datos
:::

```{=html}
<p>
```
Copiar, cargar (`<em>`{=html}load`</em>`{=html}) y almacenar
(`<em>`{=html}store`</em>`{=html}).
```{=html}
</p>
```
:::

::: {.card .bg-violet-50 .border .border-violet-200 .text-center}
::: {.card-title .text-violet-800}
Control
:::

```{=html}
<p>
```
Bifurcaciones, llamadas a subrutinas y retornos.
```{=html}
</p>
```
:::
:::

------------------------------------------------------------------------

# Modelo RAM: acceso uniforme a memoria

```{=html}
<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200">
```
::: {.card-title .text-amber-800}
3.  Acceso uniforme a memoria
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    Recuperar o almacenar un valor en `<strong>`{=html}cualquier
    posición de memoria`</strong>`{=html} requiere una cantidad
    constante de tiempo.
    ```{=html}
    </p>
    ```
:::

::: mt-4
::: {.grid .grid-cols-6 .gap-2 .text-center .font-mono}
<div>

::: {.text-slate-500 .mb-1}
0
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
17
:::

</div>

<div>

::: {.text-slate-500 .mb-1}
1
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
8
:::

</div>

<div>

::: {.text-slate-500 .mb-1}
2
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
31
:::

</div>

<div>

::: {.text-slate-500 .mb-1}
3
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
4
:::

</div>

<div>

::: {.text-slate-500 .mb-1}
...
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
...
:::

</div>

<div>

::: {.text-slate-500 .mb-1}
n−1
:::

::: {.bg-white .border-2 .border-amber-300 .rounded-lg .p-2 .font-bold}
9
:::

</div>
:::

::: {.mt-3 .text-center}
[Cualquier posición → mismo costo de acceso]{.inline-block .font-mono
.font-bold .text-amber-800 .bg-amber-50 .px-4 .py-2 .rounded-lg .border
.border-amber-200}
:::
:::

::: {.grid .grid-cols-2 .gap-4 .mt-4}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
¿Qué supone?
:::

```{=html}
<p>
```
El costo de acceso `<strong>`{=html}no depende de la
ubicación`</strong>`{=html} de la dirección.
```{=html}
</p>
```
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
Ejemplo: arreglo
:::

```{=html}
<p>
```
Conocido el índice, accedemos directamente sin recorrer elementos
anteriores.
```{=html}
</p>
```
:::
:::

------------------------------------------------------------------------

# Modelo RAM: representación de datos acotada

```{=html}
<div class="mt-3 p-3 rounded-xl bg-slate-100 border border-slate-200">
```
::: {.card-title .text-slate-800}
4.  Representación de datos acotada
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    El modelo RAM no supone celdas capaces de almacenar información
    ilimitada. Los enteros se representan mediante
    `<strong>`{=html}palabras de tamaño acotado`</strong>`{=html}.
    ```{=html}
    </p>
    ```
:::

::: {.grid .grid-cols-5 .gap-4 .mt-4 .items-center}
::: {.col-span-2 .text-center}
::: {.inline-block .bg-amber-50 .border-2 .border-amber-200 .rounded-2xl .px-7 .py-4}
::: {.font-semibold .text-amber-700 .mb-2}
Tamaño de una palabra
:::

::: {.font-mono .font-bold .text-2xl .text-slate-800}
c log₂ n bits
:::

::: {.mt-1 .font-mono .text-slate-600}
c ≥ 1
:::
:::
:::

::: col-span-3
```{=html}
<p>
```
Debe ser suficiente para `<strong>`{=html}representar el tamaño de la
entrada n`</strong>`{=html} y direccionar la memoria necesaria.
```{=html}
</p>
```
:::
:::

::: {.grid .grid-cols-2 .gap-4 .mt-4}
::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.card-title .text-emerald-800}
✓ Permite
:::

```{=html}
<p>
```
Representar valores y direcciones suficientemente grandes para trabajar
con la entrada.
```{=html}
</p>
```
:::

::: {.card .bg-red-50 .border .border-red-200}
::: {.card-title .text-red-800}
✗ Evita
:::

```{=html}
<p>
```
Suponer que una palabra puede almacenar cantidades arbitrariamente
grandes.
```{=html}
</p>
```
:::
:::

------------------------------------------------------------------------

# ¿De qué depende el costo de un algoritmo?

::: {.mt-2 .text-center}
```{=html}
<p>
```
El modelo RAM establece qué operaciones consideramos básicas y qué costo
asumimos para ellas.
```{=html}
</p>
```
::: {.mt-2 .text-xl .font-semibold .text-amber-700}
Pero... ¿un algoritmo realiza siempre la misma cantidad de operaciones?
:::
:::

::: {.grid .grid-cols-3 .gap-4 .mt-4 .items-center}
::: {.card .bg-slate-100 .border .border-slate-200 .text-center}
::: {.card-title .text-slate-800}
Entrada pequeña
:::

::: {.font-mono .text-xl .font-bold .text-slate-700 .my-2}
\[ 8, 3, 5 \]
:::

```{=html}
<p>
```
Pocos datos que procesar.
```{=html}
</p>
```
:::

::: text-center
::: {.text-4xl .font-bold .text-amber-600}
→
:::

::: {.mt-1 .font-semibold .text-slate-600}
La entrada crece
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200 .text-center}
::: {.card-title .text-amber-800}
Entrada grande
:::

::: {.font-mono .text-xl .font-bold .text-amber-800 .my-2}
\[ 8, 3, 5, ..., 21 \]
:::

```{=html}
<p>
```
Más datos pueden implicar más operaciones y recursos.
```{=html}
</p>
```
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .border .border-slate-700 .text-center}
```{=html}
<p class="!text-white">
```
Necesitamos expresar el costo en función del
`<strong class="text-amber-300">`{=html}tamaño del
problema.`</strong>`{=html}
```{=html}
</p>
```
::: mt-2
[n = tamaño de la entrada]{.inline-block .font-mono .font-bold .text-xl
.text-amber-300 .bg-white/10 .px-4 .py-1.5 .rounded-lg .border
.border-white/10}
:::
:::

------------------------------------------------------------------------

# El tamaño de la entrada: n

::: {.mt-4 .p-4 .rounded-xl .bg-amber-50 .border .border-amber-200 .text-center}
```{=html}
<p>
```
El costo se expresa en función del `<strong>`{=html}tamaño de la
entrada`</strong>`{=html}.
```{=html}
</p>
```
::: mt-3
[n]{.inline-block .font-mono .font-bold .text-3xl .text-amber-800
.bg-white .px-5 .py-2 .rounded-xl .border .border-amber-200}
:::
:::

::: {.mt-4 .text-center .font-semibold .text-slate-700}
Pero [n no significa siempre "número de elementos".]{.text-amber-700}
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
🔎 Ordenación y búsqueda
:::

```{=html}
<p>
```
`<strong>`{=html}n = número de elementos`</strong>`{=html} de la lista o
arreglo.
```{=html}
</p>
```
::: {.mt-4 .text-center .font-mono}
[14]{.bg-white .border .px-3 .py-2 .rounded} [7]{.bg-white .border .px-3
.py-2 .rounded} [21]{.bg-white .border .px-3 .py-2 .rounded}
[3]{.bg-white .border .px-3 .py-2 .rounded} [9]{.bg-white .border .px-3
.py-2 .rounded}

::: {.mt-3 .font-bold}
n = 5
:::
:::
:::

::: {.card .bg-blue-50 .border .border-blue-200}
::: {.card-title .text-blue-800}
🔢 Problemas numéricos
:::

```{=html}
<p>
```
El tamaño puede medirse mediante el `<strong>`{=html}número de
bits`</strong>`{=html} necesarios para representar la información.
```{=html}
</p>
```
::: {.mt-4 .text-center}
::: {.font-mono .font-bold .text-xl .text-blue-800 .bg-white .border .border-blue-200 .rounded-lg .px-4 .py-2 .inline-block}
11010110
:::

::: {.mt-3 .font-mono .font-bold .text-blue-800}
n = 8 bits
:::
:::
:::
:::

------------------------------------------------------------------------

# Cuando una sola variable no es suficiente

::: {.mt-4 .text-center}
```{=html}
<p>
```
Algunas entradas no pueden describirse adecuadamente mediante un único
valor n.
```{=html}
</p>
```
::: {.text-xl .font-semibold .text-amber-700 .mt-2}
Los grafos son un ejemplo importante.
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
🌐 Problemas sobre grafos
:::

```{=html}
<p>
```
Utilizamos simultáneamente:
```{=html}
</p>
```
::: {.mt-4 .space-y-3}
::: {.bg-white .border .rounded-lg .p-3}
[V]{.font-mono .font-bold .text-xl .text-amber-700}[número de vértices o
nodos]{.ml-2 .font-semibold}
:::

::: {.bg-white .border .rounded-lg .p-3}
[E]{.font-mono .font-bold .text-xl .text-amber-700}[número de aristas o
conexiones]{.ml-2 .font-semibold}
:::
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200 .text-center}
::: {.card-title .text-amber-800}
Ejemplo
:::

::: {.font-mono .text-2xl .my-5}
A ─ B ─ C`<br>`{=html}│ ╲ │ ╱ │`<br>`{=html}D ─── E
:::

[\|V\| = 5    \|E\| = 6]{.font-mono .font-bold .text-lg .text-amber-800
.bg-white .px-4 .py-2 .rounded-lg .border .border-amber-200}
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
La medida debe reflejar las
`<strong class="text-amber-300">`{=html}características relevantes del
problema.`</strong>`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# ¿De dónde sale el costo?

::: {.mt-2 .text-center}
```{=html}
<p>
```
Contamos las `<strong>`{=html}operaciones básicas`</strong>`{=html}
realizadas según el modelo RAM.
```{=html}
</p>
```
:::

::: {.grid .grid-cols-5 .gap-4 .mt-4}
::: {.col-span-2 .card .bg-violet-50 .border .border-violet-200}
::: {.card-title .text-violet-800}
Ejemplo sencillo
:::

```{=html}
<p>
```
Recorrer un arreglo y procesar cada elemento:
```{=html}
</p>
```
::: {.mt-3 .bg-white .rounded-lg .border .border-violet-200 .p-3 .font-mono}
para i = 1 hasta n:`<br>`{=html}  leer dato\[i\]`<br>`{=html}  mostrar
dato\[i\]
:::
:::

::: {.col-span-3 .card .bg-blue-50 .border .border-blue-200}
::: {.card-title .text-blue-800}
Por cada elemento
:::

::: {.grid .grid-cols-3 .gap-2 .text-center .mt-3}
::: {.bg-white .p-2 .rounded-lg}
`<strong>`{=html}leer`</strong>`{=html}`<br>`{=html}1 operación
:::

::: {.text-2xl .font-bold}
\+
:::

::: {.bg-white .p-2 .rounded-lg}
`<strong>`{=html}mostrar`</strong>`{=html}`<br>`{=html}1 operación
:::
:::

::: {.mt-3 .text-center .font-bold .text-blue-800}
2 operaciones por elemento
:::
:::
:::

::: {.mt-4 .flex .items-center .justify-center .gap-4}
::: {.font-mono .text-xl .bg-amber-50 .border .border-amber-200 .rounded-lg .px-5 .py-2}
2 × n = 2n operaciones
:::

::: {.text-2xl .font-bold}
→
:::

::: {.font-mono .text-2xl .font-bold .text-violet-800}
T(n) = 2n
:::
:::

::: {.mt-4 .text-center .font-semibold .text-slate-700}
El costo se expresa como una [función del tamaño de la entrada:
T(n).]{.text-violet-700}
:::

------------------------------------------------------------------------

# ¿Qué son las constantes?

::: {.mt-1 .text-center}
```{=html}
<p>
```
Supongamos que el algoritmo anterior realiza además `<strong>`{=html}3
operaciones fijas`</strong>`{=html} antes del ciclo.
```{=html}
</p>
```
::: {.mt-2 .font-mono .text-3xl .font-bold}
T(n) = [2n]{.text-blue-700} + [3]{.text-violet-700}
:::
:::

```{=html}
<div class="grid grid-cols-2 gap-4 mt-3">
```
```{=html}
<div class="card bg-blue-50 border border-blue-200">
```
::: {.card-title .text-blue-800}
1.  Factor constante: 2
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    El `<strong>`{=html}2`</strong>`{=html} se multiplica por n, pero su
    valor permanece fijo.
    ```{=html}
    </p>
    ```
    ::: {.mt-2 .bg-white .border .border-blue-200 .rounded-xl .p-2 .text-center}
    ::: {.font-mono .text-xl .font-bold .text-blue-800}
    2 × n = 2n
    :::

    ::: mt-1
    2 operaciones por cada elemento.
    :::
    :::

    ```{=html}
    <p class="mt-2">
    ```
    Es constante porque `<strong>`{=html}siempre son 2 operaciones por
    elemento`</strong>`{=html}.
    ```{=html}
    </p>
    ```
:::

::: {.card .bg-violet-50 .border .border-violet-200}
::: {.card-title .text-violet-800}
2.  Término constante: 3
    ```{=html}
    </div>
    ```
    ```{=html}
    <p>
    ```
    El `<strong>`{=html}3`</strong>`{=html} no depende de n: representa
    operaciones realizadas una cantidad fija de veces.
    ```{=html}
    </p>
    ```
    ::: {.mt-2 .bg-white .border .border-violet-200 .rounded-xl .p-2 .text-center}
    ::: {.font-bold .text-violet-700}
    3 operaciones fijas
    :::

    ::: mt-1
    Ej.: inicializar variables o preparar datos.
    :::
    :::

    ```{=html}
    <p class="mt-2">
    ```
    Es constante porque `<strong>`{=html}no cambia aunque cambie
    n`</strong>`{=html}.
    ```{=html}
    </p>
    ```
:::
:::

::: {.mt-3 .p-3 .rounded-xl .bg-amber-50 .border .border-amber-200 .text-center}
```{=html}
<p>
```
Ambas afectan el costo real, pero `<strong>`{=html}su valor no cambia
cuando cambia n.`</strong>`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# ¿Qué ocurre cuando n crece?

::: {.mt-2 .text-center}
```{=html}
<p>
```
Observemos `<strong>`{=html}T(n) = 2n + 3`</strong>`{=html} conforme
aumenta la entrada.
```{=html}
</p>
```
:::

::: {.grid .grid-cols-5 .gap-4 .mt-4}
::: {.col-span-2 .card .bg-violet-50 .border .border-violet-200}
::: {.card-title .text-violet-800}
Función de costo
:::

::: {.font-mono .text-3xl .font-bold .text-center .my-3}
T(n) = 2n + 3
:::

```{=html}
<p>
```
`<strong class="text-blue-700">`{=html}2n`</strong>`{=html} crece con n.
```{=html}
</p>
```
```{=html}
<p class="mt-2">
```
`<strong class="text-violet-700">`{=html}3`</strong>`{=html} permanece
igual.
```{=html}
</p>
```
:::

::: col-span-3
```{=html}
<table class="w-full text-center border-collapse">
```
```{=html}
<thead>
```
```{=html}
<tr class="bg-violet-800 text-white">
```
```{=html}
<th class="p-2">
```
n
```{=html}
</th>
```
```{=html}
<th class="p-2">
```
2n
```{=html}
</th>
```
```{=html}
<th class="p-2">
```
3
```{=html}
</th>
```
```{=html}
<th class="p-2">
```
T(n)
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
</thead>
```
```{=html}
<tbody>
```
```{=html}
<tr>
```
```{=html}
<td class="p-2 border">
```
10
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
20
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
3
```{=html}
</td>
```
```{=html}
<td class="p-2 border font-bold">
```
23
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td class="p-2 border">
```
100
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
200
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
3
```{=html}
</td>
```
```{=html}
<td class="p-2 border font-bold">
```
203
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td class="p-2 border">
```
1,000
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
2,000
```{=html}
</td>
```
```{=html}
<td class="p-2 border">
```
3
```{=html}
</td>
```
```{=html}
<td class="p-2 border font-bold">
```
2,003
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</tbody>
```
```{=html}
</table>
```
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
Al aumentar n, `<strong class="text-amber-300">`{=html}2n domina el
comportamiento de T(n)`</strong>`{=html}, mientras el efecto relativo
del 3 disminuye.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# Del costo al crecimiento asintótico

::: {.mt-4 .text-center}
```{=html}
<p>
```
Ya podemos expresar el trabajo mediante una función del tamaño de
entrada.
```{=html}
</p>
```
::: {.mt-3 .text-2xl .font-semibold .text-amber-700}
Ahora cambia nuestra pregunta.
:::
:::

::: {.grid .grid-cols-3 .gap-4 .mt-6 .items-center}
::: {.card .bg-slate-100 .border .border-slate-200 .text-center}
::: {.card-title .text-slate-800}
Entrada
:::

::: {.my-3 .font-mono .font-bold .text-3xl .text-slate-700}
n
:::

```{=html}
<p>
```
¿Cuánto debe procesar?
```{=html}
</p>
```
:::

::: text-center
::: {.text-4xl .font-bold .text-amber-600}
→
:::

::: {.mt-2 .font-semibold .text-slate-600}
produce un costo
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200 .text-center}
::: {.card-title .text-amber-800}
Costo
:::

::: {.my-3 .font-mono .font-bold .text-3xl .text-amber-800}
T(n)
:::

```{=html}
<p>
```
¿Cuánto trabajo requiere?
```{=html}
</p>
```
:::
:::

::: {.mt-6 .p-4 .rounded-xl .bg-slate-900 .border .border-slate-700 .text-center}
```{=html}
<p class="!text-white">
```
¿Qué tan rápido crece
`<strong class="text-amber-300">`{=html}T(n)`</strong>`{=html} cuando n
se hace cada vez más grande?
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# Eficiencia asintótica

::: {.mt-4 .p-5 .rounded-xl .bg-amber-50 .border .border-amber-200 .text-center}
```{=html}
<p>
```
Nos concentramos en el comportamiento cuando el `<strong>`{=html}tamaño
de la entrada crece considerablemente`</strong>`{=html}.
```{=html}
</p>
```
::: {.mt-3 .inline-block .bg-white .border .border-amber-200 .rounded-xl .px-6 .py-3}
::: {.font-mono .font-bold .text-2xl .text-amber-800}
n → ∞
:::
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
🔬 En pequeña escala
:::

```{=html}
<p>
```
Inicialización, constantes y pequeñas diferencias pueden influir
apreciablemente.
```{=html}
</p>
```
::: {.mt-4 .text-center .font-mono .text-slate-600}
n pequeño → los detalles importan
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
📈 A gran escala
:::

```{=html}
<p>
```
Cuando `<strong>`{=html}n crece`</strong>`{=html}, esos detalles pierden
relevancia frente a la tendencia.
```{=html}
</p>
```
::: {.mt-4 .text-center .font-mono .font-bold .text-amber-800}
n grande → domina el crecimiento
:::
:::
:::

------------------------------------------------------------------------

# ¿Cómo expresamos el crecimiento de T(n)?

::: {.mt-2 .text-center}
```{=html}
<p>
```
En el análisis asintótico interesa el `<strong>`{=html}patrón de
crecimiento`</strong>`{=html}.
```{=html}
</p>
```
:::

::: {.mt-4 .p-3 .rounded-xl .bg-violet-50 .border .border-violet-200 .text-center}
::: {.font-mono .text-2xl .font-bold}
T(n) = 2n + 3
:::
:::

::: {.grid .grid-cols-4 .gap-3 .mt-4}
::: {.card .bg-slate-100 .border .border-slate-200 .text-center}
::: {.font-bold .text-violet-800}
1
:::

```{=html}
<p>
```
Partimos de la función.
```{=html}
</p>
```
::: {.font-mono .font-bold .mt-2}
2n + 3
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200 .text-center}
::: {.font-bold .text-violet-800}
2
:::

```{=html}
<p>
```
El término constante no determina el crecimiento.
```{=html}
</p>
```
::: {.font-mono .font-bold .mt-2}
2n
:::
:::

::: {.card .bg-blue-50 .border .border-blue-200 .text-center}
::: {.font-bold .text-violet-800}
3
:::

```{=html}
<p>
```
El factor constante tampoco cambia el orden.
```{=html}
</p>
```
::: {.font-mono .font-bold .mt-2}
n
:::
:::

::: {.card .bg-violet-50 .border .border-violet-200 .text-center}
::: {.font-bold .text-violet-800}
4
:::

```{=html}
<p>
```
El crecimiento es lineal.
```{=html}
</p>
```
::: {.font-mono .font-bold .text-xl .mt-2}
O(n)
:::
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
No afirmamos que `<strong>`{=html}2n + 3 = n`</strong>`{=html}. Decimos
que `<strong class="text-amber-300">`{=html}2n + 3 crece linealmente con
n`</strong>`{=html}.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# ¿Qué ocurre con términos de distinto orden?

::: {.mt-3 .text-center}
```{=html}
<p>
```
Cuando una función contiene varios términos, conservamos el que
`<strong>`{=html}crece más rápido`</strong>`{=html}.
```{=html}
</p>
```
:::

::: {.mt-4 .text-center}
::: {.inline-block .bg-slate-100 .border .border-slate-200 .rounded-xl .px-7 .py-3}
[T(n) = 3n² + 10n + 50]{.font-mono .font-bold .text-2xl .text-slate-800}
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
Coeficiente constante
:::

```{=html}
<p>
```
El factor `<strong>`{=html}3`</strong>`{=html} afecta el costo real,
pero no cambia el patrón cuadrático.
```{=html}
</p>
```
::: {.mt-4 .text-center .font-mono .font-bold .text-lg}
[3]{.text-slate-400 .line-through}[n²]{.text-amber-700}
:::
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
Término dominante
:::

```{=html}
<p>
```
Para n grande, `<strong>`{=html}n²`</strong>`{=html} crece más rápido
que n y que una constante.
```{=html}
</p>
```
::: {.mt-4 .text-center .font-mono .font-bold .text-lg}
[n²]{.text-amber-800}[ + ]{.text-slate-400}[10n + 50]{.text-slate-400
.line-through}
:::
:::
:::

::: {.mt-5 .p-3 .rounded-xl .bg-slate-900 .text-center}
::: {.font-mono .font-bold .text-xl .text-white}
3n² + 10n + 50 [→]{.text-amber-300 .mx-3} n² [→]{.text-amber-300 .mx-3}
O(n²)
:::
:::

------------------------------------------------------------------------

# El orden de crecimiento importa

::: {.mt-3 .text-center}
```{=html}
<p>
```
Dos algoritmos pueden resolver correctamente el mismo problema y verse
similares para entradas pequeñas.
```{=html}
</p>
```
::: {.mt-2 .text-xl .font-semibold .text-amber-700}
La diferencia aparece cuando el problema escala.
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-emerald-50 .border .border-emerald-200 .text-center}
::: {.card-title .text-emerald-800}
Algoritmo A
:::

::: {.font-mono .font-bold .text-2xl .text-emerald-800 .my-3}
T(n) = n
:::

```{=html}
<p>
```
El trabajo crece proporcionalmente.
```{=html}
</p>
```
::: {.mt-3 .bg-white .rounded-lg .border .border-emerald-200 .p-2 .font-mono}
n = 1,000 → 1,000
:::
:::

::: {.card .bg-red-50 .border .border-red-200 .text-center}
::: {.card-title .text-red-800}
Algoritmo B
:::

::: {.font-mono .font-bold .text-2xl .text-red-800 .my-3}
T(n) = n²
:::

```{=html}
<p>
```
El trabajo crece mucho más rápido.
```{=html}
</p>
```
::: {.mt-3 .bg-white .rounded-lg .border .border-red-200 .p-2 .font-mono}
n = 1,000 → 1,000,000
:::
:::
:::

::: {.mt-5 .p-4 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
Un mejor `<strong class="text-amber-300">`{=html}orden de
crecimiento`</strong>`{=html} suele ofrecer mayor escalabilidad para
entradas suficientemente grandes.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# ¿El mismo n implica siempre el mismo costo?

::: {.mt-4 .text-center}
```{=html}
<p>
```
No necesariamente. Dos entradas con el `<strong>`{=html}mismo tamaño
n`</strong>`{=html} pueden provocar cantidades distintas de trabajo.
```{=html}
</p>
```
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-emerald-50 .border .border-emerald-200 .text-center}
::: {.card-title .text-emerald-800}
Entrada favorable
:::

::: {.font-mono .font-bold .my-3}
\[ 12, 7, 25, 9, 18, 4 \]
:::

```{=html}
<p>
```
Buscar `<strong>`{=html}12`</strong>`{=html}
```{=html}
</p>
```
::: {.mt-2 .font-bold .text-emerald-800}
1 comparación
:::
:::

::: {.card .bg-red-50 .border .border-red-200 .text-center}
::: {.card-title .text-red-800}
Entrada desfavorable
:::

::: {.font-mono .font-bold .my-3}
\[ 12, 7, 25, 9, 18, 4 \]
:::

```{=html}
<p>
```
Buscar `<strong>`{=html}4`</strong>`{=html}
```{=html}
</p>
```
::: {.mt-2 .font-bold .text-red-800}
6 comparaciones
:::
:::
:::

::: {.mt-5 .p-4 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
Mismo tamaño: `<strong class="text-amber-300">`{=html}n =
6`</strong>`{=html}. Distinto costo.
```{=html}
</p>
```
::: {.mt-2 .text-amber-300 .font-semibold}
→ Necesitamos escenarios de análisis.
:::
:::

------------------------------------------------------------------------

# Escenarios de análisis de complejidad

::: {.grid .grid-cols-2 .gap-4 .mt-4}
::: {.card .bg-red-50 .border .border-red-200}
::: {.card-title .text-red-800}
🔴 Peor caso · Worst-Case
:::

```{=html}
<p>
```
Cantidad `<strong>`{=html}máxima de recursos`</strong>`{=html} para
cualquier entrada de tamaño n.
```{=html}
</p>
```
:::

::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.card-title .text-emerald-800}
🟢 Mejor caso · Best-Case
:::

```{=html}
<p>
```
Cantidad `<strong>`{=html}mínima de recursos`</strong>`{=html} ante la
entrada más favorable.
```{=html}
</p>
```
:::

::: {.card .bg-blue-50 .border .border-blue-200}
::: {.card-title .text-blue-800}
🔵 Caso promedio · Average-Case
:::

```{=html}
<p>
```
`<strong>`{=html}Costo esperado`</strong>`{=html} bajo una distribución
de probabilidad de las entradas.
```{=html}
</p>
```
:::

::: {.card .bg-violet-50 .border .border-violet-200}
::: {.card-title .text-violet-800}
🟣 Complejidad amortizada
:::

```{=html}
<p>
```
Distribuye operaciones ocasionalmente costosas a lo largo de una
`<strong>`{=html}secuencia`</strong>`{=html}.
```{=html}
</p>
```
:::
:::

::: {.mt-5 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
Cada escenario responde una
`<strong class="text-amber-300">`{=html}pregunta diferente sobre el
comportamiento del algoritmo.`</strong>`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# Peor caso y mejor caso

::: {.grid .grid-cols-2 .gap-5 .mt-4}
::: {.card .bg-red-50 .border .border-red-200}
::: {.card-title .text-red-800}
🔴 Peor caso · Worst-Case
:::

```{=html}
<p>
```
Representa el `<strong>`{=html}máximo costo`</strong>`{=html} para
cualquier entrada de tamaño n.
```{=html}
</p>
```
::: {.mt-3 .bg-white .rounded-lg .border .border-red-200 .p-3}
::: {.font-mono .text-center .font-bold}
\[ 12, 7, 25, 9, 18, 4 \]
:::

::: {.mt-2 .text-center}
Buscar `<strong>`{=html}4`</strong>`{=html} → 6 comparaciones
:::
:::

```{=html}
<p class="mt-3">
```
Proporciona una `<strong>`{=html}garantía superior`</strong>`{=html}
sobre los recursos requeridos.
```{=html}
</p>
```
:::

::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.card-title .text-emerald-800}
🟢 Mejor caso · Best-Case
:::

```{=html}
<p>
```
Representa el `<strong>`{=html}mínimo costo`</strong>`{=html} ante la
entrada más favorable.
```{=html}
</p>
```
::: {.mt-3 .bg-white .rounded-lg .border .border-emerald-200 .p-3}
::: {.font-mono .text-center .font-bold}
\[ 12, 7, 25, 9, 18, 4 \]
:::

::: {.mt-2 .text-center}
Buscar `<strong>`{=html}12`</strong>`{=html} → 1 comparación
:::
:::

```{=html}
<p class="mt-3">
```
Es útil conocerlo, pero `<strong>`{=html}no garantiza el
rendimiento`</strong>`{=html} general.
```{=html}
</p>
```
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
El `<strong class="text-red-300">`{=html}peor caso`</strong>`{=html} es
especialmente importante cuando necesitamos garantizar un límite máximo
de recursos.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# Caso promedio · Average-Case

::: {.mt-4 .p-4 .rounded-xl .bg-blue-50 .border .border-blue-200 .text-center}
```{=html}
<p>
```
Busca determinar el `<strong>`{=html}costo esperado`</strong>`{=html}
considerando las posibles entradas de tamaño n.
```{=html}
</p>
```
::: {.mt-3 .text-xl .font-semibold .text-blue-800}
No significa simplemente "sumar varios tiempos y dividir".
:::
:::

::: {.grid .grid-cols-2 .gap-5 .mt-5}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
🎲 Requiere un modelo probabilístico
:::

```{=html}
<p>
```
Debemos establecer qué probabilidad tiene cada posible entrada.
```{=html}
</p>
```
```{=html}
<p class="mt-3">
```
Por ejemplo, podemos asumir posiciones `<strong>`{=html}igualmente
probables`</strong>`{=html}.
```{=html}
</p>
```
:::

::: {.card .bg-blue-50 .border .border-blue-200}
::: {.card-title .text-blue-800}
⚠️ La distribución importa
:::

```{=html}
<p>
```
El modelo debe representar razonablemente los datos reales.
```{=html}
</p>
```
```{=html}
<p class="mt-3">
```
Si la distribución real es distinta, el costo esperado puede dejar de
ser representativo.
```{=html}
</p>
```
:::
:::

::: {.mt-5 .p-4 .rounded-xl .bg-slate-900 .text-center}
::: {.text-xl .font-semibold .text-amber-300}
¿Qué costo esperamos bajo una determinada distribución de entradas?
:::
:::

------------------------------------------------------------------------

# Complejidad amortizada

::: {.mt-3 .text-center}
```{=html}
<p>
```
En algunas estructuras dinámicas, la mayoría de las operaciones son
baratas, pero `<strong>`{=html}ocasionalmente aparece una operación
mucho más costosa.`</strong>`{=html}
```{=html}
</p>
```
:::

::: {.grid .grid-cols-4 .gap-3 .mt-5 .text-center}
::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.font-bold .text-emerald-800}
Operación 1
:::

::: {.font-mono .text-xl .mt-2}
O(1)
:::
:::

::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.font-bold .text-emerald-800}
Operación 2
:::

::: {.font-mono .text-xl .mt-2}
O(1)
:::
:::

::: {.card .bg-emerald-50 .border .border-emerald-200}
::: {.font-bold .text-emerald-800}
Operación 3
:::

::: {.font-mono .text-xl .mt-2}
O(1)
:::
:::

::: {.card .bg-red-50 .border .border-red-200}
::: {.font-bold .text-red-800}
Redimensionar
:::

::: {.font-mono .text-xl .mt-2}
O(n)
:::
:::
:::

::: {.mt-4 .p-4 .rounded-xl .bg-violet-50 .border .border-violet-200}
::: {.card-title .text-violet-800}
Ejemplo: arreglo dinámico
:::

```{=html}
<p>
```
Insertar al final suele ser barato. Al agotarse la capacidad, se reserva
un arreglo mayor y se copian los elementos.
```{=html}
</p>
```
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
La complejidad amortizada da una
`<strong class="text-amber-300">`{=html}garantía determinista del costo
promedio por operación a lo largo de una secuencia`</strong>`{=html}; no
es un promedio probabilístico.
```{=html}
</p>
```
:::

------------------------------------------------------------------------

# En resumen: ¿cómo analizamos la complejidad?

::: {.mt-2 .text-center}
```{=html}
<p>
```
Seguimos un camino desde la `<strong>`{=html}entrada`</strong>`{=html}
hasta el `<strong>`{=html}patrón de crecimiento`</strong>`{=html}.
```{=html}
</p>
```
:::

::: {.grid .grid-cols-5 .gap-2 .mt-4}
::: {.card .bg-violet-50 .border .border-violet-200 .text-center}
::: {.text-xl .font-bold .text-violet-800}
1
:::

::: {.font-bold .mt-1}
Entrada
:::

::: {.font-mono .text-xl .my-2}
n
:::

```{=html}
<p>
```
Definimos su tamaño.
```{=html}
</p>
```
:::

::: {.card .bg-blue-50 .border .border-blue-200 .text-center}
::: {.text-xl .font-bold .text-blue-800}
2
:::

::: {.font-bold .mt-1}
Modelo RAM
:::

::: {.text-2xl .my-2}
⚙️
:::

```{=html}
<p>
```
Fijamos reglas de costo.
```{=html}
</p>
```
:::

::: {.card .bg-emerald-50 .border .border-emerald-200 .text-center}
::: {.text-xl .font-bold .text-emerald-800}
3
:::

::: {.font-bold .mt-1}
Costo
:::

::: {.font-mono .text-xl .my-2}
T(n)
:::

```{=html}
<p>
```
Contamos operaciones.
```{=html}
</p>
```
:::

::: {.card .bg-amber-50 .border .border-amber-200 .text-center}
::: {.text-xl .font-bold .text-amber-800}
4
:::

::: {.font-bold .mt-1}
Crecimiento
:::

::: {.text-2xl .my-2}
📈
:::

```{=html}
<p>
```
Identificamos qué domina.
```{=html}
</p>
```
:::

::: {.card .bg-violet-50 .border .border-violet-200 .text-center}
::: {.text-xl .font-bold .text-violet-800}
5
:::

::: {.font-bold .mt-1}
Orden
:::

::: {.font-mono .text-xl .my-2}
O(·)
:::

```{=html}
<p>
```
Describimos escalabilidad.
```{=html}
</p>
```
:::
:::

::: {.grid .grid-cols-2 .gap-4 .mt-4}
::: {.card .bg-slate-100 .border .border-slate-200}
::: {.card-title .text-slate-800}
¿Qué analizamos?
:::

```{=html}
<p>
```
`<strong>`{=html}Tiempo`</strong>`{=html},
`<strong>`{=html}espacio`</strong>`{=html} y escenarios: mejor,
promedio, peor y amortizado.
```{=html}
</p>
```
:::

::: {.card .bg-amber-50 .border .border-amber-200}
::: {.card-title .text-amber-800}
¿Para qué sirve?
:::

```{=html}
<p>
```
Para predecir escalabilidad, comparar alternativas y tomar
`<strong>`{=html}decisiones de diseño fundamentadas.`</strong>`{=html}
```{=html}
</p>
```
:::
:::

::: {.mt-4 .p-3 .rounded-xl .bg-slate-900 .text-center}
```{=html}
<p class="!text-white">
```
No buscamos únicamente cuánto tarda hoy, sino
`<strong class="text-amber-300">`{=html}cómo se comportará su costo
cuando el problema crezca.`</strong>`{=html}
```{=html}
</p>
```
:::
