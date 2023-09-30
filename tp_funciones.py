



import funciones
suma=0
while True:
    num=int(input('ingrese num, ingrese 0 para terminar: '))
    if num==0:
        break
    else:
        suma+=num

        result=funciones.add_digits(num)
        
        print(f'la suma de los digitos es: {result}')
        
print(f'la suma de los numeros es: {suma}')      
result2=funciones.add_digits(suma)
print(f'la suma de digitos de la suma es: {result2}')


import random
palabras=['laptop','mouse','teclado']
palabraA=random.choice(palabras)
spaces=['_']*len(palabraA)
