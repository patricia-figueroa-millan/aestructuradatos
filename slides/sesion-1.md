---
background: ../background3.jpg
title: Algoritmia y Estructura de Datos
class: text-center flex items-center justify-center h-full
transition: slide-left
---

<style src="../styles/index.css"></style>

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
<br>
<br>

<!--Read more about [Why Slidev?](https://sli.dev/guide/why)
You can have `style` tag in markdown to override the style for the current page.
Learn more: https://sli.dev/features/slide-scope-style
-->

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Here is another comment.
-->

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
zoom: 0.84
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