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
📧 patricia.figueroa@colima.tecnm.mx
</span>
<span class="bg-white/10 px-3 py-1.5 rounded-lg border border-white/10">
📸 instagram: @patricia.figueroa.tecnm.mx
</span>
</div>
</div>

</div>

---
transition: fade-out
---

# AGENDA

- 📝 **Presentación del Curso** 
- 📕 **Tema 1: Análisis y Diseño de Algoritmos** 
- 📕 **1.1. Definición de algoritmo y estructuras de datos.**
<br>
<br>

---
transition: fade-out
level: 2
---

# Presentación del Curso

Competencia de la asignatura de **Algoritmia y Estructura de Datos**:

<div class="my-4 p-3 bg-amber-100 dark:bg-amber-950/40 border-l-4 border-amber-400 rounded-r text-amber-900 dark:text-amber-100">
  Adquiere <b>conocimientos</b> sobre <b>algoritmos</b> y <b>estructuras de datos</b> y puede <b>aplicarlos eficazmente</b> para <b>resolver problemas complejos</b>.
</div>

Además, tiene la habilidad de **analizar críticamente** uso y aplicaciones de algoritmos y estructuras, **adaptándose** a diferentes contextos y requerimientos de **desarrollo de software**, con las siguientes competencias:

* **Diseña** algoritmos y estructuras para procesar datos en diversas plataformas.
* **Selecciona** lenguajes y paradigmas ideales para su implementación y optimización.
* **Aplica** tipos de datos y procedimientos algorítmicos básicos.
* **Optimiza** procesos mediante soluciones algorítmicas.
* **Facilita** búsquedas eficientes de información.

<div class="mt-4 p-3 bg-gray-100 dark:bg-gray-800 rounded-lg text-lg flex items-center justify-between border border-gray-300 dark:border-gray-700">
  <div class="flex items-center gap-2">
    <span>🏫</span> 
    <b>Código de Classroom:</b>
  </div>
  <code class="bg-amber-400 dark:bg-amber-500 text-gray-900 px-3 py-1 rounded-md font-mono font-bold shadow-sm">6zc7kldt</code>
</div>

---
layout: center
transition: fade-out
title: El Rol de la Asignatura en la Inteligencia Artificial
---

<div class="max-w-2xl mx-auto p-10 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Contexto -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-mono font-bold mb-4">
    <span></span> ENFOQUE Y APLICACIÓN
  </div>

  <!-- Título Principal -->
  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight leading-tight">
    El Rol de la Asignatura en la Inteligencia Artificial
  </h1>

</div>

---
transition: fade-out
layout: two-cols
title: La inteligencia artificial no es magia.
---

La Inteligencia Artificial no es magia; es **computación de alto rendimiento** aplicada.

- **Más allá de las cajas negras:** Un ingeniero en IA no solo consume bibliotecas de Machine Learning; diseña sistemas viables y optimizados en tiempo de ejecución y uso de memoria.
- **Razonamiento lógico:** Desarrollar la capacidad de abstracción para estructurar problemas complejos.
- **Eficiencia real:** Las soluciones de IA manejan miles de millones de parámetros; la correcta elección de algoritmos y estructuras determina si el modelo es viable en producción.

::right::

<div class="flex h-full items-center justify-center pl-4">
  <img 
    src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=400&q=60" 
    class="w-3/4 rounded-lg shadow-md" 
    alt="Imagen IA"
  />
</div>
---

# La Ecuación Fundamental de la Informática

En 1975, **Niklaus Wirth** sentó las bases del desarrollo de software moderno con su famosa fórmula:

<div class="flex flex-col items-center max-w-3xl mx-auto my-8 gap-2">
  
  <!-- Fila Superior: Algoritmos + Estructuras de Datos -->
  <div class="flex items-center w-full gap-4">
    <!-- Bloque 1: Algoritmos -->
    <div v-click="1" class="flex-1 border-2 border-blue-500/30 bg-blue-500/10 p-5 rounded-xl text-center shadow-sm">
      <h3 class="font-bold text-lg text-blue-500 mb-1">Algoritmos</h3>
      <p class="text-xs opacity-80 leading-relaxed">
        La lógica, las instrucciones de control y transformación.
      </p>
    </div>
    <!-- Signo Más -->
    <div v-click="2" class="text-3xl font-extrabold opacity-60 px-1">+</div>
    <!-- Bloque 2: Estructuras de Datos -->
    <div v-click="2" class="flex-1 border-2 border-indigo-500/30 bg-indigo-500/10 p-5 rounded-xl text-center shadow-sm">
      <h3 class="font-bold text-lg text-indigo-500 mb-1">Estructuras de Datos</h3>
      <p class="text-xs opacity-80 leading-relaxed">
        La organización, gestión y almacenamiento de la información.
      </p>
    </div>
  </div>

  <!-- Signo Igual -->
  <div v-click="3" class="text-3xl font-extrabold opacity-60 my-1">=</div>

  <!-- Banner Inferior: Programas -->
  <div v-click="3" class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-4 px-6 rounded-xl shadow-lg text-center">
    <span class="text-2xl font-black uppercase tracking-wider text-white">Programas</span>
  </div>

</div>

---
layout: center
transition: fade-out
---

<div class="max-w-2xl mx-auto p-10 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Contexto -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-xs font-mono font-bold mb-4">
    <span>📚</span> CONTENIDO DEL CURSO
  </div>

  <!-- Título Principal -->
  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight leading-tight">
    Temario de la Asignatura
  </h1>

</div>

---
transition: slide-up
level: 2
title: Temario de la asignatura
---

# Temario de la asignatura (1/2)

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

  <!-- Tema 1 -->
  <div class="p-4 bg-gray-100/80 dark:bg-gray-800/60 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm">
    <div class="font-bold text-amber-600 dark:text-amber-400 text-sm mb-2 flex items-center gap-2">
      <span class="bg-amber-100 dark:bg-amber-900/50 px-2 py-0.5 rounded-md text-xs font-mono font-bold">1</span>
      Análisis y diseño de algoritmos
    </div>
    <ul class="space-y-1 opacity-90 leading-snug">
      <li><b>1.1.</b> Definición de algoritmo y estructuras de datos.</li>
      <li><b>1.2.</b> Conceptos de complejidad algorítmica.</li>
      <li><b>1.3.</b> Análisis de la eficiencia de los algoritmos: tiempo y espacio.</li>
      <li><b>1.4.</b> Notación Big O y su importancia en la eficiencia de algoritmos.</li>
    </ul>
  </div>

  <!-- Tema 2 -->
  <div class="p-4 bg-gray-100/80 dark:bg-gray-800/60 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm">
    <div class="font-bold text-blue-600 dark:text-blue-400 text-sm mb-2 flex items-center gap-2">
      <span class="bg-blue-100 dark:bg-blue-900/50 px-2 py-0.5 rounded-md text-xs font-mono font-bold">2</span>
      Estructuras de datos y algoritmos de búsqueda
    </div>
    <ul class="space-y-1 opacity-90 leading-snug">
      <li><b>2.1.</b> Estructuras de datos.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>2.1.1.</b> Arreglo.</li>
          <li><b>2.1.2.</b> Listas.</li>
          <li><b>2.1.3.</b> Matrices multidimensionales.</li>
          <li><b>2.1.4.</b> Pilas.</li>
          <li><b>2.1.5.</b> Colas.</li>
          <li><b>2.1.6.</b> Punteros.</li>
        </ul>
      </li>
      <li class="mt-1"><b>2.2.</b> Algoritmos de búsqueda.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>2.2.1.</b> Búsqueda lineal.</li>
          <li><b>2.2.2.</b> Búsqueda binaria.</li>
        </ul>
      </li>
    </ul>
  </div>

</div>

