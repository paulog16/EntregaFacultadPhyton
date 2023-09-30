def dicc(cadena):
    palabras=cadena.split()
    dicc={}

    for palabra in palabras:
        palabra = palabra.strip('.,!?"\'') #elimina estos caracteres
        dicc[palabra]=len(palabra)

    return dicc    