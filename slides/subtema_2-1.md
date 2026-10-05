---
background: /background3.jpg
title: 2.1.1 Arreglos
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">

<div class="flex flex-col items-center gap-1 mb-5">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400 bg-amber-400/10 px-3 py-1 rounded-full border border-amber-400/20">
Tema 2 · Estructuras de datos
</span>
</div>

<h1 class="text-4xl font-black tracking-tight bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent !leading-tight mb-2">
2.1.1 Arreglos
</h1>

<div class="mt-3 text-lg text-slate-200">
Representación, operaciones y rendimiento con NumPy
</div>

<div class="mt-6 pt-5 border-t border-white/10">
<div class="text-sm text-slate-300">
Algoritmia y Estructura de Datos
</div>
</div>

</div>

---

# ¿Lista o arreglo?

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">Lista de Python</div>

```python
lista = [10, 20, 30, 40]
```

<div class="mt-2 text-sm">
Colección flexible de objetos. Puede crecer, reducirse y contener elementos de distintos tipos.
</div>

</div>

<div class="card bg-violet-50 border border-violet-200">

<div class="card-title text-violet-800">Arreglo NumPy</div>

```python
import numpy as np

arreglo = np.array([10, 20, 30, 40])
```

<div class="mt-2 text-sm">
Estructura orientada a datos homogéneos, con un <code>dtype</code> y una forma definida.
</div>

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">

A simple vista contienen los mismos valores, pero <strong>no son la misma estructura</strong>.

</div>

<div v-click class="mt-3 text-center font-semibold">
Hoy trabajaremos con <code>numpy.ndarray</code> para estudiar arreglos.
</div>

---

# Creación de arreglos con NumPy

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

```python
import numpy as np

temperaturas = np.array(
    [24.5, 26.1, 25.8, 29.2, 30.1]
)

print(temperaturas)
```

<div v-click class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200">

`np.array()` crea un arreglo a partir de una colección de valores.

</div>

</div>

<div v-click>

```python
ceros = np.zeros(5)
unos = np.ones(5)
secuencia = np.arange(0, 10, 2)

print(ceros)
print(unos)
print(secuencia)
```

<div class="mt-3 p-3 rounded-xl bg-violet-50 border border-violet-200">

NumPy también puede <strong>generar arreglos</strong> sin escribir cada elemento manualmente.

</div>

</div>

</div>

---

# Conozcamos nuestro arreglo

```python
temperaturas = np.array(
    [24.5, 26.1, 25.8, 29.2, 30.1]
)

print(temperaturas.dtype)
print(temperaturas.size)
print(temperaturas.shape)
print(temperaturas.ndim)
```

<div class="grid grid-cols-4 gap-3 mt-4 text-center">

<div v-click class="card bg-blue-50 border border-blue-200">
<div class="font-mono font-bold">dtype</div>
<div class="text-sm mt-1">tipo de los elementos</div>
</div>

<div v-click class="card bg-amber-50 border border-amber-200">
<div class="font-mono font-bold">size</div>
<div class="text-sm mt-1">total de elementos</div>
</div>

<div v-click class="card bg-violet-50 border border-violet-200">
<div class="font-mono font-bold">shape</div>
<div class="text-sm mt-1">forma del arreglo</div>
</div>

<div v-click class="card bg-slate-100 border border-slate-200">
<div class="font-mono font-bold">ndim</div>
<div class="text-sm mt-1">número de dimensiones</div>
</div>

</div>

<div v-click class="mt-3 text-center text-sm">
Para este arreglo: <code>size = 5</code>, <code>shape = (5,)</code> y <code>ndim = 1</code>.
</div>

---

# Índices: acceder a los elementos

<div class="mt-2 text-center font-mono">

Índice&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4  
Valor&nbsp;&nbsp;&nbsp;&nbsp;24.5&nbsp;&nbsp;&nbsp;26.1&nbsp;&nbsp;&nbsp;25.8&nbsp;&nbsp;&nbsp;29.2&nbsp;&nbsp;&nbsp;30.1

</div>

<div class="grid grid-cols-2 gap-5 mt-4">

<div>

```python
print(temperaturas[0])
print(temperaturas[3])
print(temperaturas[-1])
```

<div v-click class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
Los índices comienzan en <strong>0</strong>.<br>
<code>-1</code> permite acceder al último elemento.
</div>

</div>

<div v-click class="p-4 rounded-xl bg-slate-900 text-center">

<div class="text-2xl font-bold !text-white mb-3">
Pregunta
</div>

<div class="!text-white text-lg">
Para obtener <code class="!text-slate-900 bg-blue-100 px-2 py-1 rounded">temperaturas[3]</code>:
</div>

<div class="!text-white text-lg mt-3">
¿debemos recorrer primero las posiciones 0, 1 y 2?
</div>

<div v-click class="mt-4 text-3xl font-bold text-amber-300">
No → O(1)
</div>

</div>

</div>

---

# Modificar un elemento

<div class="grid grid-cols-2 gap-5 mt-3">

<div>

```python
temperaturas = np.array(
    [24.5, 26.1, 25.8, 29.2, 30.1]
)

temperaturas[2] = 26.4

print(temperaturas)
```

</div>

<div v-click class="card bg-amber-50 border border-amber-200">

<div class="card-title text-amber-800">Antes</div>

`[24.5, 26.1, 25.8, 29.2, 30.1]`

<div class="card-title text-violet-800 mt-3">Después</div>

`[24.5, 26.1, 26.4, 29.2, 30.1]`

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<span class="!text-white">Modificar una posición conocida tampoco requiere recorrer el arreglo:</span>

<div class="font-mono font-bold text-2xl text-amber-300 mt-1">O(1)</div>

</div>

---

# Seleccionar varios elementos: slicing

```python
datos = np.array([10, 20, 30, 40, 50, 60, 70])
```

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

```python
print(datos[1:4])
# [20 30 40]

print(datos[:3])
# [10 20 30]
```

</div>

<div v-click>

```python
print(datos[3:])
# [40 50 60 70]

print(datos[::2])
# [10 30 50 70]
```

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

La forma general es:

<div class="font-mono font-bold text-xl mt-1">
arreglo[inicio : fin : paso]
</div>

</div>

<div v-click class="mt-3 text-center text-sm">
El índice <code>fin</code> no se incluye en el resultado.
</div>

---

# Operaciones con todo el arreglo

<div class="grid grid-cols-2 gap-5 mt-3">

<div>

```python
datos = np.array([10, 20, 30, 40])

print(datos + 5)
print(datos * 2)
```

<div v-click class="mt-3 text-sm">
La operación se aplica elemento por elemento.
</div>

</div>

