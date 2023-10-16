#metodo de burbuja
def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
       
        intercambio = False

        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambio = True

        if not intercambio:
            break


lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_burbuja(lista)
print("Lista ordenada:")
print(lista)

#metodo de seleccion
def ordenamiento_seleccion(arr):
    n = len(arr)

    for i in range(n):
    
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_seleccion(lista)
print("Lista ordenada:")
print(lista)

#tipo de insercion

def ordenamiento_insercion(arr):
    n = len(arr)

    for i in range(1, n):
        elemento_actual = arr[i]
        j = i - 1

       
        while j >= 0 and elemento_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

    
        arr[j + 1] = elemento_actual


lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_insercion(lista)
print("Lista ordenada:")
print(lista)

#combinar ordenamiento

def ordenamiento_hibrido(arr, umbral=10):
    n = len(arr)

    if n <= umbral:
        # Utilizar ordenamiento por inserción para listas pequeñas
        ordenamiento_insercion(arr)
    else:
        # Utilizar ordenamiento de mezcla (Merge Sort) para listas más grandes
        ordenamiento_mezcla(arr)

def ordenamiento_mezcla(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        # Recursivamente, ordenar ambas mitades
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        i = j = k = 0

        # Copiar datos a las mitades temporales izquierda y derecha
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Comprobar si hay elementos restantes
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_hibrido(lista)
print("Lista ordenada:")
print(lista)