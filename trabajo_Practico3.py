# 1-Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
name = input("ingrese una palabra: ")
for p in range(11):
    print(name)
# 2-Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("ingresa tu edad: "))
for i in range(1, age):
    print(i)

# 3-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
number = int(input("ingrese un numero"))
for i in range(1, number + 1):
    if i % 2 != 0:
        print(f"{i},")
# 4-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("type number integer: "))
for p in range(number, -1, -1):
    print(f"{p},")

# 5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


cashInverted = float(input("cuanta plata vas a invertir: "))
interestAnual = float(input("cuanto interes anual? "))
ages = int(input("por cuantos años el plazo fijo: "))
interestAnual = interestAnual / 100
for p in range(1, ages):
    cashInverted += cashInverted * interestAnual
    print(f"capital obtenido {cashInverted}")

    # 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
    hight = int(input("ingrese altura: "))
    for i in range(1, altura + 1):
        print("*" * i)

# 7-Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1):
    print("tabla del 1")
    for j in range(1, 10):
        print(f"{i} x {j} es : {i*j}")
# 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

number = int(input("ingrese un numero: "))
for i in range(1, number + 1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print("")


# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = "Godoycruz"
while True:
    password2 = input("ingrese contraseña: ")
    if password2 == password:
        break

print("contraseña correcta")
# 10-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
number = int(input("ingrese un numero: "))
if (number % number == 0) and (number % 1 == 0):
    print("primo")
else:
    print("no primo")
# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = input("ingrese una palabra: ")
for i in word[::-1]:  # esto hace que lea de atras hacia adelante
    print(i)

# 12-Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
sentence = input("ingrese frase: ")
letter = input("ingrese letra a buscar: ")
contLetter = 0
for i in sentence:
    if (
        i == letter
    ):  # i recorre toda la frase, si la i es igual a la letra que le decimos, el contador suma 1
        contLetter += 1
print(f"la letra {letter} se encuentra {contLetter} veces ")

# 13-Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    word = input("ingrese palabra: ")
    print(word)
    if word == "salir":
        break
print("salio")
# 14-Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.


# 15-Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
divisores = []
number = int(input("ingrese numero: "))
for num in range(1, number + 1):  # recorre del 1 hasta el numero ingresado
    if number % num == 0:  # se fija si la posicion en la que va es divisor del numero
        divisores.append(num)

print(f"los divisores de ese numero son {divisores}")
# 16-Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
quantity = int(input("ingrese cantidad de numeros: "))
nums = []
contNeg = 0
for i in range(1, quantity + 1):
    num = int(input(f"ingrese numero {i}:"))
    nums.append(num)
print(nums)
for n in nums:
    if n < 0:
        contNeg += 1
print(f"en total hay {contNeg} numeros negativos")

# 17-Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
vowels = set()  # set no permite elementos repetidos
sentence = input("ingrese frase: ")
for v in sentence:
    if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
        vowels.add(v)
print(f"las vocales en la oracion son {vowels}")

# 18-Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
num = 10
a = 0
b = 1
for i in range(1, num + 1):
    print(a, end=", ")
    a = b
    b = a + b
# 19-Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
objetivecash = int(input("ingrese la meta para ahorrar: "))
sum = 0
while True:
    cash = int(input("ingrese dinero que se va ahorrando: "))

    if cash > 0:
        sum = sum + cash

    if sum >= objetivecash:
        break
print(f"perfecto, se llego a la meta!! usted junto ${sum} pesos")

# 20-Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

sum = 0
while True:
    num = int(input("ingrese numeros, para finalizar introduzca 0: "))
    sum = sum + num
    if num == 0:
        break
print(f"la suma de los numeros es: {sum}")

# 21-Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
numM = 0
while True:
    num = int(input("ingrese un num, introduzca 0 para finalizar: "))
    if numM < num:
        numM = num

        if num == 0:
            break
print(f"el numero mayor es {numM}")


# 22-Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
def resultado(num):
    sumdigit = 0
    while num > 0:
        digit = num % 10  # averiguamos el ultimo digito del numero
        sumdigit += digit  # vamos sumando el digito a la suma
        num //= 10  # sacamos el ultimo digito dividiendo el numero *10 ej 123/10=12,3, hacemos esto haste que el numero sea 0.
    return sumdigit


numPeers = 0

while True:
    num = int(input("igrese num,ingrese -1 para finalizar: "))
    if num == -1:
        break
    else:
        resultSuma = resultado(num)
        print(f"la suma de los digitos del num {num} es: {resultSuma}")
        if num % 2 == 0:
            numPeers += 1

print("programa finalizado")
print(f"cantidad de numeros pares: {numPeers}")


# 23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

# 24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


sum = 0
npago = 0
while True:
    print(f"compra: {npago}")
    npago += 1
    pago = int(input(f"ingrese pago de la compra:  "))

    if pago == 0:
        break
    elif pago < 0:
        pago = int(input("pago negativo, por favor ingrese devuelta: "))
    else:
        sum += pago
    if sum > 1000:
        total = sum - (sum * 0.10)
    else:
        total = sum
print(f"el total a pagar es de: {total}")


# 25-Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
def facto(num):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num * (num - 1)


num = int(input("Ingrese un número para calcular su factorial: "))
resultado = facto(num)
print(f"El factorial de {num} es {resultado}")