<div v-click>

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
# [11 22 33]
```

<div class="mt-3 text-sm">
NumPy permite expresar operaciones sobre arreglos sin escribir explícitamente un ciclo para cada elemento.
</div>

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
Esta capacidad se conoce como <strong>vectorización</strong>.
</div>

---

# Buscar y filtrar datos

```python
temperaturas = np.array(
    [24.5, 26.1, 25.8, 29.2, 30.1]
)
```

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

### ¿Cumple una condición?

```python
print(temperaturas > 28)
```

<div v-click class="text-sm mt-2">
Resultado: un arreglo de valores booleanos.
</div>

</div>

<div v-click>

### Usar la condición como filtro

```python
altas = temperaturas[
    temperaturas > 28
]

print(altas)
# [29.2 30.1]
```

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Para decidir qué elementos cumplen la condición es necesario considerar los datos del arreglo: el trabajo crece con <code>n</code>.
</div>

---

# Agregación: resumir un arreglo

```python
temperaturas = np.array(
    [24.5, 26.1, 25.8, 29.2, 30.1]
)
```

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

```python
print(temperaturas.sum())
print(temperaturas.mean())
```

</div>

<div v-click>

```python
print(temperaturas.min())
print(temperaturas.max())
```

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

`sum`, `mean`, `min` y `max` producen un resultado a partir de los elementos del arreglo.

</div>

<div v-click class="mt-3 text-center font-semibold">
Pregunta: si duplicamos la cantidad de datos, ¿estas operaciones siguen siendo O(1)?
</div>

<div v-click class="mt-2 text-center text-xl font-bold text-amber-700">
No. Deben procesar los elementos → O(n)
</div>

---

# Ordenar y localizar valores

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

### Ordenar

```python
datos = np.array([31, 8, 17, 4, 9])

ordenados = np.sort(datos)

print(ordenados)
```

<div v-click class="text-sm mt-2">
`np.sort()` devuelve un arreglo ordenado.
</div>

</div>

<div v-click>

### Localizar con una condición

```python
posiciones = np.where(datos > 10)

print(posiciones)
# (array([0, 2]),)
```

<div class="text-sm mt-2">
`np.where()` permite obtener las posiciones que cumplen una condición.
</div>

</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
No todas las operaciones sobre un arreglo tienen el mismo costo.
</div>

---

# ¿Se puede cambiar el tamaño de un arreglo?

<div class="grid grid-cols-3 gap-3 mt-3">

<div>

### Agregar

```python
a = np.array([10, 20, 30])

b = np.append(a, 40)
```

</div>

<div v-click>

### Insertar

```python
c = np.insert(
    a, 1, 15
)
```

</div>

<div v-click>

### Eliminar

```python
d = np.delete(
    a, 1
)
```

</div>

</div>

<div v-click class="mt-4 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

<strong>Importante:</strong> estas operaciones no modifican el tamaño del arreglo original en el mismo lugar.

NumPy devuelve <strong>un nuevo arreglo</strong>.

</div>

<div v-click class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<span class="!text-white">Crear y copiar un arreglo cuyo tamaño depende de <code>n</code> implica un costo que crece con la cantidad de elementos.</span>
</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-3xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">

<div class="flex flex-col items-center gap-1 mb-5">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400 bg-amber-400/10 px-3 py-1 rounded-full border border-amber-400/20">
Práctica guiada · 45 minutos
</span>
</div>

<h1 class="text-4xl font-black tracking-tight bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent !leading-tight mb-3">
Análisis de datos de una estación meteorológica
</h1>

<div class="mt-4 text-lg text-slate-200">
De un arreglo de datos a información útil
</div>

<div class="mt-6 pt-5 border-t border-white/10 text-sm text-slate-300">
NumPy · Arreglos · Operaciones · Complejidad
</div>

</div>

---

# El problema

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-blue-50 border border-blue-200">

<div class="card-title text-blue-800">Contexto</div>

Una estación meteorológica registra una medición de temperatura cada hora.

Tenemos **12 mediciones**, pero una de ellas contiene un valor anormal.

</div>

<div v-click class="card bg-violet-50 border border-violet-200">

<div class="card-title text-violet-800">Nuestro objetivo</div>

Usaremos un arreglo NumPy para:

- inspeccionar los datos,
- detectar el valor anormal,
- localizarlo y corregirlo,
- obtener información,
- filtrar mediciones.

</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<span class="!text-white text-lg">
No resolveremos operaciones aisladas: construiremos la solución <strong>paso a paso</strong>.
</span>

</div>

---

# Paso 1 · Representar las mediciones

<div class="mt-4 p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-bold text-amber-800 text-lg">Pregunta detonadora</div>

<div class="mt-2 text-xl">
¿Cómo representaríamos estas 12 mediciones utilizando un arreglo NumPy?
</div>

</div>

<div v-click class="mt-5">

```python {monaco}
import numpy as np

temperaturas = np.array([
    24.5, 25.1, 25.8, 26.4, 28.2, 45.5,
    31.2, 32.1, 31.7, 29.8, 27.4, 26.0
])

