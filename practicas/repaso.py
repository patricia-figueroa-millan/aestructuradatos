matrizM = [
    [12,  7, 18, 9],
    [ 5, 21, 14,16],
    [ 8, 11, 25, 6],
    [19, 13, 10,17]
]
#acceso
print("Fila[0] Col[1]",matrizM[0][1])
#modificación
matrizM[2][2] = 45 #25 a 45
print("Fila[2] col[2]",matrizM[2][2])

for fila in matrizM:
    for col in fila:
        print(col)

print("******")
#fila 0
for fila in matrizM[0]:
    print(fila)

#columna 0
print("-----")
for fila in matrizM:
    print(fila[0])

maj = matrizM[0][0]

for fila in matrizM:
    for col in fila:
        if col > maj:
            maj = col

print(maj)

#def search_maj():
#    for x in matrizM:
#        

#search_maj()