---
transition: slide-up
level: 2
---
# Temario de la asignatura (2/2)

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

  <!-- Tema 3 -->
  <div class="p-4 bg-gray-100/80 dark:bg-gray-800/60 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm">
    <div class="font-bold text-emerald-600 dark:text-emerald-400 text-sm mb-2 flex items-center gap-2">
      <span class="bg-emerald-100 dark:bg-emerald-900/50 px-2 py-0.5 rounded-md text-xs font-mono font-bold">3</span>
      Algoritmos de ordenamiento y estructuras de datos avanzadas
    </div>
    <ul class="space-y-1 opacity-90 leading-snug">
      <li><b>3.1.</b> Algoritmos de Ordenamiento.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>3.1.1.</b> Inserción.</li>
          <li><b>3.1.2.</b> Selección.</li>
          <li><b>3.1.3.</b> QuickSort.</li>
        </ul>
      </li>
      <li class="mt-1"><b>3.2.</b> Árboles binarios de búsqueda (BST) y árboles AVL.</li>
      <li class="mt-1"><b>3.3.</b> Almacenamiento libre y colas de prioridad.</li>
    </ul>
  </div>

  <!-- Tema 4 -->
  <div class="p-4 bg-gray-100/80 dark:bg-gray-800/60 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm">
    <div class="font-bold text-purple-600 dark:text-purple-400 text-sm mb-2 flex items-center gap-2">
      <span class="bg-purple-100 dark:bg-purple-900/50 px-2 py-0.5 rounded-md text-xs font-mono font-bold">4</span>
      Técnicas avanzadas de diseño de algoritmos
    </div>
    <ul class="space-y-1 opacity-90 leading-snug">
      <li><b>4.1.</b> Conceptos de grafos y sus representaciones.</li>
      <li><b>4.2.</b> Algoritmos de búsqueda en grafos.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>4.2.1.</b> DFS.</li>
          <li><b>4.2.2.</b> BFS.</li>
        </ul>
      </li>
      <li class="mt-1"><b>4.3.</b> Algoritmos de búsqueda informada.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>4.3.1.</b> A(A-Star)*.</li>
          <li><b>4.3.2.</b> Greedy Best-First.</li>
        </ul>
      </li>
      <li class="mt-1"><b>4.4.</b> Técnicas avanzadas de diseño de algoritmos.
        <ul class="pl-3 space-y-0.5 opacity-80 mt-0.5">
          <li><b>4.4.1.</b> Programación dinámica.</li>
          <li><b>4.4.2.</b> Algoritmos voraces.</li>
        </ul>
      </li>
    </ul>
  </div>

</div>

---
layout: center
transition: fade-out
---

<div class="max-w-2xl mx-auto p-10 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Contexto -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 text-purple-600 dark:text-purple-400 text-xs font-mono font-bold mb-4">
    <span>📋</span> ACREDITACIÓN DEL CURSO
  </div>

  <!-- Título Principal -->
  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight leading-tight">
    Criterios de Evaluación
  </h1>

</div>

---
layout: default
transition: fade-out
zoom: 0.90
title: Criterios de Evaluación
---

# Criterios generales de evaluación
<p>Sujetos a modificación previo aviso o por adecuación de las actividades</p>


  <div class="grid grid-cols-2 gap-2">
    <div class="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 min-h-[150px]">
      <div class="flex justify-between items-center mb-2">
        <span class="font-bold text-base text-blue-400">Prácticas Individuales</span>
        <span class="px-2.5 py-1 bg-blue-500 text-white font-bold rounded-full text-xs">30%</span>
      </div>
      <p class="text-xs opacity-80 mb-2 italic"><strong>Finalidad:</strong> Validar la capacidad de análisis y desarrollo técnico individual.</p>
      <ul class="text-xs opacity-90 space-y-1 list-disc pl-4">
        <li>Desarrollo de ejercicios prácticos de programación.</li>
        <li>Resolución de retos presenciales de código y lógica.</li>
      </ul>
    </div>
    <div class="p-4 rounded-xl bg-purple-500/10 border border-purple-500/30 min-h-[150px]">
      <div class="flex justify-between items-center mb-2">
        <span class="font-bold text-base text-purple-400">Examen de Unidad</span>
        <span class="px-2.5 py-1 bg-purple-500 text-white font-bold rounded-full text-xs">30%</span>
      </div>
      <p class="text-xs opacity-80 mb-2 italic"><strong>Finalidad:</strong> Evaluar el razonamiento lógico, dominio conceptual y trazado.</p>
      <ul class="text-xs opacity-90 space-y-1 list-disc pl-4">
        <li>Evaluación individual presencial sobre los temas desarrollados.</li>
        <li>Pruebas de razonamiento teórico y práctico en papel.</li>
      </ul>
    </div>
  </div>

  <div class="grid grid-cols-3 gap-2 mt-4">
    <div class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 min-h-[135px]">
      <div class="flex justify-between items-center mb-2">
        <span class="font-bold text-sm text-emerald-400">Proyecto</span>
        <span class="px-2 py-0.5 bg-emerald-500 text-white font-bold rounded-full text-xs">20%</span>
      </div>
      <p class="text-xs opacity-80 mb-2 italic"><strong>Finalidad:</strong> Solución integradora modular.</p>
      <ul class="text-xs opacity-90 space-y-1 list-disc pl-4">
        <li>Avances del motor o sistema de software.</li>
      </ul>
    </div>
    <div class="p-4 rounded-xl bg-cyan-500/10 border border-cyan-500/30 min-h-[135px]">
      <div class="flex justify-between items-center mb-2">
        <span class="font-bold text-sm text-cyan-400">Portafolio</span>
        <span class="px-2 py-0.5 bg-cyan-500 text-white font-bold rounded-full text-xs">10%</span>
      </div>
      <p class="text-xs opacity-80 mb-2 italic"><strong>Finalidad:</strong> Respaldo para acreditación.</p>
      <ul class="text-xs opacity-90 space-y-1 list-disc pl-4">
        <li>Carpeta/repositorio técnico (sin apuntes).</li>
      </ul>
    </div>
    <div class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 min-h-[135px]">
      <div class="flex justify-between items-center mb-2">
        <span class="font-bold text-sm text-amber-400">Apuntes / Part.</span>
        <span class="px-2 py-0.5 bg-amber-500 text-white font-bold rounded-full text-xs">10%</span>
      </div>
      <p class="text-xs opacity-80 mb-2 italic"><strong>Finalidad:</strong> Atención y trabajo diario.</p>
      <ul class="text-xs opacity-90 space-y-1 list-disc pl-4">
        <li>Registro diario en libreta y retos de cierre.</li>
      </ul>
    </div>
  </div>

---
layout: center
transition: fade-out
tittle: Políticas del Curso
---

<div class="max-w-2xl mx-auto p-10 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Contexto -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-500/10 text-rose-600 dark:text-rose-400 text-xs font-mono font-bold mb-4">
    <span>📜</span> LINEAMIENTOS Y REGLAS
  </div>

  <!-- Título Principal -->
  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight leading-tight">
    Políticas del Curso
  </h1>

</div>

---
transition: slide-left
---

# Asistencia y Entregas

Lineamientos clave sobre puntualidad, evaluación y envío de evidencias:

<div class="grid grid-cols-2 gap-4 my-4">

  <!-- Tarjeta 1: Asistencia y Puntualidad -->
  <div v-click="1" class="border-2 border-emerald-500/30 bg-emerald-500/10 p-5 rounded-xl shadow-sm">
    <div class="flex items-center justify-between mb-3">
      <span class="px-3 py-1 bg-emerald-500 text-white text-xs font-bold rounded-full uppercase tracking-wider">Puntualidad</span>
      <span class="text-2xl font-black text-emerald-600 dark:text-emerald-400">80%</span>
    </div>
    <h3 class="text-lg font-bold text-emerald-600 dark:text-emerald-400 mb-2">Asistencia y Margen</h3>
    <ul class="text-xs space-y-2 opacity-90 list-disc pl-4">
      <li><b>Derecho a examen:</b> Mínimo <b>80%</b> de asistencia.</li>
      <li><b>Tolerancia:</b> Margen máximo de <b>10 minutos</b> para ingresar.</li>
    </ul>
  </div>

  <!-- Tarjeta 2: Entregas Extemporáneas -->
  <div v-click="2" class="border-2 border-amber-500/30 bg-amber-500/10 p-5 rounded-xl shadow-sm">
    <div class="flex items-center justify-between mb-3">
      <span class="px-3 py-1 bg-amber-500 text-white text-xs font-bold rounded-full uppercase tracking-wider">Entregas</span>
      <span class="text-2xl font-black text-amber-600 dark:text-amber-400">80 / 100</span>
    </div>
    <h3 class="text-lg font-bold text-amber-600 dark:text-amber-400 mb-2">Puntualidad de Tareas</h3>
    <ul class="text-xs space-y-2 opacity-90 list-disc pl-4">
      <li><b>Entregas tardías:</b> Solo con autorización previa y sobre <b>80 pts</b>.</li>
      <li><b>Segunda oportunidad:</b> Valoradas sobre un máximo de <b>80 pts</b>.</li>
    </ul>
  </div>

</div>

<!-- Banner Formatos -->
<div v-click="3" class="w-full bg-slate-800 text-white p-4 rounded-xl shadow-md text-xs flex justify-around items-center mt-2">
  <div><b class="text-blue-400">Trabajos Teóricos:</b> Exclusivamente en formato PDF </div>
  <div class="h-4 w-px bg-slate-600"></div>
  <div><b class="text-emerald-400">Prácticas Código:</b> Entrega mediante GitHub Classroom</div>
</div>


---
transition: slide-left
---

# Herramientas Tecnológicas e IA Generativa

Reglas claras para el uso de herramientas digitales y dispositivos en el aula:

<div class="grid grid-cols-2 gap-4 my-4">

  <!-- Tarjeta 1: Inteligencia Artificial -->
  <div v-click="1" class="border-2 border-rose-500/30 bg-rose-500/10 p-5 rounded-xl shadow-sm">
    <span class="px-3 py-1 bg-rose-500 text-white text-xs font-bold rounded-full uppercase tracking-wider mb-2 inline-block">Uso de IA</span>
    <h3 class="text-lg font-bold text-rose-600 dark:text-rose-400 mb-2">ChatGPT, Gemini & Copilot</h3>
    <ul class="text-xs space-y-2 opacity-90 list-disc pl-4">
      <li><b>Prohibido:</b> En desarrollo de prácticas y generación de código.</li>
      <li><b>Permitido:</b> Solo en actividades teóricas explícitamente indicadas.</li>
    </ul>
  </div>

  <!-- Tarjeta 2: Dispositivos en Clase -->
  <div v-click="2" class="border-2 border-indigo-500/30 bg-indigo-500/10 p-5 rounded-xl shadow-sm">
    <span class="px-3 py-1 bg-indigo-500 text-white text-xs font-bold rounded-full uppercase tracking-wider mb-2 inline-block">Dispositivos</span>
    <h3 class="text-lg font-bold text-indigo-600 dark:text-indigo-400 mb-2">Laptops y Teléfonos</h3>
    <ul class="text-xs space-y-2 opacity-90 list-disc pl-4">
      <li>Uso exclusivo para <b>fines académicos</b> durante la clase.</li>
      <li>Deben mantenerse en <b>modo silencioso</b> en todo momento.</li>
    </ul>
  </div>

</div>

<!-- Protocolo de Examen -->
<div v-click="3" class="border-2 border-slate-500/30 bg-slate-500/10 p-4 rounded-xl shadow-sm">
  <h4 class="font-bold text-sm mb-1 text-slate-700 dark:text-slate-200">🔒 Protocolo durante Exámenes</h4>
  <p class="text-xs opacity-90 leading-relaxed">
    Teléfonos celulares entregados en el <b>escritorio del profesor</b> y mochilas colocadas en el <b>frente del aula</b> antes de iniciar la prueba.
  </p>
</div>

---
transition: slide-left
---

# Convivencia y Comunicación

Lineamientos para el trabajo en equipo, la disciplina y el contacto fuera de clase:

<div class="grid grid-cols-2 gap-4 my-4">

  <!-- Tarjeta 1: Disciplina en el Aula -->
  <div v-click="1" class="border-2 border-cyan-500/30 bg-cyan-500/10 p-5 rounded-xl shadow-sm">
    <span class="px-3 py-1 bg-cyan-500 text-white text-xs font-bold rounded-full uppercase tracking-wider mb-2 inline-block">Aula</span>
    <h3 class="text-lg font-bold text-cyan-600 dark:text-cyan-400 mb-2">Respeto e Interrupciones</h3>
    <p class="text-xs opacity-90 leading-relaxed">
      Guardar silencio y atención durante explicaciones. Ante interrupciones continuas, se solicitará al alumno <b>retirarse de la sesión</b>.
    </p>
  </div>

  <!-- Tarjeta 2: Coevaluación -->
  <div v-click="2" class="border-2 border-purple-500/30 bg-purple-500/10 p-5 rounded-xl shadow-sm">
    <span class="px-3 py-1 bg-purple-500 text-white text-xs font-bold rounded-full uppercase tracking-wider mb-2 inline-block">Equipos</span>
    <h3 class="text-lg font-bold text-purple-600 dark:text-purple-400 mb-2">Trabajo Colaborativo</h3>
    <p class="text-xs opacity-90 leading-relaxed">
      Se aplicará un esquema de <b>coevaluación</b> para penalizar la falta de aportación o compromiso de integrantes en tareas grupales.
    </p>
  </div>

</div>

<!-- Canales de Comunicación -->
<div v-click="3" class="grid grid-cols-2 gap-4 border-2 border-blue-500/30 bg-blue-500/10 p-4 rounded-xl shadow-sm text-xs">
  <div>
    <b class="text-blue-600 dark:text-blue-400">✉️ Correo Institucional:</b>
    <p class="opacity-80 mt-0.5">Canal oficial para trámites, justificaciones y asuntos formales.</p>
  </div>
  <div>
    <b class="text-emerald-600 dark:text-emerald-400">💬 WhatsApp (8:00 - 19:00 hrs):</b>
    <p class="opacity-80 mt-0.5">Avisos rápidos y dudas generales en horario hábil.</p>
  </div>
</div>



---
layout: center
transition: fade-out
title: Tema 1. Análisis y Diseño de Algoritmos
---

<div class="max-w-xl mx-auto p-8 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Tema -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 text-xs font-mono font-bold mb-4">
    <span>⚡</span> TEMA 01
  </div>

  <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight mb-3">
    Análisis y Diseño de Algoritmos
  </h1>

  <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">
    Evaluación de la eficiencia y complejidad en el diseño de soluciones
  </p>

  <!-- Etiquetas con los subtemas -->
  <div class="flex flex-wrap justify-center gap-2 text-xs font-mono">
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">1.1 Definición</span>
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">1.2 Complejidad</span>
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">1.3 Eficiencia</span>
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">1.4 Big O</span>
  </div>

</div>

---
layout: center
transition: fade-out
title: El pilar de la Ingeniería
---

<div class="max-w-2xl mx-auto p-8 rounded-2xl bg-gray-50/80 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700/80 shadow-xl text-center backdrop-blur-sm">
  
  <!-- Encabezado de Tema -->
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 text-blue-600 dark:text-blue-400 text-xs font-mono font-bold mb-4">
    <span></span> CONTEXTUALIZACIÓN PEDAGÓGICA
  </div>

  <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white tracking-tight mb-3">
    El Pilar de la Ingeniería y la IA
  </h2>

  <p class="text-xs text-gray-600 dark:text-gray-300 mb-5 leading-relaxed">
    La estructuración y el procesamiento eficiente de la información son los fundamentos indispensables para el diseño de soluciones viables en la computación moderna.
  </p>

  <!-- Tarjeta Destacada del Subtema -->
  <div class="p-4 rounded-xl bg-white/80 dark:bg-gray-700/50 border border-gray-200 dark:border-gray-600 text-left mb-5 shadow-xs">
    <span class="text-xs font-mono font-bold text-blue-600 dark:text-blue-400 block mb-1">
      Subtema 1.1: Definición de Algoritmo y Estructuras de Datos
    </span>
    <p class="text-xs text-gray-600 dark:text-gray-300 leading-normal">
      Sienta las bases conceptuales para comprender cómo las computadoras procesan, organizan y manipulan la información.
    </p>
  </div>

  <!-- Habilidades Clave -->
  <h3 class="text-xs font-mono text-gray-400 dark:text-gray-400 mb-2">
    Habilidades clave:
  </h3>

  <div class="flex flex-wrap justify-center gap-2 text-xs font-mono">
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">🧠 Abstracción</span>
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">📊 Pensamiento Analítico</span>
    <span class="px-2.5 py-1 bg-white dark:bg-gray-700/80 rounded-md border border-gray-200 dark:border-gray-600 shadow-xs">⚡ Razonamiento Lógico</span>
  </div>

</div>
---
transition: slide-left
zoom: 0.88
---

# 1.1 ¿Qué es un Algoritmo? (1/4)

<span class="text-xs text-blue-500 font-mono uppercase tracking-wider font-bold block mb-1">Algoritmos frente a Estructuras de Datos</span>

<!-- Definición General -->
<div v-click="1" class="mb-4 p-2 rounded-lg bg-blue-500/10 border-l-4 border-blue-500 text-xs leading-tight">
  <b class="text-blue-600 dark:text-blue-400">Procedimiento computacional bien definido:</b> Secuencia de pasos lógicos que toma un conjunto de valores como <b>Entrada (Input)</b> y los transforma en un conjunto de resultados como <b>Salida (Output)</b> en un tiempo finito.
</div>

<!-- 4 Características Fundamentales -->
<div v-click="2" class="grid grid-cols-2 gap-2 my-2">
  
  <div class="bg-blue-500/10">
    <div class="font-bold"> Precisión</div>
    <p>Indica rigurosamente el orden secuencial de realización de cada paso, sin ambigüedades.</p>
  </div>

  <div class="bg-emerald-500/10">
    <div class="font-bold"> Definición</div>
    <p>Al ejecutarse con los mismos datos de entrada, siempre debe generar exactamente el mismo resultado.</p>
  </div>

  <div class="bg-amber-500/10">
    <div class="font-bold"> Finitud</div>
    <p>Debe finalizar en algún momento; consta de un número determinado y finito de pasos.</p>
  </div>

  <div class="bg-purple-500/10">
    <div class="font-bold"> Partes Claras</div>
    <p>Estructura explícita dividida en: <b>Entrada</b> ➔ <b>Proceso</b> ➔ <b>Salida</b>.</p>
  </div>

