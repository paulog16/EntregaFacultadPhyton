import funciones
nummayor=0
fact=1
while True:
    num=int(input('ingrese un numero primo: '))
    if num>nummayor:
        nummayor=num
    if funciones.es_primo(num):
        sumadigit=0
        contf=0
        for i in str(num):
            sumadigit+=int(i)
        print(f'la suma de los digitos es: {sumadigit}')
        frec=int(input('ingrese un numero a buscar en el numero: '))
        for i in str(num):
            if str(frec)==i:
                contf+=1
        print(f'el numero {frec} se encuenta {contf} en el numero {num}')
                        
    if not funciones.es_primo(num):
        break
funciones.fact(fact,nummayor)    