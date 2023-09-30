import funciones15
fact=1
cont=0
while True:
   
    n=int(input('ingrese un numero, ingrese 0 para salir del programa: '))
    cont+=1
    funciones15.fact(fact,n)
    if n==0:
        break
print(f'se ingresaron {cont} numeros')    