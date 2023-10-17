# 1.Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
def contdig(n):
    cont = 1
    if n < 10:
        return 1
    else:
        return cont + contdig(n//10)


num = 1234
res = contdig(num)
print(res)

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.


def multiplo(a, b):
    if a == 1:  # si a es 1, es verdadero por que todos los numeros son multiplos de 1
        return True
    if a < b:  # si b es mas grande que a es falso por que para que pueda ser multiplo tiene que ser mas chico
        return False
    if a % b == 0:  # si a % b ==0 retorna a//b,b ej, 16//2,2 = 8,2, y vuelve a repetir el proceso
        return multiplo(a//b, b)
    return False


a = 42
b = 6
resultado = multiplo(a, b)
print(resultado)