print(temperaturas)
```

</div>

<div v-click class="mt-3 text-center text-sm text-slate-600">
Ejecutemos el código antes de continuar.
</div>

---

# Paso 1 · Resultado esperado

<div class="mt-5 p-4 rounded-xl bg-slate-900">

<div class="text-xs uppercase tracking-widest text-amber-300 font-bold mb-3">
Salida
</div>

<div class="font-mono !text-white text-lg text-center">
[24.5 25.1 25.8 26.4 28.2 45.5 31.2 32.1 31.7 29.8 27.4 26.0]
</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center">

Tenemos un <code>numpy.ndarray</code> de una dimensión.

</div>

<div v-click class="mt-4 text-center font-semibold text-violet-800">
Ahora conozcamos el arreglo sin contar ni inspeccionar manualmente sus elementos.
</div>

---

# Paso 1 · ¿Qué sabemos de nuestros datos?

<div class="mt-3 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

<strong>Sin contar manualmente:</strong><br>
¿Cómo sabemos cuántas mediciones existen? ¿Qué tipo de datos almacenamos? ¿Cuál es la forma del arreglo?

</div>

<div v-click class="mt-4">

```python {monaco}
print("Cantidad:", temperaturas.size)
print("Tipo:", temperaturas.dtype)
print("Forma:", temperaturas.shape)
```

</div>

<div v-click class="grid grid-cols-3 gap-3 mt-4 text-center">

<div class="card bg-blue-50 border border-blue-200">
<div class="font-mono font-bold">size</div>
<div class="text-xl mt-1">12</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="font-mono font-bold">dtype</div>
<div class="text-sm mt-1">tipo numérico decimal</div>
</div>

<div class="card bg-slate-100 border border-slate-200">
<div class="font-mono font-bold">shape</div>
<div class="text-xl mt-1">(12,)</div>
</div>

</div>

---

# Paso 2 · Algo no parece correcto

<div class="mt-5 text-center font-mono text-lg">

<span class="px-2 py-2 bg-blue-50 rounded">24.5</span>
<span class="px-2 py-2 bg-blue-50 rounded">25.1</span>
<span class="px-2 py-2 bg-blue-50 rounded">25.8</span>
<span class="px-2 py-2 bg-blue-50 rounded">26.4</span>
<span class="px-2 py-2 bg-blue-50 rounded">28.2</span>
<span class="px-2 py-2 bg-red-100 border border-red-300 rounded font-bold text-red-700">45.5</span>

<div class="mt-4">

<span class="px-2 py-2 bg-blue-50 rounded">31.2</span>
<span class="px-2 py-2 bg-blue-50 rounded">32.1</span>
<span class="px-2 py-2 bg-blue-50 rounded">31.7</span>
<span class="px-2 py-2 bg-blue-50 rounded">29.8</span>
<span class="px-2 py-2 bg-blue-50 rounded">27.4</span>
<span class="px-2 py-2 bg-blue-50 rounded">26.0</span>

</div>

</div>

<div v-click class="mt-7 p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-bold text-amber-800">Regla para este ejercicio</div>

Consideraremos anormal cualquier temperatura **mayor a 40 °C**.

</div>

<div v-click class="mt-4 p-4 rounded-xl bg-slate-900 text-center">
<span class="!text-white text-lg">
¿Cómo podemos detectarla <strong>sin conocer previamente su posición</strong>?
</span>
</div>

---

# Paso 2 · Construimos una condición

<div class="mt-4 text-center">

Antes de ejecutar:

**¿qué creen que devolverá esta expresión?**

</div>

<div v-click class="mt-4">

```python {monaco}
temperaturas > 40
```

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900">

<div class="text-xs uppercase tracking-widest text-amber-300 font-bold mb-3">
Resultado esperado
</div>

<div class="font-mono !text-white text-center">
[False False False False False True False False False False False False]
</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
La comparación se aplica a <strong>cada elemento</strong> y produce una máscara booleana.
</div>

---

# Paso 2 · ¿Dónde está el dato anormal?

<div class="mt-3 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

Ya sabemos que existe un valor que cumple la condición.

<strong>¿Cómo obtenemos su posición?</strong>

</div>

<div v-click class="mt-4">

```python {monaco}
posiciones = np.where(temperaturas > 40)

print(posiciones)
```

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<div class="font-mono text-2xl font-bold text-amber-300">
(array([5]),)
</div>

</div>

<div v-click class="mt-3 text-center">
El valor anormal se encuentra en el índice <code>5</code>.
</div>

<div v-click class="mt-3">

```python
print(temperaturas[posiciones])
# [45.5]
```

</div>

---

# Antes de corregir... pensemos en el costo

<div class="mt-5 p-5 rounded-xl bg-slate-900 text-center">

<div class="!text-white text-xl">
Para encontrar el valor mayor a 40 °C:
</div>

<div class="!text-white text-xl mt-3">
¿NumPy pudo ir directamente a una posición conocida?
</div>

</div>

<div v-click class="mt-5 text-center text-3xl font-black text-red-600">
No
</div>

<div v-click class="mt-4 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center text-lg">

Fue necesario comprobar los elementos del arreglo.

<div class="font-mono font-bold text-3xl text-violet-700 mt-2">O(n)</div>

</div>

---

# Paso 3 · Corregir el dato

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-red-50 border border-red-200 text-center">
<div class="text-sm text-red-700">Valor registrado</div>
<div class="font-mono font-bold text-3xl mt-2">45.5 °C</div>
</div>

<div v-click class="card bg-green-50 border border-green-200 text-center">
<div class="text-sm text-green-700">Valor correcto</div>
<div class="font-mono font-bold text-3xl mt-2">30.5 °C</div>
</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">

Ya encontramos la posición con <code>np.where()</code>.

<strong>¿Necesitamos escribir manualmente <code>temperaturas[5]</code>?</strong>

</div>

<div v-click class="mt-4">

```python {monaco}
# Reutilizamos la posición encontrada
temperaturas[posiciones] = 30.5

print(temperaturas)
```

</div>

---

# Paso 3 · Resultado de la corrección

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="card bg-red-50 border border-red-200">
<div class="card-title text-red-700">Antes</div>
<div class="font-mono text-sm mt-3">
... 28.2, <strong>45.5</strong>, 31.2 ...
</div>
</div>

<div class="card bg-green-50 border border-green-200">
<div class="card-title text-green-700">Después</div>
<div class="font-mono text-sm mt-3">
... 28.2, <strong>30.5</strong>, 31.2 ...
</div>
</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center">

<div class="!text-white">
Primero tuvimos que <strong>localizar</strong> el dato:
</div>
<div class="font-mono font-bold text-xl text-amber-300 mt-1">O(n)</div>

</div>

<div v-click class="mt-3 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

Una vez conocida la posición, modificar ese elemento es una operación de acceso directo.

<strong>Posición conocida → O(1)</strong>

</div>

---

# Paso 4 · ¿Qué nos dicen los datos?

<div class="mt-4 p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-bold text-amber-800 text-lg">Pregunta detonadora</div>

<div class="mt-2">
Ya corregimos los datos. ¿Qué valores nos ayudarían a describir el comportamiento general de las temperaturas?
</div>

</div>

<div v-click class="mt-5">

```python {monaco}
promedio = temperaturas.mean()
minima = temperaturas.min()
maxima = temperaturas.max()

print("Promedio:", promedio)
print("Mínima:", minima)
print("Máxima:", maxima)
```

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
Estas operaciones resumen información de <strong>todo el arreglo</strong>.
</div>

---

# Paso 4 · Resultado esperado

<div class="grid grid-cols-3 gap-4 mt-5 text-center">

<div class="card bg-blue-50 border border-blue-200">
<div class="text-sm">Promedio</div>
<div class="font-mono font-bold text-2xl mt-2">28.39 °C</div>
</div>

<div class="card bg-violet-50 border border-violet-200">
<div class="text-sm">Mínima</div>
<div class="font-mono font-bold text-2xl mt-2">24.5 °C</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="text-sm">Máxima</div>
<div class="font-mono font-bold text-2xl mt-2">32.1 °C</div>
</div>

</div>

<div v-click class="mt-6 p-4 rounded-xl bg-slate-900 text-center">

<span class="!text-white text-lg">
Nueva pregunta: <strong>¿cuántas mediciones estuvieron por encima del promedio?</strong>
</span>

</div>

<div v-click class="mt-3 text-center text-violet-800 font-semibold">
¿Qué operaciones que ya conocemos podríamos combinar?
</div>

---

# Paso 4 · Construimos la solución

<div class="text-sm mt-2">
Primero construimos la condición:
</div>

<div v-click>

```python
temperaturas > promedio
```

</div>

<div v-click class="text-sm mt-3">
Después utilizamos esa condición para filtrar:
</div>

<div v-click>

```python
sobre_promedio = temperaturas[
    temperaturas > promedio
]

