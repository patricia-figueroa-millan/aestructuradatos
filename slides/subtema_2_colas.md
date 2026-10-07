---
layout: cover
---

# Colas
## Estructura de datos FIFO

<div class="mt-8 p-5 rounded-2xl bg-violet-50 border border-violet-200">
  <p class="text-xl"><strong>Idea clave:</strong> el primero en entrar es el primero en salir.</p>
  <p class="mt-2 text-slate-600">FIFO — <em>First In, First Out</em></p>
</div>

---
layout: default
---

# ¿Qué es una cola?

Una <strong>cola (queue)</strong> es una estructura de datos lineal en la que los elementos se procesan en el <strong>mismo orden en que llegan</strong>.

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
  <div class="text-3xl font-bold text-violet-700">FIFO</div>
  <div class="mt-1 text-lg">First In, First Out</div>
  <div class="mt-2 text-slate-600">El primero en entrar es el primero en salir.</div>
</div>

<div class="mt-6 flex items-center justify-center gap-2 text-center">
  <div class="text-sm text-slate-500 mr-2">SALE</div>
  <div class="px-5 py-3 rounded-xl bg-amber-100 border border-amber-300 font-bold">Ana</div>
  <div class="px-5 py-3 rounded-xl bg-blue-50 border border-blue-200">Luis</div>
  <div class="px-5 py-3 rounded-xl bg-blue-50 border border-blue-200">Carlos</div>
  <div class="px-5 py-3 rounded-xl bg-blue-50 border border-blue-200">Elena</div>
  <div class="text-sm text-slate-500 ml-2">ENTRA</div>
</div>

<div class="grid grid-cols-2 gap-4 mt-5">
  <div class="card text-center">
    <strong>Frente</strong>
    <p class="text-sm mt-1">Elemento que será atendido primero.</p>
  </div>
  <div class="card text-center">
    <strong>Final</strong>
    <p class="text-sm mt-1">Lugar donde se agregan nuevos elementos.</p>
  </div>
</div>

---
layout: default
---

# Cola vs. pila

<div class="grid grid-cols-2 gap-6 mt-6">

<div class="card">

### Pila

<div class="text-center my-4">
  <div class="text-3xl font-bold text-violet-700">LIFO</div>
  <div>Last In, First Out</div>
</div>

- El último en entrar sale primero.
- Se inserta y elimina por el mismo extremo.
- Operaciones: `push` y `pop`.

</div>

<div class="card">

### Cola

<div class="text-center my-4">
  <div class="text-3xl font-bold text-blue-700">FIFO</div>
  <div>First In, First Out</div>
</div>

- El primero en entrar sale primero.
- Se inserta al final.
- Se elimina desde el frente.
- Operaciones: `enqueue` y `dequeue`.

</div>

</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
  <strong>Pregunta:</strong> ¿en cuál estructura importa respetar el orden de llegada?
</div>

---
layout: default
---

# Operaciones de una cola

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="card">
  <div class="text-xl font-bold text-violet-700">enqueue(x)</div>
  <p>Agrega un elemento al <strong>final</strong> de la cola.</p>
</div>

<div class="card">
  <div class="text-xl font-bold text-violet-700">dequeue()</div>
  <p>Elimina y devuelve el elemento del <strong>frente</strong>.</p>
</div>

<div class="card">
  <div class="text-xl font-bold text-violet-700">front() / peek()</div>
  <p>Consulta el elemento del frente <strong>sin eliminarlo</strong>.</p>
</div>

<div class="card">
  <div class="text-xl font-bold text-violet-700">is_empty()</div>
  <p>Indica si la cola está vacía.</p>
</div>

</div>

<div class="mt-4 card">
  <div class="text-xl font-bold text-violet-700">size()</div>
  <p>Devuelve el número de elementos almacenados en la cola.</p>
</div>

---
layout: default
---

# ¿Cómo funcionan enqueue y dequeue?

<div class="mt-5">

### 1. Encolar — `enqueue("Elena")`

<div class="flex items-center justify-center gap-2 mt-3">
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Ana</div>
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Luis</div>
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Carlos</div>
  <div class="text-2xl">←</div>
  <div class="px-4 py-3 rounded-xl bg-green-50 border border-green-200 font-bold">Elena</div>
