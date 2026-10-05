matrizM = [
    [12, 7,18, 9],
    [5 ,21,14,16],
    [8 ,11,25, 6],
    [19,13,19,17]
]

mayor = matrizM[0][0]
for fila in matrizM:
    for valor in fila:
        if valor > mayor:
            mayor = valor

print("Valor máximo:", mayor)