print(sobre_promedio)
```

</div>

<div v-click class="mt-3 p-3 rounded-xl bg-slate-900 text-center">
<div class="font-mono !text-white">
[30.5 31.2 32.1 31.7 29.8]
</div>
</div>

<div v-click class="mt-3">

```python
print("Cantidad:", sobre_promedio.size)
# Cantidad: 5
```

</div>

---

# Paso 5 · Sabemos cuál es la máxima...

<div class="mt-5">

```python
maxima = temperaturas.max()

print(maxima)
# 32.1
```

</div>

<div v-click class="mt-6 p-5 rounded-xl bg-amber-50 border border-amber-200 text-center">

<div class="font-bold text-amber-800 text-lg">Pero ahora queremos saber algo más</div>

<div class="mt-2 text-2xl font-bold">
¿En qué posición ocurrió?
</div>

</div>

<div v-click class="mt-5 text-center text-violet-800">

Ya conocemos el valor <code>32.1</code>.<br>
¿Qué herramienta utilizada anteriormente podría ayudarnos a localizarlo?

</div>

---

# Paso 5 · Combinamos operaciones

<div class="mt-3">

```python {monaco}
posicion_max = np.where(
    temperaturas == maxima
)

print(posicion_max)
```

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-slate-900 text-center">

<div class="text-xs uppercase tracking-widest text-amber-300 font-bold mb-2">
Resultado
</div>

<div class="font-mono text-2xl font-bold !text-white">
(array([7]),)
</div>

</div>

<div v-click class="mt-4">

```python
print(
    "Temperatura máxima:",
    maxima,
    "en la posición:",
    posicion_max[0][0]
)
```

</div>

<div v-click class="mt-3 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

Ya no estamos usando operaciones aisladas:<br>
<strong>combinamos operaciones para resolver una pregunta.</strong>

</div>

---

# Paso 6 · Ahora ustedes

<div class="mt-4 p-5 rounded-xl bg-slate-900 text-center">

<div class="text-amber-300 font-bold uppercase tracking-widest text-sm">
Reto
</div>

<div class="!text-white text-xl mt-3">
Queremos obtener únicamente las mediciones dentro del intervalo:
</div>

<div class="font-mono font-black text-3xl text-amber-300 mt-4">
25 °C ≤ temperatura ≤ 30 °C
</div>

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">

<strong>Antes de programar:</strong>

1. ¿Qué condición comprueba el límite inferior?
2. ¿Qué condición comprueba el límite superior?
3. ¿Cómo podríamos exigir que ambas se cumplan?

</div>

<div v-click class="mt-4 text-center font-semibold text-violet-800">
Intenten construir la solución antes de continuar.
</div>

---

# Paso 6 · Construimos las condiciones

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

### Límite inferior

```python
temperaturas >= 25
```

</div>

<div v-click>

### Límite superior

```python
temperaturas <= 30
```

</div>

</div>

<div v-click class="mt-5 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">

Necesitamos que <strong>las dos condiciones</strong> sean verdaderas para una misma posición.

</div>

<div v-click class="mt-4">

```python {monaco}
condicion = (
    (temperaturas >= 25) &
    (temperaturas <= 30)
)
```

</div>

<div v-click class="mt-2 text-center text-sm text-violet-800">
En NumPy, <code>&</code> permite combinar condiciones elemento por elemento.
</div>

---

# Paso 6 · Aplicamos el filtro

<div class="mt-3">

```python {monaco}
confort = temperaturas[condicion]

