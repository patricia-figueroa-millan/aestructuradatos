def busquedaBinaria(lista, dato_objetivo):

    # Definir los límites iniciales de búsqueda
    inicio = 0
    fin = len(lista) - 1

    # Repetir mientras exista un intervalo válido de búsqueda
    while inicio <= fin:
        # Calcular la posición central del intervalo
        medio = (inicio + fin) // 2

        # Comparar el código del producto central con el objetivo
        # medio determina el índice de la fila central del intervalo, por eso
        # se pasa como primer índice.
        # verifica que el valor en esa posición de fila y columan sea el código objetivo
        if lista[medio][0] == dato_objetivo:
            # Si coincide, devolver su posición y el registro completo
            return medio, lista[medio]

        # Si el objetivo es menor, buscar en la mitad izquierda
        elif dato_objetivo < lista[medio][0]:
            # Descartar el elemento central y la mitad derecha
            fin = medio - 1
        # Si el objetivo es mayor, buscar en la mitad derecha
        else:
            # Descartar el elemento central y la mitad izquierda
            inicio = medio + 1

    # Si se agota el intervalo sin encontrar el producto
    return None