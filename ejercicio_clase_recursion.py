# 1

import random


def rata(x):
    cont = 0
    if cont >= 7:
        return 'la rata salio de la caja'
    if x == 1:
        print('la rata eligio el camino 1, regresa cada 3 minutos')
        return rata(cont+3)
    elif x == 2:
        print('la rata eligio el camino 2, regresa cada 5 minutos')
        return rata(cont+5)
    else:
        print('la rata eligio el camino 3, salio de la jaula despues de 7 min')
        return 'la rata salio de la caja'


num = random.randint(1, 3)
res = rata(num)
print(res)

# 2
# n=int


def f(n):
    s = str(n)  # s es n pero como string
    if len(s) >= 1:  # si la longitud de s es mayor o igual a 1 retorna s, que es n pero en string
        return s
    # sino retorna el ultimo caracter de s+los caracteres excepto el ultimo de s pero como entero, que es n
    return s[-1]+f(int(s[:-1]))


num = 3
res = f(num)
print(res)
# enunciado:

# hacer una funcion recursiva donde dentro se declare una variable str con el valor de un entero, luego retornar el ultimo caracter de la variable str concatenado con la variable entera excepto el ultimo caracter, si la longitud de la variable str es mayor o igual a 1 se retorna la variable str.

# supongo que return s[-1]+f(int(s[:-1])) da el mismo numero ya que tendria que ser un solo numero para que retorne esto