</div>

<!-- Símil Cotidiano -->
<div v-click="3" class="mt-3 p-2 rounded-lg bg-slate-800 shadow-md flex items-center justify-between">
  <div class="leading-tight">
    <span class="text-amber-400 font-bold text-xs block mb-0.5">Símil Cotidiano: Receta de Cocina</span>
    <span class="text-xs block">
      Ingredientes (Entrada) ➔ Preparación (Proceso) ➔ Plato Final (Salida)
    </span>
  </div>
  <span class="text-xs font-mono bg-slate-700 text-slate-200 px-2 py-1 rounded border border-slate-600 whitespace-nowrap hidden sm:block">
    Entrada ➔ Proceso ➔ Salida
  </span>
</div>

---
transition: slide-left
---

# 1.1 ¿Qué es una Estructura de Datos? (2/4)

<span class="text-xs text-indigo-500 font-mono uppercase tracking-wider font-bold">Organización y Almacenamiento Eficiente</span>

<!-- Definición Principal -->
<div v-click="1" class="mb-3 bg-indigo-500/10">
  <p class="m-0 leading-relaxed">
    <b>Medio sistemático de organización:</b> Permite almacenar y estructurar datos en la memoria de la computadora para facilitar su acceso, manipulación y modificación eficiente.
  </p>
</div>

<!-- 3 Grupos de Operaciones -->
<div v-click="2" class="mt-5">
  <span class="text-[11px] font-mono font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider block mb-1.5">Operaciones Principales</span>
  <div class="grid grid-cols-3 gap-2">
    <div class="p-2.5 rounded-lg border border-gray-200 dark:border-gray-700/80 bg-gray-50/50 dark:bg-gray-800/40 text-center shadow-xs">
      <div class="text-xs font-bold text-emerald-600 dark:text-emerald-400">⚡ Creación / Eliminación</div>
      <p class="text-[10px] opacity-80 mt-1">Reserva y liberación de espacio en memoria.</p>
    </div>
    <div class="p-2.5 rounded-lg border border-gray-200 dark:border-gray-700/80 bg-gray-50/50 dark:bg-gray-800/40 text-center shadow-xs">
      <div class="text-xs font-bold text-amber-600 dark:text-amber-400">🔄 Actualización</div>
      <p class="text-[10px] opacity-80 mt-1">Inserción y borrado de valores existentes.</p>
    </div>
    <div class="p-2.5 rounded-lg border border-gray-200 dark:border-gray-700/80 bg-gray-50/50 dark:bg-gray-800/40 text-center shadow-xs">
      <div class="text-xs font-bold text-blue-600 dark:text-blue-400">🔍 Consulta</div>
      <p class="text-[10px] opacity-80 mt-1">Búsqueda y acceso sin modificar la estructura.</p>
    </div>
  </div>
</div>

<!-- Clasificación Estáticas vs Dinámicas -->
<div v-click="3" class="grid grid-cols-2 gap-3 mt-5">
  
  <!-- Estáticas -->
  <div class="border border-cyan-500/30 bg-cyan-500/10 p-3 rounded-xl shadow-xs">
    <div class="flex justify-between items-center mb-1">
      <span class="font-bold text-xs text-cyan-600 dark:text-cyan-400">📌 Estructuras Estáticas</span>
      <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-700 dark:text-cyan-300 font-bold">Tamaño Fijo</span>
    </div>
    <p class="text-[11px] opacity-80 leading-tight mb-1.5">
      Espacio reservado antes de la ejecución. No se redimensionan en tiempo de ejecución.
    </p>
    <div class="text-[10px] text-cyan-700 dark:text-cyan-300 font-mono">
      <b>Ejemplos:</b> Arreglos (arrays), vectores, matrices.
    </div>
  </div>

  <!-- Dinámicas -->
  <div class="border border-purple-500/30 bg-purple-500/10 p-3 rounded-xl shadow-xs">
    <div class="flex justify-between items-center mb-1">
      <span class="font-bold text-xs text-purple-600 dark:text-purple-400">🚀 Estructuras Dinámicas</span>
      <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-purple-500/20 text-purple-700 dark:text-purple-300 font-bold">Punteros</span>
    </div>
    <p class="text-[11px] opacity-80 leading-tight mb-1.5">
      Crecen y se contraen en tiempo de ejecución según se requiera.
    </p>
    <div class="text-[10px] text-purple-700 dark:text-purple-300 font-mono">
      <b>Ejemplos:</b> Listas, pilas, colas, árboles, grafos.
    </div>
  </div>

</div>

---
transition: slide-left
---

# 1.1 La Relación Simbiótica (3/4)

<span class="text-xs text-indigo-500 font-mono uppercase tracking-wider font-bold">Algoritmos frente a Estructuras de Datos</span>

<!-- Concepto de Simbiosis -->
<div v-click="1" class="my-2 p-2.5 rounded-xl bg-indigo-500/10 border-l-4 border-indigo-500 text-xs leading-relaxed">
  <b class="text-indigo-600 dark:text-indigo-400">Dos caras de una misma moneda:</b> Un algoritmo veloz requiere una estructura de datos adecuada que le dé soporte, y una estructura compleja solo cobra sentido mediante algoritmos que la exploten.
</div>

<!-- Ecuación de Niklaus Wirth -->
<div v-click="2" class="my-3 p-4 rounded-xl bg-slate-900 shadow-md text-center">
  <div class="inline-block px-3 py-1 rounded-full bg-indigo-500/30 text-indigo-300 font-mono font-bold mb-3 uppercase tracking-wider text-xs">
    Niklaus Wirth — Creador de Pascal
  </div>
  
  <div class="flex items-center justify-center gap-3 my-1">
    <div class="px-4 py-2 rounded-lg bg-blue-600 text-white font-bold">
      Algoritmos
    </div>
    <span class="text-amber-400 font-bold text-xl">+</span>
    <div class="px-4 py-2 rounded-lg bg-purple-600 text-white font-bold">
      Estructuras de Datos
    </div>
    <span class="text-amber-400 font-bold text-xl">=</span>
    <div class="px-5 py-2 rounded-lg bg-emerald-600 text-white font-extrabold shadow-sm">
      Programas
    </div>
  </div>
</div>

<!-- Impacto y Selección -->
<div v-click="3" class="grid grid-cols-2 gap-2 mt-2">
  <div class="border border-gray-200 dark:border-gray-700/80 bg-gray-50/50 dark:bg-gray-800/40 p-2.5 rounded-xl shadow-xs">
    <div class="font-bold text-xs text-amber-600 dark:text-amber-400 mb-0.5">⚡ Impacto en Rendimiento</div>
    <p class="text-[11px] opacity-80 leading-tight">
      La organización en memoria determina qué operaciones son sencillas y cuáles resultan extremadamente lentas.
    </p>
  </div>

  <div class="border border-gray-200 dark:border-gray-700/80 bg-gray-50/50 dark:bg-gray-800/40 p-2.5 rounded-xl shadow-xs">
    <div class="font-bold text-xs text-emerald-600 dark:text-emerald-400 mb-0.5">🎯 Núcleo del Software</div>
    <p class="text-[11px] opacity-80 leading-tight">
      La correcta elección de esta dupla es el pilar esencial de la ingeniería de software y el diseño algorítmico.
    </p>
  </div>
</div>

---
transition: slide-left
zoom: 0.95
---

# Tabla Comparativa de Diferencias Clave (4/4)

<span class="text-xs text-blue-500 font-mono uppercase tracking-wider font-bold">1.1 Algoritmos frente a Estructuras de Datos</span>