</div>

### 2. Desencolar — `dequeue()`

<div class="flex items-center justify-center gap-2 mt-3">
  <div class="px-4 py-3 rounded-xl bg-amber-50 border border-amber-300 font-bold">Ana</div>
  <div class="text-2xl">←</div>
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Luis</div>
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Carlos</div>
  <div class="px-4 py-3 rounded-xl bg-blue-50 border border-blue-200">Elena</div>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
  <strong>Entra por el final · Sale por el frente</strong>
</div>

---
layout: default
---

# ¿Para qué se utiliza una cola?

Una cola es útil cuando necesitamos <strong>procesar elementos respetando su orden de llegada</strong>.

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="card">
  <strong>🖨️ Cola de impresión</strong>
  <p class="text-sm mt-1">Los documentos esperan su turno para imprimirse.</p>
</div>

<div class="card">
  <strong>👥 Sistemas de atención</strong>
  <p class="text-sm mt-1">Clientes, pacientes o solicitudes esperan para ser atendidos.</p>
</div>

<div class="card">
  <strong>💻 Procesamiento de tareas</strong>
  <p class="text-sm mt-1">Tareas pendientes se ejecutan según su llegada.</p>
</div>

<div class="card">
  <strong>🌐 Redes y servidores</strong>
  <p class="text-sm mt-1">Mensajes, paquetes o solicitudes esperan procesamiento.</p>
</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">
  <strong>También aparece en algoritmos:</strong> por ejemplo, en el recorrido en anchura de grafos (BFS).
</div>

---
layout: default
---

# Implementación en Python: ¿con una lista?

Podemos intentar representar una cola con una lista:

```python
cola = []

cola.append("Ana")
cola.append("Luis")
cola.append("Carlos")

print(cola)
```

Resultado:

```text
['Ana', 'Luis', 'Carlos']
```

<div class="mt-4 p-4 rounded-xl bg-green-50 border border-green-200">

### Para encolar funciona bien

```python
cola.append("Elena")
```

`append()` agrega al final en <strong>O(1) amortizado</strong>.

</div>

---
layout: default
---

# ¿Y para desencolar?

Con una lista podríamos hacer:

```python
cola = ["Ana", "Luis", "Carlos", "Elena"]

atendido = cola.pop(0)
```

<div class="mt-4 text-center font-mono">
  [Ana] [Luis] [Carlos] [Elena]
</div>

<div class="mt-2 text-center text-2xl">↓ `pop(0)`</div>

<div class="mt-2 text-center font-mono">
  [Luis] [Carlos] [Elena]
</div>

<div class="mt-5 p-4 rounded-xl bg-red-50 border border-red-200">
  <strong>Problema:</strong> al eliminar la posición 0, los elementos restantes deben desplazarse una posición.
</div>

<div class="mt-4 text-center">
  <span class="px-5 py-2 rounded-xl bg-slate-900 text-white font-mono text-xl">pop(0) → O(n)</span>
</div>

---
layout: default
---

# Entonces, ¿qué sí utilizamos?

Python proporciona `deque` en el módulo `collections`.

```python
from collections import deque

cola = deque()
```

<div class="grid grid-cols-2 gap-5 mt-5">

<div class="card">

### Encolar

```python
cola.append("Ana")
cola.append("Luis")
```

<div class="mt-3 text-center font-mono font-bold">append() → O(1)</div>

</div>

<div class="card">

### Desencolar

```python
atendido = cola.popleft()
```

<div class="mt-3 text-center font-mono font-bold">popleft() → O(1)</div>

</div>

</div>

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200">
  <strong>deque</strong> = <em>double-ended queue</em>. Permite agregar y eliminar eficientemente en ambos extremos.
</div>

---
layout: default
---

# ¿Qué sí y qué no?

| Necesidad | Evitar | Recomendado |
|---|---|---|
| Crear la cola | `cola = []` | `cola = deque()` |
| Encolar | `append()` ✓ | `append()` ✓ |
| Desencolar | `pop(0)` ❌ O(n) | `popleft()` ✓ O(1) |
| Ver el frente | `cola[0]` | `cola[0]` |
| Saber si está vacía | `len(cola) == 0` | `len(cola) == 0` |
| Tamaño | `len(cola)` | `len(cola)` |

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
  <strong>Una lista puede comportarse como cola, pero `deque` es más adecuada para implementarla eficientemente.</strong>
