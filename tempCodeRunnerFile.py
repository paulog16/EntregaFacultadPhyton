def posiciones(a, b, start=0, positions=None):
    if positions is None:
        positions = []

    if start >= len(a):
        return positions

    index = a.find(b, start)

    if index != -1:
        positions.append(index)
        return posiciones(a, b, index + 1, positions)
    else:
        return positions

# Ejemplo de uso
a = "un tete a tete con Tete"
b = "te"
result = posiciones(a, b)
print(result)