<!-- Tabla Comparativa -->
<div v-click="1" class="mt-3 overflow-hidden rounded-xl border border-gray-200 dark:border-gray-700/80 shadow-xs">
  <table class="w-full text-[10.5px] text-left border-collapse">
    <thead>
      <tr class="bg-gray-100 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
        <th class="py-2 px-3 font-bold text-gray-700 dark:text-gray-200 w-1/4">Criterio</th>
        <th class="py-2 px-3 font-bold text-blue-600 dark:text-blue-400 w-3/8"> Algoritmo</th>
        <th class="py-2 px-3 font-bold text-purple-600 dark:text-purple-400 w-3/8"> Estructura de Datos</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 dark:divide-gray-800 bg-white/50 dark:bg-gray-900/40">
      <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/30">
        <td class="py-1.5 px-3 font-bold text-gray-800 dark:text-gray-200">Naturaleza</td>
        <td class="py-1.5 px-3 opacity-90"><b class="text-blue-600 dark:text-blue-400">Dinámica y de Comportamiento:</b> Proceso, lógica e instrucciones de cálculo.</td>
        <td class="py-1.5 px-3 opacity-90"><b class="text-purple-600 dark:text-purple-400">Estructural y Organizativa:</b> Disposición, almacenamiento y acceso en memoria.</td>
      </tr>
      <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/30">
        <td class="py-1.5 px-3 font-bold text-gray-800 dark:text-gray-200">Pregunta que Resuelve</td>
        <td class="py-1.5 px-3 opacity-90"><b class="text-blue-600 dark:text-blue-400">¿Cómo se hace?</b> Pasos sistemáticos para resolver un problema.</td>
        <td class="py-1.5 px-3 opacity-90"><b class="text-purple-600 dark:text-purple-400">¿Dónde y cómo se guarda?</b> Modelo lógico y físico de la información.</td>
      </tr>
      <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/30">
        <td class="py-1.5 px-3 font-bold text-gray-800 dark:text-gray-200">Componentes</td>
        <td class="py-1.5 px-3 opacity-90"><b>Entradas, Procesos y Salidas</b> definidos por estructuras de control.</td>
        <td class="py-1.5 px-3 opacity-90"><b>Campos, registros, nodos, punteros o celdas</b> organizados lógicamente.</td>
      </tr>
      <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/30">
        <td class="py-1.5 px-3 font-bold text-gray-800 dark:text-gray-200">Operaciones Comunes</td>
        <td class="py-1.5 px-3 opacity-90">Operaciones aritméticas, comparaciones y control de flujo.</td>
        <td class="py-1.5 px-3 opacity-90">Inserción, borrado de datos y consultas/búsquedas.</td>
      </tr>
      <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/30">
        <td class="py-1.5 px-3 font-bold text-gray-800 dark:text-gray-200">Dependencia Mutua</td>
        <td class="py-1.5 px-3 opacity-90">Requiere una estructura compatible para operar eficientemente.</td>
        <td class="py-1.5 px-3 opacity-90">Requiere algoritmos específicos para manipular sus elementos.</td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: default
---

# Caso Práctico: Adivinanza de Números
Aplicando la dependencia mutua entre Algoritmos y Estructuras de Datos en un escenario real.

<div class="grid grid-cols-2 gap-4">
  <div class="bg-indigo-50 rounded-xl p-5">
    
  ### 1. La Estructura de Datos
   
   
  * **Naturaleza:** Estructural y Organizativa.
  * **Modelo:** Colección secuencial en memoria contigua.
    

  $$\text{Arreglo } A: [1, 2, 3, \dots, 99, 100]$$
  $$\text{Índices: } [0, 1, 2, \dots, 98, 99]$$

  </div>
 
  <div class="bg-emerald-50 rounded-xl p-5">

  ### 2. El Algoritmo
  
  * **Naturaleza:** Dinámica y de Comportamiento.
  * **Misión:** Hallar $X \in [1, 100]$ en mínimos intentos.
  * **Mecanismo:** Evaluación de 3 estados tras propuesta $k$:

  ```text
    SI k < X  ➔ "Mi número es más alto"
    SI k > X  ➔ "Mi número es más bajo"
    SI k == X ➔ "¡Correcto!"
  ```
  
  </div>
</div>

---
layout: default
zoom: 0.90
---

# ¿Cómo resolvemos el reto?
Comparación de estrategias para encontrar el número objetivo dentro del arreglo $A[0 \dots 99]$:
<div class="grid grid-cols-2 gap-6 mt-6">
<div class="p-5 rounded-xl bg-slate-800/80 border border-slate-700 shadow-lg">
<span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Estrategia 1</span>

### Enfoque A: Búsqueda Lineal
* **Mapeo:** Evaluar elemento por elemento ($1, 2, 3, 4, \dots$).
* **Aprovechamiento:** Ignora que la estructura está ordenada.
* **¿Es eficiente?:** Ineficiente a medida que $n$ crece.
* **Costo Computacional:**
  * Caso promedio: $50$ intentos.
  * **Peor caso:** **$100$ intentos** ($O(n)$).

</div>
<div class="p-5 rounded-xl bg-slate-800/80 border border-indigo-500/50 shadow-lg">
<span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Estrategia 2</span>

### Enfoque B: Búsqueda Binaria
* **Mapeo:** Dividir el espacio a la mitad en cada paso ($50, 75, \dots$).
* **Aprovechamiento:** Utiliza el orden indexado de la estructura.
* **¿Es eficiente?:** Altamente eficiente.
* **Costo Computacional:**
  * Caso promedio: $\approx 6$ intentos.
  * **Peor caso:** **$\lceil \log_2(100) \rceil = 7$ intentos** ($O(\log n)$).

</div>
</div>

<v-click>
<div class="mt-6 p-4 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-center text-sm text-indigo-200">
💡 **Conclusión clave:** El *Algoritmo B* solo es posible porque la *Estructura de Datos* (el arreglo) mantiene los elementos **ordenados e indexados** en memoria.
</div>
</v-click>

---
layout: section
---

# Enfoque A
## Búsqueda Lineal o Simple

<div class="text-2xl mt-8">

### El camino intuitivo… pero ineficiente

</div>

<div class="mt-10 text-xl">

La estrategia más directa consiste en preguntar:

</div>

<div class="mt-8 flex justify-center items-center gap-4 text-2xl">

<span class="px-5 py-3 rounded-lg bg-gray-100">1</span>
<span>→</span>
<span class="px-5 py-3 rounded-lg bg-gray-100">2</span>
<span>→</span>
<span class="px-5 py-3 rounded-lg bg-gray-100">3</span>
<span>→</span>
<span class="px-5 py-3 rounded-lg bg-gray-100">4</span>
<span>→</span>
<span class="px-5 py-3 rounded-lg bg-yellow-100">5</span>
<span>→</span>
<span class="px-5 py-3 rounded-lg bg-gray-100">…</span>

</div>

<div class="mt-10 text-center text-xl">

**Hasta encontrar el número correcto.**

</div>

---
layout: default
---

# ¿Cómo funciona la búsqueda lineal?

<div class="text-xl mt-3">

La búsqueda lineal realiza un **recorrido secuencial** del arreglo.

</div>

<div class="grid grid-cols-2 gap-8 mt-5">

<div>

### Recorrido secuencial

Se revisan los elementos:

- uno por uno;
- en orden;
- comenzando en el índice `0`;
- avanzando hasta `n - 1`.

En cada posición se compara:

$$
A[i] \stackrel{?}{=} secreto
$$

</div>

<div>

### Ejemplo

```text
Índice:  0    1    2    3    4    ...   99
Valor:  | 1 | 2 | 3 | 4 | 5 | ... | 100 |
          ↑
        inicio
```
<div class="mt-3">
El índice aumenta de uno en uno:
</div>

```text
i = 0 → 1 → 2 → 3 → ... → n-1
```

</div>

</div>

<div class="mt-0 p-4 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-lg">

💡 **Idea fundamental:** no intenta "adivinar" dónde está el elemento. Simplemente revisa cada posición en orden.

</div>

---
layout: default
---

# Algoritmo lógico

<div class="grid grid-cols-2 gap-10 mt-8">

<div>

### Pseudocódigo

```text
i ← 0

mientras (A[i] ≠ secreto) y (i < n) hacer
    i ← i + 1
fin_mientras
```

</div>

<div>

### ¿Qué está haciendo?

**1.** Comienza en:

```text
i ← 0
```

**2.** Compara:

```text
A[i] ≠ secreto
```

**3.** Si no coincide:

```text
i ← i + 1
```

**4.** Repite hasta encontrarlo o llegar al final.

</div>

</div>

<div class="mt-0.5 p-5 rounded-xl bg-yellow-50 dark:bg-yellow-900/30">

⚠️ **Importante:** el algoritmo debe contemplar también el caso en que el elemento buscado **no se encuentre** en el arreglo.

</div>

---
layout: default
---

# Ejemplo: número secreto = **31**

<div class="text-xl mt-5">

Supongamos que el arreglo contiene los números del **1 al 100** y el docente ha pensado en el número **31**.

</div>

<div class="mt-8">

```text
Índice:  0    1    2    3    4    ...   29   30   ...   99
Valor:  | 1 | 2 | 3 | 4 | 5 | ... | 30 | 31 | ... | 100 |
```

</div>

<div class="mt-8 grid grid-cols-3 gap-5 text-center">

<div class="p-5 rounded-xl bg-red-50 dark:bg-red-900/30">

### Paso 1

`A[0] = 1`

`1 ≠ 31`

**Más alto**

</div>

<div class="p-5 rounded-xl bg-red-50 dark:bg-red-900/30">

### Paso 2

`A[1] = 2`

`2 ≠ 31`

