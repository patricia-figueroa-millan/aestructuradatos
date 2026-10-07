from collections import deque

cola = deque()

cola.append("Ana")
cola.append("Luis")
cola.append("Carlos")

print(cola)

atendido = cola.popleft()

print("Se atendió a:", atendido)
print("Cola:", cola)

print("Siguiente:", cola[0])