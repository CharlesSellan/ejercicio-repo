def rotar_circular(lista, n, direccion):
    if not lista:
        return lista
    
    n = n % len(lista)
    
    if direccion == 'right':
        return lista[-n:] + lista[:-n]
    elif direccion == 'left':
        return lista[n:] + lista[:n]
    else:
        raise ValueError("La dirección debe ser 'right' o 'left'")

# Caso de prueba solicitado en la P1
lista_original =
resultado = rotar_circular(lista_original, 2, 'right')

print(f"Entrada: {lista_original}")
print(f"Salida:  {resultado}")
