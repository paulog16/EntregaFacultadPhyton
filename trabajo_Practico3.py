# 1-Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
name=input('ingrese una palabra: ')
for p in range(11):
    print(name)
# 2-Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age=int(input('ingresa tu edad: '))
for i in range(1,age):
    print(i)

# 3-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
number=int(input('ingrese un numero'))
for i in range(1,number+1):
    if (i % 2 !=0):
        print(f'{i},')
# 4-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number=int(input('type number integer: '))
for p in range(number,-1,-1):
    print(f'{p},')
    
# 5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


cashInverted=float(input('cuanta plata vas a invertir: '))
interestAnual=float(input('cuanto interes anual? '))
ages=int(input('por cuantos años el plazo fijo: '))
interestAnual=interestAnual/100
for p in range(1,ages):
    cashInverted+=cashInverted*interestAnual
    print(f'capital obtenido {cashInverted}')

# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
    hight=int(input('ingrese altura: '))
    for i in range(1, altura + 1):
        print('*' * i)

# 7-Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1):
    print('tabla del 1')
    for j in range(1,10):
        print(f'{i} x {j} es : {i*j}')
# 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

number=int(input('ingrese un numero: '))
for i in range(1,number+1,2):           
        for j in range(i,0,-2):
            print(j,end='')
        print('')


#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password='Godoycruz'
while True:
    password2=input('ingrese contraseña: ')
    if password2==password:
        break

print('contraseña correcta')
#10-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
number=int(input('ingrese un numero: '))
if (number%number==0)and(number%1==0):
    print('primo')
else:
    print('no primo')  
# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word=input('ingrese una palabra: ')
for i in word[::-1]: #esto hace que lea de atras hacia adelante
    print(i) 

#12-Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
sentence=input('ingrese frase: ')
letter=input('ingrese letra a buscar: ')
contLetter=0
for i in sentence:
    if i==letter: #i recorre toda la frase, si la i es igual a la letra que le decimos, el contador suma 1
        contLetter+=1
print(f'la letra {letter} se encuentra {contLetter} veces ')

#13-Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    word=input('ingrese palabra: ')
    print(word)
    if word=='salir':
        break
print('salio')
#14-Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.


#15-Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
divisores=[]
number=int(input('ingrese numero: '))
for num in range(1,number+1): #recorre del 1 hasta el numero ingresado
    if number%num==0: # se fija si la posicion en la que va es divisor del numero
        divisores.append(num)

print(f'los divisores de ese numero son {divisores}')        


   



    
    


