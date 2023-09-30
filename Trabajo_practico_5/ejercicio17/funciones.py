def es_primo(a):
    if a==2:
        return True
    if a<2:
        return False
    for i in range(2,a-1):
        if a%i==0:
            return False
    return True        

def fact(f,a):
    for i in range(1,a+1):
        f*=i
    print(f'el factorial de {a} es {f}')            