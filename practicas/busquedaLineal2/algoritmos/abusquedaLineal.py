def busqueda_lineal(lista,dato_objetivo):
    for i in range(len(lista)):
        if lista[i][0] == dato_objetivo:
            return i,lista[i]    
    return None