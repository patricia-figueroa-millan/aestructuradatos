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
layout: center
transition: fade-out
title: Introducción
---

<div class="max-w-2xl mx-auto p-10 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Contexto -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-mono font-bold mb-4">
    <span></span> Introducción al Tema 2
  </div>

  <!-- Título Principal -->
  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight leading-tight">
    El desempeño de las Estructuras de Datos
  </h1>

</div>


---

# ¿Todas las operaciones cuestan lo mismo?

```python
datos = [10, 20, 30, 40, 50]

datos[0]           # acceder
datos.append(60)   # agregar al final
datos.insert(0, 5) # insertar al inicio
datos.pop()        # eliminar al final
50 in datos        # buscar
```

<div class="mt-4 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

### Misma estructura de datos: `datos`

Pero... ¿todas estas operaciones tendrán el mismo costo?

</div>

<div v-click class="mt-4 text-center text-lg">

**Antes de continuar:** ordénenlas de la que creen más eficiente a la menos eficiente.

</div>

<!--
NOTAS DOCENTE:
- No revelar todavía las complejidades.
- Dar 2–3 minutos para discutir en parejas.
- Recuperar algunas predicciones en el pizarrón.
- Preguntar: ¿una línea de código significa necesariamente el mismo costo?
-->

---

# De algoritmo a estructura de datos

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

### Estructura de datos

Forma de **organizar y almacenar datos** para poder trabajar con ellos.

```python
datos = [10, 20, 30, 40, 50]
```

</div>

<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">

### Operaciones

Sobre una estructura podemos:

- acceder
- buscar
- insertar
- eliminar
- recorrer

</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-white text-center">

No preguntaremos solamente:

**“¿Qué estructura estoy utilizando?”**

También preguntaremos:

### “¿Cuánto cuesta la operación que realizo sobre ella?”

</div>

<div v-click class="mt-4 text-center font-mono text-xl">

estructura + operación → costo

</div>

<!--
NOTAS DOCENTE:
Conectar explícitamente con el Tema 1:
ya sabemos estudiar cómo crece el trabajo cuando aumenta n.
Ahora analizaremos ese crecimiento para operaciones realizadas sobre estructuras de datos.
-->

---

# Misma estructura, diferente operación

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

### Acceder

```python
datos = list(range(1000000))

x = datos[0]
```

¿Necesitamos revisar los elementos anteriores?

<div v-click class="mt-3 text-center text-2xl font-bold text-violet-700">
No → O(1)
</div>

</div>

<div class="p-4 rounded-xl bg-amber-50 border border-amber-200">

### Buscar

```python
datos = list(range(1000000))

999999 in datos
```

¿Sabemos directamente dónde se encuentra?

<div v-click class="mt-3 text-center text-2xl font-bold text-amber-700">
No → O(n)
</div>

</div>

</div>

<div v-click class="mt-5 text-center text-xl font-semibold">

La lista es la misma. Lo que cambió fue la operación.

</div>

<!--
NOTAS DOCENTE:
- Para datos[0], aumentar n no aumenta la cantidad de elementos que debemos consultar.
- Para "x in datos", la búsqueda puede requerir revisar sucesivamente los elementos.
- Recuperar las ideas de O(1) y O(n) del Tema 1.
-->

---

# Agregar al final vs. insertar al inicio

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

### Opción A

```python
datos.append(99)
```

```text
[10][20][30][40][  ]
                 ↓
                [99]
```

</div>

<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">

### Opción B

```python
datos.insert(0, 99)
```

```text
[10][20][30][40]
 ↓   →   →   →   →
[99][10][20][30][40]
```

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

### Predicción

Si `datos` contiene 100,000 elementos:

**¿cuál operación esperan que tarde más? ¿Por qué?**

</div>

<!--
NOTAS DOCENTE:
No mostrar todavía Big O.
La pregunta guía es:
¿Qué tiene que hacer internamente la estructura para completar cada operación?
-->

---

# Experimento: midamos el tiempo

<div class="text-lg mb-2">
Primero probemos con <code>n = 10_000</code>.
</div>

<div class="text-[0.78em]">

```python {monaco}
import timeit

n = 10_000

tiempo_append = timeit.timeit(
    "datos.append(0)",
    setup=f"datos = list(range({n}))",
    number=1000
)

tiempo_insert = timeit.timeit(
    "datos.insert(0, 0)",
    setup=f"datos = list(range({n}))",
    number=1000
)

print(f"append:    {tiempo_append:.6f} s")
print(f"insert(0): {tiempo_insert:.6f} s")
```

</div>

<div class="mt-2 p-2 rounded-xl bg-amber-50 border border-amber-200 text-center">

**Ejecuten → observen → comparen**

¿Qué operación tardó más?

</div>

