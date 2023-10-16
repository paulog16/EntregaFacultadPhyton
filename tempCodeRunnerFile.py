libros = [
    {"titulo": "Iron Man", "autor": "G.Paulo Guidolin", "año": 2002},
    {"titulo": "Cenicienta", "autor": "Disney", "año": 1967},
    {"titulo": "El extraño mundo de jack", "autor": "Sheckpeasre", "año": 1860},

]

# Función para ordenar la lista de libros en función de un campo específico
def ordenar_libros_por_campo(libros, campo):
    return sorted(libros, key=lambda x: x[campo])

# Campo por el que deseamos ordenar los libros (en este caso, "año")
campo_ordenamiento = "año"

# Llamamos a la función de ordenamiento
libros_ordenados = ordenar_libros_por_campo(libros, campo_ordenamiento)

# Imprimimos la lista de libros ordenada
for libro in libros_ordenados:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}")