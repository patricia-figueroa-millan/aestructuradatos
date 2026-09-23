import numpy as np

temperaturas = np.array(
    [23.5,18.7,22.4,32.5,30.5]
    )

print(temperaturas)
print(type(temperaturas))

print(temperaturas>28)

temp_altas = temperaturas[temperaturas>28]
print(temp_altas)
print(type(temp_altas))

print(temperaturas.sum())
print(temperaturas.mean())
print(temperaturas.min())
print(temperaturas.max())
ordenado = np.sort(temperaturas)
print(ordenado)
cumple = np.where(temperaturas>30)
print(cumple)

arreglob = np.append(temperaturas,45.5)
print(arreglob)

#print(temperaturas.append(40.5))

arregloc = np.insert(temperaturas,1,12)
print(arregloc)