**Más alto**

</div>

<div class="p-5 rounded-xl bg-red-50 dark:bg-red-900/30">

### Paso 3

`A[2] = 3`

`3 ≠ 31`

**Más alto**

</div>

</div>

<div class="mt-8 text-center text-xl">

El patrón continúa incrementando `i` de uno en uno.

</div>

--
layout: default
---

# El recorrido continúa…

<div class="mt-2">

```text
Paso 1
A[0] = 1   →   1 ≠ 31   →   i ← 1

Paso 2
A[1] = 2   →   2 ≠ 31   →   i ← 2

Paso 3
A[2] = 3   →   3 ≠ 31   →   i ← 3

              ⋮

Paso 30
A[29] = 30 → 30 ≠ 31   →   i ← 30
```

</div>

<div class="mt-6 p-5 rounded-xl bg-orange-50 dark:bg-orange-900/30 text-xl text-center">

**31 todavía no ha sido encontrado.**

</div>

---
layout: default
---

# Finalmente… encontramos el 31

<div class="mt-8">

```text
Paso 31

A[30] = 31

31 = 31
  ↓
¡CORRECTO!
```

</div>

<div class="mt-10 grid grid-cols-3 gap-6 text-center">

<div class="p-6 rounded-xl bg-gray-50 dark:bg-gray-800">

### Inicio

`i = 0`

</div>

<div class="p-6 rounded-xl bg-yellow-50 dark:bg-yellow-900/30">

### Recorrido

`0 → 1 → 2 → ... → 30`

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### Resultado

**31 comparaciones**

</div>

</div>

<div class="mt-10 text-center text-xl">

El algoritmo tuvo que revisar **todos los valores anteriores** antes de encontrar el objetivo.

</div>

---
layout: default
---

# Visualización del recorrido

```text
Índice:   [0]    [1]    [2]    [3]    ...    [30]    ...    [99]
Valor:   | 1 |  | 2 |  | 3 |  | 4 |   ...   | 31 |   ...   | 100 |
           ↑      ↑      ↑                       ↑
         Paso 1  Paso 2  Paso 3                 Paso 31 ✓
```

<div class="mt-5 grid grid-cols-2 gap-6">

<div class="p-4 rounded-xl bg-red-50 dark:bg-red-900/30">

### ❌ Mientras no coincide

```text
A[i] ≠ secreto  →  i ← i + 1
```

El puntero avanza **una posición** y realiza una nueva comparación.

</div>

<div class="p-4 rounded-xl bg-green-50 dark:bg-green-900/30">

### ✅ Cuando coincide

```text
A[i] = secreto  →  detener
```

La búsqueda termina: **el elemento fue encontrado**.

</div>

</div>

<div class="mt-5 text-center text-xl">

**El recorrido siempre avanza de manera secuencial: una posición a la vez.**

</div>

---
layout: default
---

# ¿Cuántas comparaciones necesita?

<div class="grid grid-cols-3 gap-6 mt-8">

<div class="p-6 rounded-xl border-2">

### 🟢 Mejor caso

El elemento está en la **primera posición**.

```text
A[0] = secreto
```

**1 comparación**

$$
T(n) = 1
$$

</div>

<div class="p-6 rounded-xl border-2">

### 🟡 Caso promedio

Si todos los elementos tienen la misma probabilidad:

$$
\frac{n+1}{2}
$$

Para `n = 100`:

**50.5 comparaciones**

</div>

<div class="p-6 rounded-xl border-2">

### 🔴 Peor caso

El elemento está al final o **no existe**.

Para `n = 100`:

**100 comparaciones**

</div>

</div>

<div class="mt-10 text-center text-xl">

El **peor caso** nos indica la cantidad máxima de trabajo que puede realizar el algoritmo.

</div>

---
layout: default
---

# ¿Qué ocurre si el número no existe?

<div class="text-xl mt-6">

Supongamos que buscamos el número **150**, pero el arreglo contiene únicamente valores del `1` al `100`.

</div>

<div class="mt-8">

```text
1 → 2 → 3 → 4 → 5 → ... → 98 → 99 → 100
                                           ↑
                                      último elemento
```

</div>

<div class="mt-8 p-6 rounded-xl bg-red-50 dark:bg-red-900/30 text-xl">

❌ Ningún elemento coincide con `150`.

El algoritmo debe revisar **las 100 posiciones** antes de concluir que el elemento no está.

</div>

<div class="mt-8 text-center text-2xl">

**Peor caso = 100 comparaciones**

</div>

---
layout: default
zoom: 0.82
---

# Análisis de crecimiento

<div class="text-xl mt-5">

La cantidad de trabajo crece proporcionalmente al tamaño del arreglo.

</div>

<div class="mt-8">

| Tamaño `n` | Comparaciones máximas |
|---:|---:|
| 10 | 10 |
| 50 | 50 |
| 100 | 100 |
| 200 | 200 |
| 1,000 | 1,000 |

</div>

<div class="mt-8 text-center">

$$
T(n) \propto n
$$

</div>

<div class="mt-6 text-center text-3xl">

# $O(n)$

<div class="text-xl mt-3">

**Crecimiento lineal**

</div>

</div>

---
layout: default
---

# ¿Qué significa $O(n)$?

<div class="text-xl mt-6">

`O(n)` significa que el tiempo de ejecución crece **linealmente** con el tamaño de los datos.

</div>

<div class="mt-8 grid grid-cols-2 gap-8">

<div>

### Si tenemos 100 elementos

Peor caso:

```text
100 elementos
      ↓
100 comparaciones
```

</div>

<div>

### Si tenemos 200 elementos

Peor caso:

```text
200 elementos
      ↓
200 comparaciones
```

</div>

</div>

<div class="mt-10 p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-xl text-center">

📈 **Si duplicamos `n`, el trabajo máximo también se duplica.**

</div>

---
layout: default
---

# Búsqueda Lineal: resumen

<div class="grid grid-cols-2 gap-6 mt-5 text-lg">

<div class="p-4 rounded-xl">

### ¿Cómo busca?

Revisa los elementos **uno por uno**.

</div>

<div class="p-4 rounded-xl">

### ¿Dónde comienza?

En el índice:

`i = 0`

</div>

<div class="p-4 rounded-xl">

### ¿Cuándo termina?

Cuando encuentra el elemento o llega al final.

</div>

<div class="p-4 rounded-xl">

### ¿Cuál es su complejidad?

$$
O(n)
$$

</div>

</div>

<div class="mt-6 p-5 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-center text-xl">

### 💭 Pregunta para el siguiente enfoque

**¿Podemos aprovechar que los números están ordenados para evitar revisar uno por uno?**

</div>

<div class="mt-4 text-center text-xl">

👉 **Sí: Búsqueda Binaria**

</div>

---
layout: section
---
# Enfoque B
## Búsqueda Binaria o Dicotómica
<div class="text-2xl mt-8">

### El camino eficiente del **“Divide y Vencerás”**

</div>

<div class="mt-10 text-xl">

En lugar de revisar los elementos uno por uno, proponemos el valor que se encuentra en la **mitad del rango activo**.

</div>

<div class="mt-8 flex justify-center items-center gap-4 text-2xl">

<span class="px-6 py-3 rounded-lg bg-gray-100">1</span><span>…</span><span class="px-6 py-3 rounded-lg bg-green-100 font-bold">50</span><span>…</span><span class="px-6 py-3 rounded-lg bg-gray-100">100</span>

</div>

<div class="mt-10 text-center text-xl">

Cada respuesta permite **descartar aproximadamente la mitad de las opciones restantes**.

</div>

---
layout: default
---
# Antes de comenzar: una condición indispensable
<div class="text-xl mt-6">

La búsqueda binaria solamente funciona correctamente cuando los elementos están **ordenados**.

</div>

<div class="grid grid-cols-2 gap-10 mt-10">

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### ✅ Arreglo ordenado
```text
[1, 2, 3, 4, 5, 6, 7, ...]
```
Podemos determinar si el valor buscado está a la **izquierda** o a la **derecha** del centro.

</div>

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### ❌ Arreglo desordenado
```text
[7, 2, 9, 1, 5, 3, 8, ...]
```
Comparar con el centro no permite saber qué mitad podemos descartar.

</div>

</div>

<div class="mt-10 p-5 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-xl text-center">

💡 **Requisito fundamental:** los datos deben estar **ordenados**.

</div>

---
layout: default
---
# ¿Cómo funciona?
<div class="text-xl mt-5">

En cada iteración se calcula el elemento central del **intervalo activo**.

</div>

<div class="mt-8 text-center">

$$
centro = \left\lfloor \frac{bajo + alto}{2} \right\rfloor
$$

</div>

