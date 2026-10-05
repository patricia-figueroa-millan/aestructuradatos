#Gestión de tareas con listas

tareas = [
    "Monitorización de mediciones",
    "Generar reporte",
    "Respaldar base de datos",
    "Enviar resultados"
]

#O(1) por que Python ya conoce la longitud
#de la estructura creada y cantidad de elementos.
cantidad_tareas = len(tareas)
print("Cantidad de tareas:", cantidad_tareas)

#Acceder a tarea 2 por posición conocida
#O(1) por que ya se conoce la posición y se accede
#directamente
print("Tarea 2:", tareas[1])

#Modificar tarea con base en el índice de ésta
#O(1)
tareas[1] = "Generar reporte específico"
print(tareas)

#Agregar una tarea a la lista
#O(1) amortizado por que se agrega al final
tareas.append("Actualizar sistema")

#Agregar al princio de la lista
#O(n) por que reindexa y dezplaza todos los elemtnos
#n
tareas.insert(0,"Atender alerta")
print(tareas)

#Eliminar la ultima tarea de la lista
#O(1) por que elimina la ultima posición conocida
tareas_completadas =tareas.pop()
print(tareas_completadas)
print(tareas)

#Eliminar primera tarea
#O(n) por que regresa a la posición 0 y sucesivamente
#el resto de las tareas afectando a todos los
#elementos n
tareas_completadas=tareas.pop(0)
print("Tareas completadas", tareas_completadas)
print("Tareas:",tareas)

#Buscar tarea en la lista tareas
tarea_encontrada = "Enviar resultados" in tareas
print(tarea_encontrada)

#Encontrar el indice de la tarea encontrada
posicion_tarea_encontrada = tareas.index("Enviar resultados")
print("Posición de la tarea encontrada: ", posicion_tarea_encontrada)

#Eliminar por valor
#O(n)
tareas.remove("Enviar resultados")
print(tareas)

tareas_nuevas = [
    "Revisar red",
    "Validar datos",
    "Documentar cambios"
]

#O(k)
tareas.extend(tareas_nuevas)
print(tareas)

#O(k)
primeras = tareas[:3]
print("Rebanada 1 de las lista:", primeras)

#O(n)
tareas.sort()
print(tareas)