</div>

---
layout: default
---

# Práctica guiada: nuestra primera cola

```python
from collections import deque

cola = deque()

cola.append("Ana")
cola.append("Luis")
cola.append("Carlos")

print(cola)

atendido = cola.popleft()

print("Se atendió a:", atendido)
print("Cola:", cola)

print("Siguiente:", cola[0])
```

<div class="mt-5 p-4 rounded-xl bg-violet-50 border border-violet-200">

### Antes de ejecutar

1. ¿Quién será atendido?
2. ¿Cómo quedará la cola?
3. ¿Quién será el siguiente?

</div>

---
layout: default
---

# Corrida a mano

<div class="mt-5">

| Instrucción | Acción | Estado de la cola |
|---|---|---|
| `cola = deque()` | Crear cola | `[]` |
| `append("Ana")` | Entra Ana | `[Ana]` |
| `append("Luis")` | Entra Luis | `[Ana, Luis]` |
| `append("Carlos")` | Entra Carlos | `[Ana, Luis, Carlos]` |
| `popleft()` | Sale Ana | `[Luis, Carlos]` |
| `cola[0]` | Consultar frente | `[Luis, Carlos]` |

</div>

<div class="mt-6 grid grid-cols-2 gap-4">
  <div class="card text-center">
    <div class="text-sm text-slate-500">ATENDIDO</div>
    <div class="text-2xl font-bold mt-1">Ana</div>
  </div>
  <div class="card text-center">
    <div class="text-sm text-slate-500">SIGUIENTE</div>
    <div class="text-2xl font-bold mt-1">Luis</div>
  </div>
</div>

---
layout: default
---

# Caso práctico: sistema de atención

Un módulo atiende a las personas en el <strong>orden en que llegan</strong>.

Los eventos del día son:

```python
eventos = [
    ("llega", "Ana"),
    ("llega", "Luis"),
    ("atiende", None),
    ("llega", "Carlos"),
    ("llega", "Elena"),
    ("atiende", None),
    ("atiende", None),
]
```

<div class="mt-5 p-4 rounded-xl bg-amber-50 border border-amber-200">

### Antes de programar

- ¿Quién será atendido primero?
- ¿En qué orden serán atendidos?
- ¿Quién quedará esperando al finalizar?
- ¿Qué estructura de datos necesitamos?

</div>

---
layout: default
---

# Algoritmo

Para cada evento:

<div class="mt-5 space-y-3">

<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">
  <strong>Si llega una persona</strong> → agregarla al final de la cola.
</div>

<div class="p-4 rounded-xl bg-violet-50 border border-violet-200">
  <strong>Si se solicita atender</strong> → retirar a la persona del frente.
</div>

<div class="p-4 rounded-xl bg-red-50 border border-red-200">
  <strong>Pero...</strong> antes de atender debemos comprobar que exista alguien esperando.
</div>

</div>

<div class="mt-6 text-center font-mono text-lg">
llega → append() &nbsp;&nbsp;&nbsp; atiende → popleft()
</div>

---
layout: default
---

# Implementación en Python

```python
from collections import deque

eventos = [
    ("llega", "Ana"),
    ("llega", "Luis"),
    ("atiende", None),
    ("llega", "Carlos"),
    ("llega", "Elena"),
    ("atiende", None),
    ("atiende", None),
]

cola = deque()

for evento, persona in eventos:

    if evento == "llega":
        cola.append(persona)
        print(persona, "entra a la cola")

    elif evento == "atiende":
        if len(cola) == 0:
            print("No hay personas esperando")
        else:
            atendido = cola.popleft()
            print("Se atiende a:", atendido)

    print("Cola:", list(cola))
```

---
layout: default
---

# ¿Qué ocurre en cada evento?

<div class="mt-4">

| Paso | Evento | Operación | Sale | Estado de la cola |
|---:|---|---|---|---|
| 1 | llega Ana | `append("Ana")` | — | `[Ana]` |
| 2 | llega Luis | `append("Luis")` | — | `[Ana, Luis]` |
| 3 | atiende | `popleft()` | Ana | `[Luis]` |
| 4 | llega Carlos | `append("Carlos")` | — | `[Luis, Carlos]` |
| 5 | llega Elena | `append("Elena")` | — | `[Luis, Carlos, Elena]` |
| 6 | atiende | `popleft()` | Luis | `[Carlos, Elena]` |
| 7 | atiende | `popleft()` | Carlos | `[Elena]` |