print(confort)
print("Cantidad:", confort.size)
```

</div>

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900">

<div class="text-xs uppercase tracking-widest text-amber-300 font-bold mb-3">
Resultado esperado
</div>

<div class="font-mono !text-white text-center text-lg">
[25.1 25.8 26.4 28.2 29.8 27.4 26.0]
</div>

<div class="font-mono text-amber-300 text-center mt-3">
Cantidad: 7
</div>

</div>

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">

Partimos de 12 mediciones y construimos un nuevo arreglo con las que cumplen <strong>ambas condiciones</strong>.

</div>

---

# ¿Qué acabamos de construir?

<div class="mt-7 flex items-center justify-center gap-2 text-center text-sm">

<div class="card bg-blue-50 border border-blue-200 px-4">
<strong>Datos</strong>
</div>

<div class="text-2xl">→</div>

<div v-click class="card bg-amber-50 border border-amber-200 px-4">
<strong>Detectar</strong>
</div>

<div v-click class="text-2xl">→</div>

<div v-click class="card bg-violet-50 border border-violet-200 px-4">
<strong>Localizar</strong>
</div>

<div v-click class="text-2xl">→</div>

<div v-click class="card bg-blue-50 border border-blue-200 px-4">
<strong>Corregir</strong>
</div>

</div>

<div class="mt-4 flex items-center justify-center gap-2 text-center text-sm">

<div v-click class="card bg-violet-50 border border-violet-200 px-5">
<strong>Analizar</strong>
</div>

<div v-click class="text-2xl">→</div>

<div v-click class="card bg-amber-50 border border-amber-200 px-5">
<strong>Filtrar</strong>
</div>

</div>

<div v-click class="mt-6 p-4 rounded-xl bg-slate-900 text-center">

<span class="!text-white text-lg">
Las operaciones de NumPy son herramientas.<br>
<strong>El algoritmo aparece cuando decidimos cómo combinarlas para resolver el problema.</strong>
</span>

</div>

---

# Cierre · ¿O(1) u O(n)?

<div class="mt-3 text-center text-sm">
Clasifiquemos algunas de las operaciones utilizadas durante la práctica.
</div>

<div class="grid grid-cols-2 gap-3 mt-4">

<div class="card bg-blue-50 border border-blue-200">
<code>temperaturas[5]</code><br>
<span class="text-sm">Acceder a una posición conocida</span>
<div v-click class="font-mono font-bold text-xl text-violet-700 mt-1">O(1)</div>
</div>

<div class="card bg-blue-50 border border-blue-200">
<code>temperaturas[5] = 30.5</code><br>
<span class="text-sm">Modificar una posición conocida</span>
<div v-click class="font-mono font-bold text-xl text-violet-700 mt-1">O(1)</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<code>temperaturas &gt; 40</code><br>
<span class="text-sm">Evaluar una condición</span>
<div v-click class="font-mono font-bold text-xl text-amber-700 mt-1">O(n)</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<code>temperaturas.mean()</code><br>
<span class="text-sm">Resumir los elementos</span>
<div v-click class="font-mono font-bold text-xl text-amber-700 mt-1">O(n)</div>
</div>

</div>

---

# Cierre · La idea importante

<div class="grid grid-cols-2 gap-5 mt-6">

<div class="card bg-blue-50 border border-blue-200 text-center">

<div class="text-sm">Si conocemos la posición</div>

<div class="font-mono font-bold text-2xl text-violet-700 mt-3">
índice → acceso directo
</div>

<div class="font-mono font-black text-3xl mt-3">
O(1)
</div>

</div>

<div v-click class="card bg-amber-50 border border-amber-200 text-center">

<div class="text-sm">Si necesitamos buscar, filtrar o resumir</div>

<div class="font-mono font-bold text-2xl text-amber-700 mt-3">
procesamos elementos
</div>

<div class="font-mono font-black text-3xl mt-3">
O(n)
</div>

</div>

</div>

<div v-click class="mt-6 p-4 rounded-xl bg-slate-900 text-center">
<span class="!text-white text-lg">
Un arreglo permite acceso directo por índice, pero <strong>no todas las operaciones sobre un arreglo cuestan lo mismo</strong>.
</span>
</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Tema 2 · Estructuras de datos</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">2.1.2 Listas</h1>
<div class="mt-3 text-lg text-slate-200">Estructuras dinámicas y costo de sus operaciones</div>
</div>

---

# Lista: estructura dinámica

```python
tareas = ["Monitorear", "Generar reporte", "Respaldar datos"]
```

<div class="grid grid-cols-2 gap-5 mt-4">
<div class="card bg-blue-50 border border-blue-200"><strong>Acceso / modificación</strong><div class="font-black text-2xl mt-2">O(1)</div></div>
<div v-click class="card bg-violet-50 border border-violet-200"><strong>Pregunta</strong><div class="mt-2">¿Todas las operaciones cuestan lo mismo?</div><div class="font-black text-2xl mt-2 text-violet-700">No</div></div>
</div>

---

# Agregar y eliminar

<div class="grid grid-cols-2 gap-5 mt-4">
<div class="card bg-green-50 border border-green-200">

```python
tareas.append("Actualizar sistema")
tareas.pop()
```
<div class="text-center font-bold">Final → O(1) amortizado / O(1)</div>
</div>
<div v-click class="card bg-amber-50 border border-amber-200">

```python
tareas.insert(0, "Atender alerta")
tareas.pop(0)
```
<div class="text-center font-bold">Inicio → O(n)</div>
</div>
</div>

---

# Buscar, extender y ordenar

| Operación | Complejidad |
|---|---:|
| `x in lista` | O(n) |
| `lista.index(x)` | O(n) |
| `lista.remove(x)` | O(n) |
| `lista.extend(nuevas)` | O(k) |
| `lista[:k]` | O(k) |
| `lista.sort()` | O(n log n) |

<div v-click class="mt-4 p-3 rounded-xl bg-slate-900 text-center !text-white">En <code>extend()</code>, <strong>k</strong> representa cuántos elementos se agregan.</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---
<div class="max-w-3xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Práctica · Listas</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">Gestión dinámica de tareas</h1>
<div class="mt-4 text-lg text-slate-200">Operaciones de listas + análisis de complejidad</div>
</div>

---

# Práctica · 1 · Crear, consultar y modificar

```python
tareas = [
    "Monitorización de mediciones",
    "Generar reporte",
    "Respaldar base de datos",
    "Enviar resultados"
]

cantidad_tareas = len(tareas)       # O(1)
print(tareas[1])                    # O(1)

tareas[1] = "Generar reporte específico"  # O(1)
```

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
Si conocemos la posición, accedemos directamente al elemento.
</div>

---

# Práctica · 2 · Agregar

```python
tareas.append("Actualizar sistema")
```

<div class="text-center mt-3 font-black text-2xl text-green-700">O(1) amortizado</div>

<div v-click class="mt-4">

```python
tareas.insert(0, "Atender alerta")
```

</div>

<div v-click class="text-center mt-3 font-black text-2xl text-amber-700">O(n)</div>

<div v-click class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
¿Por qué? Insertar al inicio obliga a desplazar los elementos existentes.
</div>

---

# Práctica · 3 · Eliminar

<div class="grid grid-cols-2 gap-5 mt-3">
<div>

```python
completada = tareas.pop()
```

<div class="text-center font-bold">Final → O(1)</div>
</div>

<div v-click>

```python
completada = tareas.pop(0)
```

<div class="text-center font-bold">Inicio → O(n)</div>
</div>
</div>

<div v-click class="mt-5 p-3 rounded-xl bg-slate-900 text-center !text-white">
Eliminar al inicio requiere desplazar los elementos restantes.
</div>

---

# Práctica · 4 · Buscar

```python
encontrada = "Enviar resultados" in tareas
print(encontrada)
```

<div v-click class="mt-3 text-center"><code>in</code> → <strong>O(n)</strong></div>

<div v-click class="mt-4">

```python
posicion = tareas.index("Enviar resultados")
print(posicion)
```

</div>

<div v-click class="mt-3 text-center"><code>index()</code> → <strong>O(n)</strong></div>

---

# Práctica · 5 · Eliminar por valor

```python
tareas.remove("Enviar resultados")
print(tareas)
```

<div v-click class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
Primero debe localizar el valor y después puede ser necesario desplazar elementos.
<div class="font-black text-2xl text-amber-700 mt-2">O(n)</div>
</div>

---

# Práctica · 6 · Agregar varios elementos

```python
tareas_nuevas = [
    "Revisar red",
    "Validar datos",
    "Documentar cambios"
]