<div class="grid grid-cols-3 gap-6 mt-10 text-center">

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### Secreto < centro
Descartamos la mitad **derecha**.
`alto ← centro - 1`

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### Secreto = centro
🎯 **¡Encontrado!**
La búsqueda termina.

</div>

<div class="p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30">

### Secreto > centro
Descartamos la mitad **izquierda**.
`bajo ← centro + 1`

</div>

</div>

<div class="mt-8 text-center text-xl">

El proceso se repite calculando un **nuevo centro** sobre la mitad que permanece activa.

</div>

---
layout: default
---
# Algoritmo lógico
<div class="grid grid-cols-2 gap-10 mt-7">

<div>

### Pseudocódigo
```text
bajo ← 0
alto ← n - 1
mientras (bajo ≤ alto) hacer
    centro ← parte_entera((bajo + alto) / 2)
    si (A[centro] == secreto) entonces
        retornar centro
    sino si (A[centro] > secreto) entonces
        alto ← centro - 1
    sino
        bajo ← centro + 1
    fin_si
fin_mientras
```

</div>

<div>

### Los tres punteros
**`bajo`** marca el inicio del rango activo.

**`alto`** marca el final del rango activo.

**`centro`** indica la posición que se compara con el valor buscado.
<div class="mt-7 p-5 rounded-xl bg-blue-50 dark:bg-blue-900/30">

Después de cada comparación, el intervalo activo se hace **mucho más pequeño**.

</div>

</div>

</div>

---
layout: default
---
# Iteración 1: comenzamos con **50**
<div class="text-lg mt-4">Número secreto: **31**</div>

<div class="mt-5">

```text
Índice:  [0]                    [49]                    [99]
Valor:    1  2  3 ...           50          ...         100
          ↑                      ↑                        ↑
        bajo                   centro                    alto
```

</div>

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### Cálculo
`bajo = 0`  
`alto = 99`
$$
centro=\left\lfloor\frac{0+99}{2}\right\rfloor=49
$$
`A[49] = 50`

</div>

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### Comparación
$$
31 < 50
$$
**“Mi número es más bajo.”**

Descartamos la mitad superior.
```text
alto ← 49 - 1
alto ← 48
```

</div>

</div>

<div class="mt-5 text-center text-xl">❌ Se descartan de inmediato los valores **50 a 100**.</div>

---
layout: default
---
# Iteración 2: probamos con **25**
<div class="mt-5">

```text
Índice:  [0]          [24]          [48] | DESCARTADO
Valor:    1 ...        25    ...     49  | 50 ... 100
          ↑             ↑             ↑
        bajo          centro         alto
```

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Nuevo rango activo
Valores: **1 a 49**

`bajo = 0`  
`alto = 48`
$$
centro=\left\lfloor\frac{0+48}{2}\right\rfloor=24
$$
`A[24] = 25`

</div>

<div class="p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30">

### Comparación
$$
31 > 25
$$
**“Mi número es más alto.”**
```text
bajo ← 24 + 1
bajo ← 25
```

</div>

</div>

<div class="mt-6 text-center text-xl">❌ Se descartan los valores **1 a 25**.</div>

---
layout: default
---
# Iteración 3: probamos con **37**
<div class="mt-5">

```text
DESCARTADO | [25]       [36]       [48] | DESCARTADO
  1 ... 25 |  26 ...     37  ...    49  | 50 ... 100
              ↑           ↑          ↑
            bajo        centro      alto
```

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Nuevo rango activo
Valores: **26 a 49**

`bajo = 25`  
`alto = 48`
$$
centro=\left\lfloor\frac{25+48}{2}\right\rfloor=36
$$
`A[36] = 37`

</div>

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### Comparación
$$
31 < 37
$$
**“Mi número es más bajo.”**
```text
alto ← 36 - 1
alto ← 35
```

</div>

</div>

<div class="mt-6 text-center text-xl">❌ Se descartan los valores **37 a 49**.</div>

---
layout: default
---
# Iteración 4: encontramos el **31**
<div class="mt-5">

```text
DESCARTADO | [25]       [30]       [35] | DESCARTADO
  1 ... 25 |  26 ...     31  ...    36  | 37 ... 100
              ↑           ↑          ↑
            bajo        centro      alto
```

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Nuevo rango activo
Valores: **26 a 36**

`bajo = 25`  
`alto = 35`
$$
centro=\left\lfloor\frac{25+35}{2}\right\rfloor=30
$$
`A[30] = 31`

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### Comparación
$$
31 = 31
$$
🎯 **¡Correcto!**

La búsqueda termina.

</div>

</div>

<div class="mt-6 text-center text-2xl">**Resultado: solamente 4 comparaciones.**</div>

---
layout: default
---

# Visualización completa de la reducción

<div class="text-base mt-1 text-center">

El arreglo es el mismo; en cada iteración se **reduce el rango activo**.

</div>

<div class="grid grid-cols-2 gap-5 mt-2">

<div>

### Iteraciones 1 y 2

```text
ITERACIÓN 1
[ 1 ....... 31 ....... 50 ....... 100 ]
  ↑                   ↑             ↑
 bajo               centro         alto
31 < 50 → descartamos 50 ... 100
          nuevo rango: 1 ... 49

ITERACIÓN 2
[ 1 ... 25 ... 31 ... 49 | 50 ... 100 ]
  ↑     ↑             ↑
 bajo centro         alto
31 > 25 → descartamos 1 ... 25
          nuevo rango: 26 ... 49
```

</div>

<div>

### Iteraciones 3 y 4

```text
ITERACIÓN 3
[ 1...25 | 26 ... 31 ... 37 ... 49 | 50...100 ]
         ↑             ↑         ↑
       bajo          centro     alto
31 < 37 → descartamos 37 ... 49
          nuevo rango: 26 ... 36

ITERACIÓN 4
[ 1...25 | 26 ... 31 ... 36 | 37 ....... 100 ]
         ↑         ↑       ↑
       bajo      centro   alto
31 = 31 → ¡ENCONTRADO! ✓
```

</div>

</div>

<div class="mt-2 py-2 px-4 rounded-lg bg-green-50 dark:bg-green-900/30 text-center">

🎯 **100 posibilidades → 4 comparaciones → 31 encontrado ✓**

</div>

---
layout: default
---
# ¿Por qué es tan eficiente?
<div class="text-xl mt-5">

La búsqueda binaria no elimina una opción en cada paso: elimina aproximadamente **la mitad del espacio de búsqueda**.

</div>

<div class="mt-8 text-center text-2xl">

$$
100 \rightarrow 50 \rightarrow 25 \rightarrow 13 \rightarrow 7 \rightarrow 4 \rightarrow 2 \rightarrow 1
$$

</div>

<div class="grid grid-cols-2 gap-8 mt-10">

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### Búsqueda lineal
Elimina aproximadamente **1 opción por comparación**.
```text
100 → 99 → 98 → 97 → ...
```

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### Búsqueda binaria
Elimina aproximadamente **la mitad por comparación**.
```text
100 → 50 → 25 → 13 → ...
```

</div>

</div>

<div class="mt-8 text-center text-xl">

Esta reducción repetida es la esencia de la estrategia **Divide y Vencerás**.

</div>

---
layout: default
---
# Peor caso: ¿cuántas comparaciones?
<div class="text-xl mt-5">

Para saber cuántas veces podemos dividir el problema entre 2 utilizamos el logaritmo en base 2.

</div>

<div class="mt-8 text-center">

$$
k = \lceil \log_2(n) \rceil
$$

</div>

<div class="mt-8 text-center text-xl">

Para un rango de **100 elementos**:
$$
\log_2(100) \approx 6.64
$$
$$
\lceil 6.64 \rceil = 7
$$

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="p-5 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### Máximo
**7 comparaciones** para 100 elementos.

</div>

<div class="p-5 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### ¿Por qué?
$$
2^7 = 128 \ge 100
$$

</div>

</div>

---
layout: default
zoom: 0.95
---
# Búsqueda Binaria: resumen
<div class="grid grid-cols-2 gap-7 mt-7 text-lg">

<div class="p-5 rounded-xl">

### Requisito
Los datos deben estar **ordenados**.

</div>

<div class="p-5 rounded-xl">

### Estrategia
Comparar siempre con el **elemento central**.

</div>

<div class="p-5 rounded-xl">

### En cada paso
Se descarta aproximadamente **la mitad del rango**.

</div>

<div class="p-5 rounded-xl">

### Complejidad temporal
$$
O(\log n)
$$

</div>

</div>

<div class="mt-9 p-6 rounded-xl bg-green-50 dark:bg-green-900/30 text-center text-xl">

### Ejemplo del número 31
**50 → 25 → 37 → 31 ✓**

Solo **4 comparaciones** frente a las **31 comparaciones** de la búsqueda lineal.

</div>

<div class="mt-7 text-center text-xl">

