import numpy as np

ceros = np.zeros(5)
unos = np.ones(5)
secuencia = np.arange(0,10,2)

print(ceros)
print(unos)
print(secuencia)
print(type(secuencia))
print(secuencia.dtype)
print(secuencia.shape)
print(secuencia.ndim)
print(secuencia.size)
print(secuencia[-1])
secuencia[-1]=10
print(secuencia)
print(secuencia[1:4])
print(secuencia[:3])
print(secuencia[::4])