tareas.extend(tareas_nuevas)
```

<div v-click class="mt-4 p-4 rounded-xl bg-slate-900 text-center">
<div class="!text-white">Si incorporamos <strong>k</strong> elementos:</div>
<div class="font-black text-3xl text-amber-300 mt-2">O(k)</div>
</div>

<div v-click class="mt-3 text-center text-sm"><strong>k</strong> = cantidad de elementos que agregamos.</div>

---

# Práctica · 7 · Slicing

```python
primeras = tareas[:3]
print(primeras)
```

<div v-click class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
El slicing crea una nueva lista con los elementos seleccionados.
<div class="font-black text-2xl text-violet-700 mt-2">k elementos → O(k)</div>
</div>

---

# Práctica · 8 · Ordenar

```python
tareas.sort()
print(tareas)
```

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="!text-white">Ordenar la lista:</div>
<div class="font-black text-3xl text-amber-300 mt-2">O(n log n)</div>
</div>

---

# Cierre · Operaciones de listas

| Operación | Complejidad |
|---|---:|
| `len(lista)`, `lista[i]`, modificar `lista[i]` | O(1) |
| `append(x)` | O(1) amortizado |
| `pop()` | O(1) |
| `insert(i,x)`, `pop(i)`, `remove(x)` | O(n) |
| `in`, `index(x)` | O(n) |
| `extend(...)`, slicing | O(k) |
| `sort()` | O(n log n) |

<div v-click class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Una lista es dinámica, pero la posición y la operación elegida determinan su costo.
</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---
<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Tema 2 · Estructuras de datos</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">2.1.3 Matrices multidimensionales</h1>
<div class="mt-3 text-lg text-slate-200">Organización de datos en filas y columnas</div>
</div>

---

# ¿Qué es una matriz?

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="card bg-blue-50 border border-blue-200">
Una <strong>matriz</strong> organiza datos en dos dimensiones:
<div class="mt-4 text-center font-black text-2xl text-blue-800">filas × columnas</div>
<div class="mt-4 text-sm">Cada dato se identifica mediante una fila y una columna.</div>
</div>

<div v-click class="font-mono text-center">

```text
          columnas
          0   1   2
       ┌─────────────
fila 0 │ 12   7  18
fila 1 │  5  21  14
fila 2 │  8  11  25
```

</div>
</div>

---

# En Python: lista de listas

```python
matriz = [
    [12,  7, 18,  9],
    [ 5, 21, 14, 16],
    [ 8, 11, 25,  6],
    [19, 13, 10, 17]
]
```

<div class="grid grid-cols-2 gap-4 mt-4 text-center">
<div v-click class="card bg-blue-50 border border-blue-200"><code>matriz</code><div class="mt-2">Lista principal</div></div>
<div v-click class="card bg-violet-50 border border-violet-200"><code>matriz[i]</code><div class="mt-2">Una fila completa</div></div>
</div>

<div v-click class="mt-4 text-center"><strong>4 filas × 4 columnas = 16 elementos</strong></div>

---

# Índices: fila y columna

<div class="grid grid-cols-[90px_repeat(4,70px)] gap-1 mt-5 justify-center text-center font-mono">
<div></div><div class="font-bold text-slate-500">0</div><div class="font-bold text-slate-500">1</div><div class="font-bold text-violet-700">2</div><div class="font-bold text-slate-500">3</div>

<div class="font-bold text-slate-500 py-2">fila 0</div><div class="card !p-2">12</div><div class="card !p-2">7</div><div class="card !p-2">18</div><div class="card !p-2">9</div>
<div class="font-bold text-slate-500 py-2">fila 1</div><div class="card !p-2">5</div><div class="card !p-2">21</div><div class="card !p-2">14</div><div class="card !p-2">16</div>
<div class="font-bold text-violet-700 py-2">fila 2 →</div><div class="card !p-2">8</div><div class="card !p-2">11</div><div class="card !p-2 bg-violet-100 border-violet-300 font-bold">25</div><div class="card !p-2">6</div>
<div class="font-bold text-slate-500 py-2">fila 3</div><div class="card !p-2">19</div><div class="card !p-2">13</div><div class="card !p-2">10</div><div class="card !p-2">17</div>
</div>

<div v-click class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<span class="font-mono text-amber-300 text-xl">matriz[2][2] = 25</span>
<div class="!text-white text-sm mt-1">Primero indicamos la fila y después la columna.</div>
</div>

---

# Acceder y modificar una celda

```python
print(matriz[2][2])   # 25

matriz[2][2] = 30
```

<div class="grid grid-cols-2 gap-4 mt-5 text-center">
<div v-click class="card bg-blue-50 border border-blue-200">Acceso por posición<div class="font-black text-2xl mt-2">O(1)</div></div>
<div v-click class="card bg-violet-50 border border-violet-200">Modificación por posición<div class="font-black text-2xl mt-2">O(1)</div></div>
</div>

<div v-click class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Tener dos índices <strong>no significa O(n²)</strong>.
</div>

---

# Recorrer una fila

```python
for valor in matriz[0]:
    print(valor)
```

<div v-click class="mt-4 font-mono text-center">12 → 7 → 18 → 9</div>

<div v-click class="mt-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-center">
Si la fila tiene c columnas → <strong>O(c)</strong>.<br>
En una matriz n × n → <strong>O(n)</strong>.
</div>

---

# Recorrer una columna

```python
for fila in matriz:
    print(fila[0])
```

<div v-click class="mt-4 font-mono text-center">

```text
12
 5
 8
19
```

</div>

<div v-click class="mt-3 text-center">Visitamos un elemento por fila → <strong>O(n)</strong> en una matriz n × n.</div>

---

# Recorrer toda la matriz

```python
for fila in matriz:
    for valor in fila:
        print(valor)
```

<div class="grid grid-cols-2 gap-4 mt-5 text-center">
<div v-click class="card bg-blue-50 border border-blue-200">Caso general<div class="font-black text-2xl mt-2">O(f · c)</div><div class="text-sm mt-1">f filas, c columnas</div></div>
<div v-click class="card bg-violet-50 border border-violet-200">Matriz n × n<div class="font-black text-3xl mt-2">O(n²)</div></div>
</div>

<div v-click class="mt-4 text-center text-sm">No es “dos for = O(n²)”; depende del número de iteraciones.</div>

---

# Suma y promedio de una fila

```python
fila = matriz[0]

suma = sum(fila)
promedio = sum(fila) / len(fila)
```

<div class="grid grid-cols-2 gap-4 mt-5 text-center">
<div v-click class="card bg-amber-50 border border-amber-200"><code>sum(fila)</code><div class="font-black text-xl mt-2">O(n)</div></div>
<div v-click class="card bg-blue-50 border border-blue-200"><code>len(fila)</code><div class="font-black text-xl mt-2">O(1)</div></div>
</div>

<div v-click class="mt-4 text-center">El recorrido de la fila domina → <strong>O(n)</strong>.</div>

---

# Suma o promedio de todas las filas

```python
for fila in matriz:
    promedio = sum(fila) / len(fila)
    print(promedio)
