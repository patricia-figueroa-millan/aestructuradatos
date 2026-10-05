import numpy as np

temperaturas = np.array(
    [
    24.5, 25.1, 25.8, 26.4, 28.2, 45.5,
    31.2, 32.1, 31.7, 29.8, 27.4, 26.0
    ]
)

print(temperaturas)
print("Cantidad:", temperaturas.size)
print("Tipo elementos:", temperaturas.dtype)
print("Forma del arreglo", temperaturas.shape)

posiciones = np.where(temperaturas>40)
print(posiciones)
print(temperaturas[posiciones])

#Acceso mediante posición y asignación de nuevo valor
temperaturas[posiciones]= 30.5
print(temperaturas)

#Comportamiento de temperaturas
minima = temperaturas.min()
maxima = temperaturas.max()
promedio = temperaturas.mean()
print(minima) #minima
print(maxima) #máxima
print(promedio) #media

sobre_promedio = np.where(temperaturas>promedio)
print(sobre_promedio)
print(temperaturas[sobre_promedio])
print(temperaturas[sobre_promedio].size)

posicion_max = np.where(
    temperaturas == maxima
)

print(posicion_max)

print(
    "Temperatura máxima:",
    maxima,
    "en la posición:",
    posicion_max[0][0]
)