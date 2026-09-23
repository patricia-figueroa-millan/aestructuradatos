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