```

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="!text-white">n filas × n elementos procesados por <code>sum()</code></div>
<div class="font-black text-3xl text-amber-300 mt-2">O(n²)</div>
</div>

---

# Buscar el valor máximo

```python
mayor = matriz[0][0]

for fila in matriz:
    for valor in fila:
        if valor > mayor:
            mayor = valor
```

<div v-click class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
Para garantizar el máximo debemos considerar todos los elementos.
<div class="font-black text-3xl text-amber-700 mt-2">O(n²)</div>
</div>

---

# Resumen · Matrices con listas de listas

| Operación | Matriz n × n |
|---|---:|
| Acceder `matriz[i][j]` | O(1) |
| Modificar `matriz[i][j]` | O(1) |
| Recorrer una fila | O(n) |
| Recorrer una columna | O(n) |
| Sumar / promediar una fila | O(n) |
| Recorrer toda la matriz | O(n²) |
| Buscar el máximo | O(n²) |

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---
<div class="max-w-3xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Práctica · Matrices</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">Temperaturas de varios días</h1>
<div class="mt-4 text-lg text-slate-200">Acceso · modificación · recorridos · promedio · máximo</div>
</div>

---

# Práctica · 1 · Crear la matriz

```python
temperaturas = [
    [24,27,29,31,28],
    [23,26,30,32,29],
    [25,28,31,33,30]
]
```

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center !text-white">
¿Qué representa cada lista interna? ¿Cuántas filas y columnas tenemos?
</div>

---

# Práctica · 2 · Acceder y modificar

```python
print(temperaturas[1][3])   # O(1)

temperaturas[1][3] = 40     # O(1)
print(temperaturas)
```

<div v-click class="mt-5 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Conocemos la posición exacta: no recorremos la matriz.
</div>

---

# Práctica · 3 · Recorrer una fila

```python
for t in temperaturas[0]:
    print(t)
```

<div v-click class="mt-5 text-center">Una fila → <strong>O(n)</strong> para n columnas.</div>

---

# Práctica · 4 · Recorrer toda la matriz

```python
for fila in temperaturas:
    for t in fila:
        print(t)
```

<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center">
<div class="!text-white">Matriz n × n:</div>
<div class="font-black text-3xl text-amber-300 mt-2">O(n²)</div>
</div>

---

# Práctica · 5 · Promedio del lunes

```python
lunes = temperaturas[0]
promedio_temp_lunes = sum(lunes) / len(lunes)

print(promedio_temp_lunes)
```

<div v-click class="mt-5 text-center"><code>sum()</code> recorre la fila → <strong>O(n)</strong></div>

---

# Práctica · 6 · Promedio de cada día

```python
for fila in temperaturas:
    promedio = sum(fila) / len(fila)
    print(promedio)
```

<div v-click class="mt-5 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">
n filas × n elementos por fila → <strong>O(n²)</strong>
</div>

---

# Práctica · 7 · Temperatura mayor

```python
mayor = temperaturas[0][0]

for fila in temperaturas:
    for t in fila:
        if t > mayor:
            mayor = t

print("Temperatura mayor:", mayor)
```

<div v-click class="mt-4 text-center">Recorrido completo → <strong>O(n²)</strong></div>

---

# Reto · Matrices

```python
matriz = [
    [12,  7, 18,  9],
    [ 5, 21, 14, 16],
    [ 8, 11, 25,  6],
    [19, 13, 10, 17]
]
```

<div class="grid grid-cols-2 gap-3 mt-3">
<div v-click class="card bg-blue-50 border border-blue-200">Imprime únicamente la <strong>columna 0</strong>.</div>
<div v-click class="card bg-violet-50 border border-violet-200">Obtén la <strong>suma de cada fila</strong>.</div>
<div v-click class="card bg-amber-50 border border-amber-200">Encuentra el <strong>valor máximo</strong> sin usar <code>max()</code>.</div>
<div v-click class="card bg-green-50 border border-green-200">Indica la <strong>complejidad</strong> de cada solución.</div>
</div>

---

# Práctica extracurricular · Matrices con NumPy

<div class="grid grid-cols-2 gap-5 mt-3">
<div>

```python
matriz = [
    [12,  7, 18,  9],
    [ 5, 21, 14, 16],
    [ 8, 11, 25,  6],
    [19, 13, 10, 17]
]
```

<div class="mt-3 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center text-sm">
Implementa esta matriz utilizando <strong>NumPy</strong>.
</div>
</div>

<div class="card bg-amber-50 border border-amber-200">
<div class="card-title text-amber-800">La práctica debe incluir</div>
<div class="text-sm leading-6">
① Crear la matriz como un arreglo NumPy.<br>
② Mostrar sus dimensiones y tamaño.<br>
③ Acceder a un elemento específico.<br>
④ Modificar un elemento.<br>
⑤ Obtener una fila completa.<br>
⑥ Obtener una columna completa.<br>
⑦ Calcular la suma de cada fila.<br>
⑧ Calcular la suma de cada columna.<br>
⑨ Calcular el promedio de cada fila.<br>
⑩ Obtener el valor máximo y el mínimo.<br>
⑪ Indicar la posición del valor máximo.<br>
⑫ Explicar la complejidad de las operaciones realizadas.
</div>
</div>
</div>

<div v-click class="mt-4 p-3 rounded-xl bg-slate-900 text-center !text-white">
Entrega: código ejecutable + resultados obtenidos + breve análisis de complejidad.
</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Tema 2 · Estructuras de datos</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">2.1.4 Pilas</h1>
<div class="mt-3 text-lg text-slate-200">TDA restringido basado en LIFO</div>
</div>

---

# Pila como TDA

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="font-mono text-center text-lg">

```text
          TOPE
            ↓
       ┌─────────┐
       │    D    │
       ├─────────┤
       │    C    │
       ├─────────┤
       │    B    │
       ├─────────┤
       │    A    │
       └─────────┘
```
</div>
<div class="card bg-violet-50 border border-violet-200 text-center flex flex-col justify-center"><div class="font-black text-4xl text-violet-700">LIFO</div><div class="mt-3"><strong>Last In, First Out</strong></div><div class="mt-2">El último en entrar es el primero en salir.</div></div>
</div>

---

# Operaciones fundamentales

| Operación | Función | Costo esperado |
|---|---|---:|
| **Push** | Inserta en el tope | O(1) |
| **Pop** | Elimina y devuelve el tope | O(1) |
| **Peek / Top** | Consulta el tope | O(1) |
| **isEmpty** | Comprueba si está vacía | O(1) |
| **Size** | Cantidad de elementos | O(1) |

<div v-click class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">La pila restringe el acceso: trabajamos directamente sobre el <strong>tope</strong>.</div>

---

# ¿Qué pasa con un elemento interno?

```text
TOPE → [ D ]
       [ C ]
       [ B ] ← queremos llegar aquí
       [ A ]
