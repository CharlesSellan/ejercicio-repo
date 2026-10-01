def f(lista, n, direction):
    n = n % len(lista)

    if direction == "right":
        return lista[-n:] + lista[:-n]
    elif direction == "left":
        return lista[n:] + lista[:n]
    else:
        raise ValueError("La dirección debe ser 'left' o 'right'")
nu = [2,4,1,3,7,9]

print(f(nu,2,"right"))
print(f(nu,3,"left"))