💡 A medida que `n` crece, la diferencia entre **$O(n)$** y **$O(\log n)$** se vuelve cada vez mayor.

</div>

---
layout: default
---

# La conexión clave con la estructura de datos

<div class="mt-8 text-center">

## ¿Por qué funciona la búsqueda binaria?

</div>

<div class="mt-10 text-xl text-center">

La búsqueda binaria puede descartar la mitad de los elementos después de cada comparación.

</div>

<div class="mt-8 mx-auto max-w-4xl p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### 🤔 Entonces, ¿qué propiedad de la estructura de datos hace esto posible?

</div>

<div class="mt-8 text-center">

<div class="text-4xl font-bold">

El orden de los datos

</div>

<div class="mt-4 text-xl">

Los elementos deben estar **previamente ordenados**.

</div>

</div>

<div class="mt-8 text-center text-lg">

Sin esta propiedad, una comparación con el elemento central **no permitiría decidir qué mitad descartar**.

</div>
---
layout: default
zoom: 0.90
---

# Requisito: los datos deben estar ordenados

<div class="text-xl mt-5">

La búsqueda binaria puede descartar la mitad del espacio de búsqueda porque conoce la **relación de orden** entre los elementos.

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30">

### ✅ Vector ordenado

```text
[ 1 | 2 | 3 | 4 | 5 | ... | 50 | ... | 100 ]
                              ↑
                            centro
```

Si buscamos `31`:

$$
31 < 50
$$

Entonces sabemos que `31` solamente puede estar **a la izquierda**.

<div class="mt-5 text-center">

**Podemos descartar toda la mitad derecha.**

</div>

</div>

<div class="p-6 rounded-xl bg-red-50 dark:bg-red-900/30">

### ❌ Vector desordenado

```text
[ 42 | 7 | 99 | 18 | 63 | 4 | 31 | 85 | ... ]
                         ↑
                       centro
```

Aunque comparemos con el elemento central, no sabemos si `31` está:

**← a la izquierda**

o

**a la derecha →**

<div class="mt-5 text-center">

**No podemos descartar ninguna mitad.**

</div>

</div>

</div>

---
layout: default
zoom: 0.94
---

# Algoritmo + Estructura de Datos

<div class="text-xl mt-5 text-center">

La eficiencia de un algoritmo no depende únicamente de sus instrucciones.

</div>

<div class="mt-10 flex justify-center items-center gap-6 text-2xl">

<div class="p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### Estructura de datos

Vector **ordenado**

</div>

<div class="text-4xl">

+

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### Algoritmo

Búsqueda **binaria**

</div>

<div class="text-4xl">

→

</div>

<div class="p-6 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-center">

### Eficiencia

$$
O(\log n)
$$

</div>

</div>

<div class="mt-10 p-7 rounded-xl bg-purple-50 dark:bg-purple-900/30 text-center text-xl">

### 💡 Principio fundamental

**Los algoritmos eficientes están estrechamente ligados a las propiedades de las estructuras de datos sobre las cuales operan.**

</div>

<div class="mt-8 text-center text-xl">

La propiedad de **ordenamiento** es precisamente lo que permite a la búsqueda binaria eliminar la mitad de las posibilidades en cada iteración.

</div>

---
layout: default
zoom: 0.75
---

# Búsqueda Lineal vs. Búsqueda Binaria

<div class="text-xl mt-4 text-center">

Dos estrategias para resolver el mismo problema, pero con **requisitos y eficiencias diferentes**.

</div>

<div class="mt-7">

| Característica | 🔵 Búsqueda Lineal | 🟢 Búsqueda Binaria |
|---|---|---|
| **Estrategia** | Compara elemento por elemento | Compara con el elemento central |
| **¿Requiere datos ordenados?** | ❌ **No** | ✅ **Sí** |
| **Uso del orden** | No utiliza el orden para buscar | Utiliza el orden para descartar la mitad |
| **Avance** | Una posición a la vez | Reduce el rango aproximadamente a la mitad |
| **Datos permitidos** | `[42, 7, 99, 18, 31...]` | `[1, 2, 3, 4, 5...]` |
| **Peor caso para n = 100** | Hasta **100 comparaciones** | Hasta **7 comparaciones** |
| **Complejidad temporal** | $O(n)$ | $O(\log n)$ |

</div>

<div class="grid grid-cols-2 gap-8 mt-7">

<div class="p-5 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### 🔵 Búsqueda Lineal

**“¿Este es el elemento que busco?”**

<div class="mt-3 text-lg">

Si no es, simplemente avanza al **siguiente elemento**.

</div>

</div>

<div class="p-5 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### 🟢 Búsqueda Binaria

**“¿Este es el elemento que busco?”**

**“Si no es, ¿en qué dirección debo continuar?”**

<div class="mt-3 text-lg">

El **orden** permite decidir qué mitad descartar.

</div>

</div>

</div>

<div class="mt-7 p-5 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-center text-xl">

💡 **Idea clave:** La elección de una estructura de datos y las propiedades que posee pueden determinar qué algoritmos podemos aplicar y qué tan eficiente será la solución.

</div>

---
layout: default
---

# Entonces… ¿qué significa que un algoritmo sea eficiente?

<div class="text-xl mt-5">

El juego de búsqueda nos permitió resolver **el mismo problema** mediante dos estrategias diferentes:

</div>

<div class="grid grid-cols-2 gap-8 mt-2">

<div class="p-6 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### 🔵 Búsqueda Lineal

Puede trabajar con datos **ordenados o desordenados**.

Revisa los elementos **uno por uno**.

$$
O(n)
$$

</div>

<div class="p-6 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### 🟢 Búsqueda Binaria

Aprovecha una propiedad de la estructura:

**los datos están ordenados**.

Descarta aproximadamente **la mitad** en cada paso.

$$
O(\log n)
$$

</div>

</div>
---
layout: default
---
<div class="mt-7 p-6 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-center text-xl">

### 💡 Primera conclusión

**Elegir un algoritmo implica considerar cómo están organizados los datos y cuántos recursos requiere la estrategia para resolver el problema.**

</div>

<div class="mt-7 text-center text-2xl">

Pero… ¿cómo podemos **medir y comparar** formalmente ese costo?

</div>

<div class="mt-5 text-center text-xl">

⏱️ **Tiempo de ejecución** &nbsp;&nbsp;&nbsp;&nbsp; 💾 **Espacio en memoria**

</div>

<div class="mt-6 text-center text-2xl">

### → Esto nos lleva al análisis de la eficiencia de los algoritmos.

</div> 


---
layout: default
---

# Una última idea: resolver tiene un costo

<div class="text-lg mt-3 text-center">

Dos algoritmos pueden resolver correctamente el mismo problema y, sin embargo, **no requerir el mismo esfuerzo computacional**.

</div>

<div class="mt-5 text-center text-xl">

### En computación, cuando hablamos de **costo**, no hablamos de dinero.

</div>

<div class="grid grid-cols-2 gap-6 mt-5">

<div class="p-5 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### ⏱️ Tiempo

**¿Cuánto trabajo debe realizar el algoritmo?**

<div class="mt-2 text-lg">

Operaciones, comparaciones o pasos necesarios para resolver el problema.

</div>

</div>

<div class="p-5 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### 💾 Espacio

**¿Cuánta memoria necesita?**

<div class="mt-2 text-lg">

Recursos de memoria utilizados durante la ejecución.

</div>

</div>

</div>


---
layout: default
zoom: 0.92
---

# Una idea que retomaremos más adelante

<div class="mt-3 text-center text-lg">

Durante los ejemplos de búsqueda aparecieron dos expresiones:

</div>

<div class="grid grid-cols-2 gap-6 mt-5">

<div class="p-4 rounded-xl bg-blue-50 dark:bg-blue-900/30 text-center">

### Búsqueda Lineal

<div class="text-3xl mt-1">

$$
O(n)
$$

</div>

El trabajo aumenta conforme aumenta la cantidad de datos.

</div>

<div class="p-4 rounded-xl bg-green-50 dark:bg-green-900/30 text-center">

### Búsqueda Binaria

<div class="text-3xl mt-1">

$$
O(\log n)
$$

</div>

El trabajo crece mucho más lentamente al aumentar la cantidad de datos.

</div>

</div>

<div class="mt-4 p-4 rounded-xl bg-yellow-50 dark:bg-yellow-900/30 text-center text-lg">

### 💡 Por ahora, quedémonos con esto:

Estas expresiones describen **cómo crece el trabajo de un algoritmo cuando aumenta la cantidad de datos**.

</div>

<div class="mt-4 text-center text-xl font-bold">

¿Cómo podemos medir y comparar formalmente ese crecimiento?

</div>

<div class="mt-2 text-center text-lg">

→ Lo estudiaremos al abordar la **complejidad algorítmica**.

</div>