# 2.1.6 Punteros y referencias

> **Idea central:** en Python trabajaremos con referencias a objetos. Esto nos permitirá comprender cómo se conectan nodos y, posteriormente, estructuras como árboles.

---

# 1. Memoria: variables y objetos

Cuando ejecutamos:

```python
numero = 25
```

podemos representarlo conceptualmente así:

<div class="mt-6 flex items-center justify-center gap-6">
  <div class="px-6 py-4 rounded-xl bg-violet-50 border border-violet-200 font-mono text-xl">numero</div>
  <div class="text-4xl">→</div>
  <div class="px-7 py-4 rounded-xl bg-blue-50 border border-blue-200 font-mono text-xl">25</div>
</div>

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200">
En Python, una variable puede entenderse como un <strong>nombre asociado a una referencia hacia un objeto</strong>.
</div>

---

# ¿Qué es una referencia?

Una **referencia** permite acceder a un objeto desde una variable.

```python
lista = [10, 20, 30]
```

<div class="mt-6 text-center font-mono text-2xl">
lista → [10, 20, 30]
</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200">
<strong>Importante:</strong> en Python no necesitamos conocer ni modificar directamente la dirección de memoria del objeto.
</div>

---

# ¿Y qué es un puntero?

En términos generales, un **puntero** es una variable cuyo valor representa una dirección de memoria.

<div class="grid grid-cols-2 gap-5 mt-6">
<div class="card">
<strong>C/C++</strong>
<p class="mt-2">Permiten trabajar explícitamente con direcciones y punteros.</p>
</div>
<div class="card">
<strong>Python</strong>
<p class="mt-2">Trabaja con referencias a objetos.</p>
</div>
</div>

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
Para esta asignatura nos interesa comprender la <strong>referencia y el enlace entre objetos</strong>.
</div>

---

# 2. Varias variables pueden referenciar el mismo objeto

```python
lista1 = [10, 20, 30]
lista2 = lista1
```

<div class="mt-6 text-center font-mono text-xl">
lista1 ──┐<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──→ [10, 20, 30]<br>
lista2 ──┘
</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
<strong>Pregunta:</strong> ¿<code>lista2 = lista1</code> creó una copia?
</div>

---

# No se creó una copia

```python
lista1 = [10, 20, 30]
lista2 = lista1
lista2.append(40)

print(lista1)
print(lista2)
```

Resultado:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200">
Ambas variables <strong>referencian el mismo objeto</strong>. Una modificación mediante <code>lista2</code> también se observa desde <code>lista1</code>.
</div>

---

# Aliasing

Cuando dos o más variables hacen referencia al **mismo objeto**, existe **aliasing**.

```python
datos = [5, 8, 12]
respaldo = datos
respaldo.append(20)
```

<div class="mt-5 text-center font-mono text-xl">
datos ─────┐<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──→ [5, 8, 12, 20]<br>
respaldo ──┘
</div>

<div class="mt-5 p-4 rounded-xl bg-red-50 border border-red-200 text-center">
<strong>Asignar otra variable ≠ copiar el objeto</strong>
</div>

---

# ¿Y si realmente quiero una copia?

```python
lista1 = [10, 20, 30]
lista2 = lista1.copy()

lista2.append(40)
```

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="card text-center font-mono">lista1 → [10, 20, 30]</div>
<div class="card text-center font-mono">lista2 → [10, 20, 30, 40]</div>
</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
Ahora existen <strong>dos objetos diferentes</strong>.
</div>

---

# `==` vs. `is`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
```

<div class="grid grid-cols-2 gap-5 mt-5">
<div class="card">

### `==`
Compara el **contenido o valor**.

```python
a == b   # True
```
</div>

<div class="card">

### `is`
Comprueba si es el **mismo objeto**.

```python
a is b   # False
a is c   # True
```
</div>
</div>

---

# Comprueba: `==` o `is`

```python
a = [5, 10]
b = [5, 10]
c = a
```

Predice:

```python
a == b
a is b
a == c
a is c
```

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200">
<strong>Pregúntate:</strong> ¿tienen el mismo contenido? ¿son el mismo objeto?
</div>

---

# `None`: ausencia de una referencia

En estructuras enlazadas necesitaremos representar que **no existe otro objeto** al cual continuar.

```python
siguiente = None
```

<div class="mt-5 text-center font-mono text-2xl">
siguiente → None
</div>

Para comprobarlo:

```python
if siguiente is None:
    print("No hay siguiente elemento")
```

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">
Podemos interpretar <code>None</code> como: <strong>“no existe un siguiente objeto”</strong>.
</div>

---

# 3. Una referencia puede apuntar a otro objeto

Hasta ahora:

<div class="mt-4 text-center font-mono text-xl">
variable → objeto
</div>

Pero un objeto también puede contener una **referencia hacia otro objeto**:

<div class="mt-7 text-center font-mono text-2xl">
objeto A ─────→ objeto B
</div>

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200">
Esto permite construir estructuras cuyos elementos están <strong>conectados entre sí</strong>.
</div>

---

# Nodo: dato + referencia

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
```

<div class="grid grid-cols-2 gap-5 mt-5">
<div class="card text-center">
<strong>dato</strong>
<p class="mt-2">Información almacenada.</p>
</div>
<div class="card text-center">
<strong>siguiente</strong>
<p class="mt-2">Referencia hacia otro nodo.</p>
</div>
</div>

<div class="mt-6 text-center font-mono text-2xl">
[ dato: 10 | siguiente: None ]
</div>

---

# Creamos y enlazamos dos nodos

```python
nodo1 = Nodo(10)
nodo2 = Nodo(20)

nodo1.siguiente = nodo2
```

