def f(n):
    s = str(n)  # s es n pero como string
    if len(s) >= 1:  # si la longitud de s es mayor o igual a 1 retorna s, que es n pero en string
        return s
    # sino retorna el ultimo caracter de s+los caracteres excepto el ultimo de s pero como entero, que es n
    return s[-1]+f(int(s[:-1]))


num = 3
res = f(num)
print(res)