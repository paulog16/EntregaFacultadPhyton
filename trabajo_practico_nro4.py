"""1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
"""

"""crear un bucle while con las siguientes caracteristicas
-El valor inicial de la variable x tiene que ser 0
-El valor se va a incrementar en 1
-La condicion de salida del bucle es cuando x sea mayor o igual a 30
-se debe romper el ciclo cuando x sea 15
-hay que ir mostrando el valor de x
-se debe omitir cuando x sea 4,6 y 10
-cuando x tenga esos valores se debe indicar que se saltea
-cuando el bucle termine escribimos "el bucle se corto cuando x era: x "
"""
x = 0
while True:
    x += 1
    if x >= 30:
        break
    if x == 15:
        break
    if x == 4 or x == 6 or x == 10:
        print(f"el numero {x} se saltea")
    else:
        print(x)
print(f"el bucle termino por que el valor de x es {x}")

"""1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas."""

while True:
    word = input("ingrese palabra: ")
    if word == "":
        break
    else:
        print(word.upper())

    """2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350
"""
total = 0
while True:
    inp = input("")
    if inp == "":
        break
    operation, mont = inp.split()  # separa la frase en cadenas separadas
    mont = int(mont)

    if operation.upper() == "D":
        total += mont
    elif operation.upper() == "R":
        total -= mont
print(f"el monto total es: {total}")

"""3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
"""
contCousin = 0

while True:
    n = int(input("ingrese numero: "))
    if n == 0:
        break
    es_primo=True #declaro una variable si es o no primo
    if n>1: #verifico que el numero sea mayor a 1
        for i in range(1,n+1): #recorro del 1 hasta el n
            if n %i==0: #si el n % i ==0
                es_primo=False #no es primo
                break

    if es_primo:
        contCousin+=1        

print(f"cantidad de n primos: {contCousin}")

'''4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
'''

firtsYear=int(input('ingrese el primer año: '))
SecondYear=int(input('ingrese el segundo año: '))

for leap_year in range(firtsYear,SecondYear+1):
    if (leap_year%4==0 and leap_year%100!=0) or leap_year%400==0:
        print(leap_year)


'''5.Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.'''

for i in range(1,21):
    if i % 2!=0:
        continue
    print(i)

'''6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.'''  

nums=[2,3,4,5,2,1,4,8,9]
numE=int(input('what search a number: '))
for i in nums:
    if nums[i]==numE:
        break
    print(i)
print(f'la lista salio en el numero: {numE} y era la posicion {i}')    


'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).'''

while True:
    options=input('OPCIONES: 1-2-3: ')
    if options=='0':
        break
    if options=='1':
        print('usted eligio la opcion 1')
    elif options=='2':
        print('usted eligio la opcion 2')
        
    elif options=='3':
        print('usted eligio la opcion 3')
    else:
        print('opcion invalida, elija otra: ')
                                
