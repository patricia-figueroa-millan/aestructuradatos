
temperaturas = [
    [24,27,29,31,28],
    [23,26,30,32,29],
    [25,28,31,33,30]
]

#Acceder a un elemento de la matriz
#por posición
#O(1)
print(temperaturas[1][3])

#Modificar elemento de la matriz por posición
#O(1)
temperaturas[1][3] = 40
print(temperaturas)

#Obtener las temperaturas de la fila [0]
#O(c) cantidad de columnas de la fila [0]
for t in temperaturas[0]:
    print(t)

print("*******")
#O(n^2)
for fila in temperaturas:
    for t in fila:
        print(t)

#O(c)
lunes = temperaturas[0]
promedio_temp_lunes = sum(lunes)/len(lunes)
print(promedio_temp_lunes)

#Promedio de temperaturas de cada dia.
#O(n^2)
#sum(fila) procesa c elementos y lo hacemos
#f veces, entonces f*c = O(f*c)
for fila in temperaturas:
    promedio = sum(fila)/len(fila)
    print(promedio)

#Obtener temperatura mayor manualmente
mayor = temperaturas[0][0]
for fila in temperaturas:
    for t in fila:
        if t > mayor:
            mayor = t

print("temperatura mayor:", mayor)