<!--
NOTAS DOCENTE:
- Ejecutar primero en el intérprete/entorno Python que utilicen, sin explicar el resultado.
- Los segundos exactos dependen del equipo y del entorno.
- Lo importante no es memorizar tiempos, sino comparar comportamientos.
-->

---

# ¿Qué pasa cuando aumenta `n`?

Ya ejecutamos el experimento con:

<div class="mt-2 text-center font-mono text-2xl">
n = 10_000
</div>

<div v-click class="mt-3 text-center">

### Ahora modifiquen únicamente `n`

```python
n = 100_000
```

y vuelvan a ejecutar.

</div>

<div v-click class="mt-3 text-center">

Después prueben:

```python
n = 1_000_000
```

</div>

<div v-click class="mt-3 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

No buscamos memorizar tiempos.

**Buscamos observar cómo cambia el costo cuando crece `n`.**

</div>

<div v-click class="mt-2 text-center text-lg font-semibold">

¿Cuál operación se ve más afectada al aumentar `n`?

</div>

<!--
NOTAS DOCENTE:
Secuencia sugerida:
1. n = 10,000
2. n = 100,000
3. n = 1,000,000

Preguntar:
¿Cuál operación se ve más afectada cuando crece n?

Después formalizar:
append(x) → O(1) amortizado
insert(0,x) → O(n)

Recordar que "amortizado" ya se abordó en el Tema 1.
-->

---

# ¿Qué observamos?

<div class="grid grid-cols-2 gap-5 mt-5">

<div v-click class="p-5 rounded-xl bg-blue-50 border border-blue-200 text-center">

### `datos.append(x)`

Agregar al final no requiere desplazar todos los elementos.

<div class="mt-4 text-3xl font-bold text-blue-700">
O(1) amortizado
</div>

</div>

<div v-click class="p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

### `datos.insert(0, x)`

Insertar al inicio requiere desplazar elementos existentes.

<div class="mt-4 text-3xl font-bold text-amber-700">
O(n)
</div>

</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-white text-center text-xl">

El experimento muestra tiempos concretos.<br>
**Big O describe cómo crece el costo cuando aumenta `n`.**

</div>

<!--
NOTAS DOCENTE:
Aclarar que una medición experimental y Big O no son lo mismo.
El experimento ayuda a observar el efecto que el crecimiento predice.
-->

---

# Regresemos al código inicial

```python
datos = [10, 20, 30, 40, 50]
```

<div class="mt-3 space-y-2">

<div v-click class="grid grid-cols-[1fr_180px] gap-3 p-2 rounded-lg bg-slate-50">
<div><code>datos[0]</code> — acceder por índice</div>
<div class="font-bold text-center">O(1)</div>
</div>

<div v-click class="grid grid-cols-[1fr_180px] gap-3 p-2 rounded-lg bg-slate-50">
<div><code>datos.append(60)</code> — agregar al final</div>
<div class="font-bold text-center">O(1) amortizado</div>
</div>

<div v-click class="grid grid-cols-[1fr_180px] gap-3 p-2 rounded-lg bg-slate-50">
<div><code>datos.insert(0, 5)</code> — insertar al inicio</div>
<div class="font-bold text-center">O(n)</div>
</div>

<div v-click class="grid grid-cols-[1fr_180px] gap-3 p-2 rounded-lg bg-slate-50">
<div><code>datos.pop()</code> — eliminar al final</div>
<div class="font-bold text-center">O(1)</div>
</div>

<div v-click class="grid grid-cols-[1fr_180px] gap-3 p-2 rounded-lg bg-slate-50">
<div><code>50 in datos</code> — buscar</div>
<div class="font-bold text-center">O(n)</div>
</div>

</div>

<!--
NOTAS DOCENTE:
Antes de revelar cada fila, pedir que el grupo responda.
Pregunta clave:
¿Podemos decir entonces que "una lista es O(n)"?
Respuesta: no. Analizamos el costo de una operación concreta sobre la estructura.
-->

---

# ¿Qué aprendimos hoy?

<div class="mt-7 text-center text-2xl">

Una estructura de datos determina cómo organizamos los datos...

<div v-click class="my-4 text-4xl">↓</div>

<div v-click>
pero también influye en el <strong>costo de las operaciones</strong>
que realizamos sobre ellos.
</div>

</div>

<div v-click class="mt-7 p-5 rounded-xl bg-slate-900 text-white text-center text-xl">

## Elegir una estructura de datos también implica elegir el costo de sus operaciones.

</div>

<div v-click class="mt-5 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center text-amber-800">

### Siguiente pregunta

¿Por qué podemos acceder directamente a `datos[i]` en O(1)?

</div>

<!--
NOTAS DOCENTE:
Cerrar aquí.
La pregunta final sirve como puente al subtema 2.1.1 Arreglo:
índices, organización de los elementos y representación en memoria.
-->