<div class="mt-7 text-center font-mono text-2xl">
nodo1 → [10 | ●] ─────→ [20 | None] ← nodo2
</div>

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200">
No copiamos <code>nodo2</code>. <code>nodo1.siguiente</code> guarda una <strong>referencia hacia ese objeto</strong>.
</div>

---

# ¿Qué significa el enlace?

```python
print(nodo1.dato)
# 10

print(nodo1.siguiente.dato)
# 20
```

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
<code>nodo1.siguiente</code><br>↓<br>
referencia a <code>nodo2</code><br>↓<br>
<code>nodo1.siguiente.dato</code> → <strong>20</strong>
</div>

---

# Construimos una cadena de nodos

```python
n1 = Nodo(10)
n2 = Nodo(20)
n3 = Nodo(30)

n1.siguiente = n2
n2.siguiente = n3
```

<div class="mt-7 text-center font-mono text-2xl">
n1 → [10 | ●] ─→ [20 | ●] ─→ [30 | None] ← n3
</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200">
La conexión lógica entre los nodos se establece mediante <strong>referencias</strong>.
</div>

---

# ¿Cómo recorremos los nodos?

```python
actual = n1

while actual is not None:
    print(actual.dato)
    actual = actual.siguiente
```

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200">

### Idea del recorrido

```text
actual → n1 → n2 → n3 → None
```

1. Procesamos el nodo actual.
2. Avanzamos a `actual.siguiente`.
3. Terminamos cuando `actual is None`.

</div>

---

# Corrida a mano

| Iteración | `actual` referencia a | Imprime | `actual.siguiente` | Nuevo `actual` |
|---:|---|---:|---|---|
| 1 | `n1` | 10 | `n2` | `n2` |
| 2 | `n2` | 20 | `n3` | `n3` |
| 3 | `n3` | 30 | `None` | `None` |

<div class="mt-6 p-4 rounded-xl bg-green-50 border border-green-200 text-center">
Salida: <span class="font-mono font-bold">10 &nbsp; 20 &nbsp; 30</span>
</div>

<div class="mt-4 text-center">
Cuando <code>actual is None</code>, el ciclo termina.
</div>

---

# ¿Se modificó `n1` al recorrer?

Inicialmente:

```python
actual = n1
```

```text
n1 ─────┐
        ├──→ [10] → [20] → [30] → None
actual ─┘
```

Después:

```python
actual = actual.siguiente
```

solo cambia la referencia almacenada en `actual`.

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">
<strong>La estructura no se mueve.</strong> La referencia <code>actual</code> es la que va avanzando de nodo en nodo.
</div>

---

# 4. La misma idea aparecerá en árboles

En una cadena:

```text
[10] → [20] → [30]
```

En un árbol, un nodo puede contener referencias hacia **más de un nodo**:

<div class="mt-6 text-center font-mono text-2xl">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[50]<br>
&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\<br>
&nbsp;[20]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[70]
</div>

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200">
La idea fundamental no cambia: <strong>los objetos se conectan mediante referencias</strong>.
</div>

---

# Un nodo de un árbol

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
```

```python
raiz = Nodo(50)
raiz.izquierdo = Nodo(20)
raiz.derecho = Nodo(70)
```

<div class="mt-5 text-center font-mono text-2xl">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raiz<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[50]<br>
&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\<br>
&nbsp;[20]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[70]
</div>

---

# De referencias a estructuras dinámicas

<div class="mt-7 text-center text-xl font-bold">
Memoria → Referencias → Nodos → Enlaces → Estructuras dinámicas
</div>

<div class="mt-7 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
<strong>Idea clave:</strong> no necesitamos manipular direcciones de memoria directamente para construir estructuras conectadas en Python.
</div>

---

# Práctica guiada: construye y recorre

Construye mediante referencias:

```text
[5] → [12] → [18] → [25] → None
```

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

n1 = Nodo(5)
n2 = Nodo(12)
n3 = Nodo(18)
n4 = Nodo(25)

# Completa los enlaces
```

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">
<strong>Tarea:</strong> enlaza los nodos, crea una variable <code>actual</code>, recorre desde <code>n1</code> e imprime cada dato hasta llegar a <code>None</code>.
</div>

---

# Práctica: predice antes de ejecutar

```python
n1 = Nodo(10)
n2 = Nodo(20)
n3 = Nodo(30)

n1.siguiente = n2
n2.siguiente = n3

actual = n1.siguiente
actual.dato = 99
```

<div class="mt-6 p-5 rounded-xl bg-violet-50 border border-violet-200">

### Responde

1. ¿A qué nodo referencia `actual`?
2. ¿Cuál será ahora `n2.dato`?
3. ¿Qué imprimirá `n1.siguiente.dato`?
4. ¿Se creó una copia de `n2`?

</div>

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
Justifica utilizando los conceptos de <strong>referencia</strong> y <strong>aliasing</strong>.
</div>

---

# Lo esencial

<div class="grid grid-cols-2 gap-4 mt-5">
<div class="card"><strong>Referencia</strong><p class="mt-2">Permite acceder a un objeto.</p></div>
<div class="card"><strong>Aliasing</strong><p class="mt-2">Varias variables pueden referenciar el mismo objeto.</p></div>
<div class="card"><strong>`is` vs. `==`</strong><p class="mt-2"><code>is</code>: mismo objeto.<br><code>==</code>: mismo contenido/valor.</p></div>
<div class="card"><strong>`None`</strong><p class="mt-2">Puede representar la ausencia de un siguiente enlace.</p></div>
</div>

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
<strong>Un nodo puede almacenar una referencia hacia otro nodo.</strong><br>
Esta idea será fundamental cuando trabajemos con árboles.
</div>