</div>

<div class="mt-5 p-4 rounded-xl bg-green-50 border border-green-200 text-center">
  <strong>Orden de atención:</strong> Ana → Luis → Carlos<br>
  <strong>Continúa esperando:</strong> Elena
</div>

---
layout: default
---

# ¿Por qué comprobamos si la cola está vacía?

Observa:

```python
elif evento == "atiende":

    if len(cola) == 0:
        print("No hay personas esperando")
    else:
        atendido = cola.popleft()
```

¿Qué ocurriría con estos eventos?

```python
eventos = [
    ("atiende", None),
    ("llega", "Ana"),
]
```

<div class="mt-5 p-4 rounded-xl bg-red-50 border border-red-200">
  Al iniciar, la cola está vacía. No podemos ejecutar `popleft()` si no existe ningún elemento que retirar.
</div>

<div class="mt-5 text-center">
  <span class="font-mono px-5 py-2 rounded-xl bg-slate-900 text-white">cola vacía + popleft() → error</span>
</div>

---
layout: default
---

# Analicemos la complejidad

Si existen `n` eventos:

```python
for evento, persona in eventos:
```

cada evento se procesa una sola vez.

<div class="grid grid-cols-3 gap-4 mt-5">

<div class="card text-center">
  <div class="font-mono text-xl font-bold">append()</div>
  <div class="mt-2 text-2xl text-violet-700">O(1)</div>
</div>

<div class="card text-center">
  <div class="font-mono text-xl font-bold">popleft()</div>
  <div class="mt-2 text-2xl text-violet-700">O(1)</div>
</div>

<div class="card text-center">
  <div class="font-mono text-xl font-bold">len()</div>
  <div class="mt-2 text-2xl text-violet-700">O(1)</div>
</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-5">
  <div class="p-4 rounded-xl bg-blue-50 border border-blue-200 text-center">
    <strong>Tiempo total</strong>
    <div class="font-mono text-2xl mt-1">O(n)</div>
  </div>
  <div class="p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
    <strong>Espacio — peor caso</strong>
    <div class="font-mono text-2xl mt-1">O(n)</div>
  </div>
</div>

---
layout: default
---

# ¿Cuál sería el peor caso de espacio?

Supongamos que todas las personas llegan y nadie es atendido:

```text
llega Ana
llega Luis
llega Carlos
llega Elena
llega Pedro
...
```

La cola crece:

```text
[Ana]

[Ana, Luis]

[Ana, Luis, Carlos]

[Ana, Luis, Carlos, Elena]

...
```

<div class="mt-6 p-4 rounded-xl bg-violet-50 border border-violet-200 text-center">
  Si llegan <strong>n</strong> personas y ninguna sale, la cola puede almacenar <strong>n elementos</strong>.
  <div class="mt-2 font-mono text-2xl font-bold">Espacio → O(n)</div>
</div>

---
layout: default
---

# Cierre: lo esencial de una cola

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="card">
  <strong>Regla</strong>
  <div class="text-2xl font-bold text-violet-700 mt-2">FIFO</div>
  <p>Primero en entrar, primero en salir.</p>
</div>

<div class="card">
  <strong>Extremos</strong>
  <p class="mt-2">Se agrega por el <strong>final</strong> y se elimina por el <strong>frente</strong>.</p>
</div>

<div class="card">
  <strong>Python</strong>
  <div class="font-mono mt-2">collections.deque</div>
  <p>`append()` + `popleft()`</p>
</div>

<div class="card">
  <strong>Eficiencia</strong>
  <p class="mt-2">Evitar `list.pop(0)` porque requiere <strong>O(n)</strong>.</p>
</div>

</div>

<div class="mt-6 p-4 rounded-xl bg-amber-50 border border-amber-200 text-center">
  <strong>Pregunta final:</strong> si una aplicación debe respetar estrictamente el orden de llegada, ¿qué estructura elegirías y por qué?
</div>