```

<div v-click class="mt-4 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center">Respetando el TDA: <strong>POP D → POP C → B queda en el tope</strong>.</div>
<div v-click class="mt-4 text-center">En el peor caso se procesan n elementos → <strong>O(n)</strong>.</div>

---

# Pila en Python

```python
pila = []

pila.append("A")   # PUSH
pila.append("B")
pila.append("C")

print(pila[-1])    # PEEK / TOP
pila.pop()         # POP
print(len(pila))   # SIZE
```

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">Python proporciona una <code>list</code>; nosotros imponemos la disciplina <strong>LIFO</strong>.</div>

---

# TDA Pila ↔ Python

| TDA | Con `list` |
|---|---|
| `push(x)` | `pila.append(x)` |
| `pop()` | `pila.pop()` |
| `peek()` / `top()` | `pila[-1]` |
| `isEmpty()` | `len(pila) == 0` |
| `size()` | `len(pila)` |

<div v-click class="mt-4 text-center text-sm">Con una lista, <code>append()</code> es O(1) amortizado; <code>pop()</code> al final y <code>[-1]</code> son O(1).</div>

---

# Python lo permite... pero no como pila

<div class="grid grid-cols-2 gap-5 mt-4">
<div class="card bg-green-50 border border-green-200"><strong>✓ Usar</strong>

```python
pila.append(x)
pila.pop()
pila[-1]
len(pila)
```
</div>
<div v-click class="card bg-red-50 border border-red-200"><strong>✗ Evitar como TDA Pila</strong>

```python
pila.insert(i, x)
pila.remove(x)
pila.pop(i)
pila[i]
pila[i] = x
pila.index(x)
```
</div>
</div>

---

# Buscar no es una operación básica

<div class="grid grid-cols-2 gap-5 mt-4">
<div class="card bg-amber-50 border border-amber-200">
<strong>Como TDA</strong>
<div class="mt-3 text-sm">Desapilamos hasta alcanzar el elemento. Para conservar la pila puede utilizarse una pila auxiliar.</div>
</div>

<div v-click class="card bg-violet-50 border border-violet-200">
<strong>Como <code>list</code> de Python</strong>
<div class="mt-3 font-mono bg-white/70 rounded-lg p-3">"B" in pila<br>pila.index("B")</div>
<div class="mt-3 text-sm">Python lo permite, pero son operaciones de <code>list</code>, no de la interfaz fundamental de una pila.</div>
</div>
</div>

<div v-click class="mt-5 p-3 rounded-xl bg-slate-900 text-center">
<span class="!text-white">En el peor caso revisamos n elementos:</span>
<span class="font-black text-2xl text-amber-300 ml-2">O(n)</span>
</div>

---

# ¿Por qué son importantes?

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="card bg-blue-50 border border-blue-200"><strong>Llamadas a funciones</strong><br><span class="text-sm">La última llamada pendiente se resuelve primero.</span></div>
<div v-click class="card bg-violet-50 border border-violet-200"><strong>Deshacer</strong><br><span class="text-sm">La última acción es la primera que se revierte.</span></div>
<div v-click class="card bg-amber-50 border border-amber-200"><strong>Evaluación de expresiones</strong><br><span class="text-sm">Paréntesis y operadores.</span></div>
<div v-click class="card bg-green-50 border border-green-200"><strong>Backtracking</strong><br><span class="text-sm">Regresar al último estado pendiente.</span></div>
</div>

---
background: /background3.jpg
class: text-center flex items-center justify-center h-full
transition: slide-left
---
<div class="max-w-3xl mx-auto p-8 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/10 shadow-2xl text-white">
<span class="text-xs font-mono font-bold uppercase tracking-widest text-amber-400">Práctica guiada · Pilas</span>
<h1 class="text-4xl font-black mt-4 bg-gradient-to-r from-amber-200 via-orange-300 to-amber-400 bg-clip-text text-transparent">Validación de paréntesis</h1>
<div class="mt-4 text-lg text-slate-200">Un problema donde LIFO es necesario</div>
</div>

---

# El problema

<div class="grid grid-cols-2 gap-5 mt-4">
<div class="card bg-green-50 border border-green-200 text-center"><div class="font-mono text-2xl">(a + b) * (c - d)</div><div class="mt-3 font-bold text-green-700">✓ Balanceada</div></div>
<div v-click class="card bg-red-50 border border-red-200 text-center"><div class="font-mono text-2xl">(a + b)) * (c - d</div><div class="mt-3 font-bold text-red-700">✗ No balanceada</div></div>
</div>
<div v-click class="mt-5 p-4 rounded-xl bg-slate-900 text-center !text-white">¿Cómo recordar cada paréntesis abierto y cerrarlo en el orden correcto?</div>

---

# Paso 1 · Apilar aperturas

```python
expresion = "(a + b) * (c - d)"
pila = []

for caracter in expresion:
    if caracter == "(":
        pila.append(caracter)
```

<div v-click class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">Cada <code>(</code> queda pendiente de ser cerrado.</div>

---

# Paso 2 · Procesar cierres

```python
elif caracter == ")":
    if len(pila) == 0:
        print("No balanceada")
        break

    pila.pop()
```

<div v-click class="mt-4 p-3 rounded-xl bg-violet-50 border border-violet-200 text-center">Si aparece <code>)</code> con la pila vacía, no existe una apertura pendiente.</div>

---

# Paso 3 · Solución completa

```python
expresion = "(a + b) * (c - d)"
pila = []
valida = True

for caracter in expresion:
    if caracter == "(":
        pila.append(caracter)
    elif caracter == ")":
        if len(pila) == 0:
            valida = False
            break
        pila.pop()

if len(pila) != 0:
    valida = False

print("Balanceada" if valida else "No balanceada")
```

---

# Cierre · Pilas

<div class="grid grid-cols-3 gap-3 mt-5 text-center">
<div class="card bg-blue-50 border border-blue-200"><strong>Regla</strong><div class="font-black text-2xl text-violet-700 mt-2">LIFO</div></div>
<div class="card bg-violet-50 border border-violet-200"><strong>Acceso</strong><div class="font-black text-2xl text-violet-700 mt-2">TOPE</div></div>
<div class="card bg-amber-50 border border-amber-200"><strong>Operaciones</strong><div class="font-bold mt-2">push · pop · peek</div></div>
</div>
<div v-click class="mt-6 p-4 rounded-xl bg-slate-900 text-center !text-white">Una pila es útil cuando el problema exige recuperar información en <strong>orden inverso al que fue incorporada</strong>.</div>
