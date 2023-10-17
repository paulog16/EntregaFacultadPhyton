def multiplo(a, b):
    if a == 1: #si a es 1, es verdadero por que todos los numeros son multiplos de 1
        return True
    if a < b: # si b es mas grande que a es falso por que para que pueda ser multiplo tiene que ser mas chico
        return False
    if a % b == 0: # si a % b ==0 retorna a//b,b ej, 16//2,2 = 8,2, y vuelve a repetir el proceso
        return multiplo(a//b, b)
    return False


a = 42
b = 6
resultado = multiplo(a, b)
print(resultado)