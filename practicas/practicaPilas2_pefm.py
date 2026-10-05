expresion = "a + b) * (c - d)"
pila = []
valida = True

for caracter in expresion:
    if caracter == "(":
        pila.append(caracter)
    elif caracter == ")":
        if len(pila) == 0:
            valida = False
            break
        pila.pop()
    print(pila)

if len(pila) != 0:
    valida = False

print("Balanceada" if valida else "No balanceada")