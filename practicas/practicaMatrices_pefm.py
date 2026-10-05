
temperaturas = [
    [24,27,29,31,28],
    [23,26,30,32,29],
    [25,28,31,33,30]
]

print("Filas matriz:",len(temperaturas)) # 3 cantidad de filas
print("Longitud fila [0]",len(temperaturas[0])) #5 longitud de la primera filas

#Primer índice fila [1] y segundo índice [columna]
#Acceso a un elemento en matriz
#O(1)
print(temperaturas[1][2])

#Modificación de valor por posición
#O(1)
temperaturas[1][2]= 32
print(temperaturas)

#O(c)
#Impresión de temperaturas del día lunes
for t in temperaturas[0]:
    print(t) 