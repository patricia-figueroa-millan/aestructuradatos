import numpy as np

temperaturas = np.array(
    [
    24.5, 25.1, 25.8, 26.4, 28.2, 45.5,
    31.2, 32.1, 31.7, 29.8, 27.4, 26.0
]
)
print(temperaturas)

#Inspección del arreglo
cantidad = temperaturas.size
tipo = temperaturas.dtype
forma = temperaturas.shape
print("Cantidad: ", cantidad, 
      "Tipo:", tipo, 
      "Forma:", forma)

print(temperaturas>40)
posiciones = np.where(temperaturas>40)
print(posiciones)
print(temperaturas[posiciones])

temperaturas[posiciones] = 30.5
print(temperaturas)

#comportamiento temperaturas
minima = temperaturas.min()
maxima = temperaturas.max()
promedio = temperaturas.mean()
print("Minima", minima)
print("Maxima", maxima)
print("Promedio", promedio)

sobre_promedio = np.where(temperaturas>promedio)
print(sobre_promedio)
print(temperaturas[sobre_promedio])

posiciones_max = np.where(temperaturas == maxima)
print(posiciones_max)
print(temperaturas[posiciones_max])

print(
    "Temperatura máxima:",
    maxima,
    "en la posición:",
    posiciones_max[0][0]
)