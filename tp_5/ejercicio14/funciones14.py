def es_primo(n):
    if n==2:
        return True
    if n<2:
        return False

    for  i in range(2,n-1):
        if n%1==0:
            return False

    return True               