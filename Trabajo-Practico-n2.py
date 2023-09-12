#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
years=int(input('ingrese cantidad de años de su pc: '))
if years>0:
    if years>2:
        print('su pc tiene mas de 2 años')
    else:
        print('su pc tiene menos de dos años')
             
#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
else:
    print('opcion incorrecta') 

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.
name1=input('ingrese primer nombre: ')
name2=input('ingrese segundo nombre: ')

if name1[0].lower()==name2[0].lower():
    print('la primer letra coincide')
else:
    print('la primer letra no coincide')    

#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
print('CANDIDATOS: A-PARTIDO ROJO, B-PARTIDO VERDE, C-PARTIDO AZUL')
op=input('INGRESE OPCION: ')
if op.upper()=='A':
    print('ELIGIO AL PARTIDO ROJO')
elif op.upper()=='B':
    print('ELIGIO AL PARTIDO VERDE')    
elif op.upper()=='C':
    print('ELIGIO AL PARTIDO AZUL')
else:
    print('OPCION INCORRECTA')    
#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
vocal=input('ingrese letra: ')
if(vocal.lower()=='a' or vocal.lower()=='e' or vocal.lower()=='i' or vocal.lower()=='o' or vocal.lower()=='u' ):
    print('es vocal')     
else:
    print('no es vocal o tiene mas de 1 caracter')

#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
year=int(input('ingrese año: '))
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('es bisiesto')
else:
    print('no es bisiesto') 

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
number1=int(input('ingrese numero 1: '))
number2=int(input('ingrese numero 2: '))
number3=int(input('ingrese numero 3: '))

if number1<number2 and number1<number3:
    print(f'el numero mas chico es: {number1}')
elif number2<number1 and number2<number3:
    print(f'el numero mas chico es: {number2}')
else:
    print(f'el numero mas chico es: {number3}')    
#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
user='Gwenevere'
password='excalibur'
usuario=input('ingrese usuario: ')
contrasenia=input('ingrese contraseña: ')
if (usuario==user and contrasenia==password):
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
name=input('ingrese nombre: ')
sex=input('ingrese sexo: ')  
if (sex.lower()=='mujer' and name[0].lower()<'m') and (sex.lower()=='hombre' and name[0].lower>'n'):
    print('forman parte del Grupo A')
else:
    print('perteneces al grupo B')    

#10-Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad=int(input('ingrese edad: '))
if edad>0:
    if edad<=4:
        print('entra gratis')
    elif edad>4 and edad<=18:
        print('usted paga 500')
    else:
        print('usted paga 1000')
else:
    print('edad incorrecta')                

#11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print('PIZZERIA BELLA NAPOLI')
print('OFRECEMOS MENU VEGETARIANO Y MENU NO VEGETARIANO')
print('DESEA COMPRAR UNA PIZZA?s/n')
op=input('')
if op.lower()=='s':
    print('PERFECTO, MENU VEGETARIANO O NO VEGETARIANO')
    op2=input('')
    if op2.lower()=='vegetariano':
        print('Ingredientes: Pimiento,Tofu, Que ingrediente desea?')
        opv=input('')
        print(f'Muchas gracias, aqui tiene su pizza vegetariana con {opv}')
    elif op2.lower()=='no vegetariano':
        print('ingredientes: peperoni,jamon,salmon')
        opnv=input('')
        print(f'Muchas gracias, aqui tine su pizza con {opnv}')
    else:
        print('no tenemos esa clase de pizza')        
else:
    print('no pasa nada, gracias por su visita')            
#12-Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
anioActual=int(input('igrese año actual: '))
anioCualquiera=int(input('ingrese año cualquiera'))
resto=abs(anioActual-anioCualquiera)
print(f'han pasado o falta para llegar: {resto} años') 



num=int(input('ingrese numero 1: '))
num2=int(input('ingrese numero 2: '))
nummayor=0
nummenor=0
if num>0 and num2>0:
    if num>num2:
        nummayor=num
        nummenor=num2
    elif num<num2:
        nummayor=num2
        nummenor=num
    if nummayor%nummenor==0:
        print('el numero mayor es multiplo del numero menor')
    else:
        print('no es multiplo')
else:
    print('es numero negativo o nulo')                    
#14-Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, #o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
#x = -b / a

a=float(input('ingrese a: '))
b=float(input('ingrese b: '))
print(f'ECUACION: {a} x + {b} = 0 ')
x=-b/a
print(f'el valor de X es: {x}')

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

print('QUE DESEA CALCULAR, AREA TRIANGULO(t) o AREA CIRCULO(c)')
op=input('')
if op.lower()=='t':
    base=float(input('ingrese base: '))
    altura=float(input('ingrese altura: '))
    area=0.5*base*altura
    print(f'el area del triangulo es: {area}')
elif op.lower()=='c':
    radio=float(input('ingrese radio del circulo: '))
    area=3.14*(radio**2)
    print(f'el area del circulo es: {area}')
else:
    print('opcion incorrecta')    

#16-	Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b

valor1=int(input('ingrese valor 1: '))
valor2=int(input('ingrese valor 2: '))
op=input('que operacion desea realizar: 1(suma),2(mul),3(resta),4(div): ')
if op.lower()=='1':
    print(f'el resultado es: {valor1 + valor2}')
elif op.lower()=='2':    
    print(f'el resultado es: {valor1 * valor2}')
elif op.lower()=='3':
    print(f'el resultado es: {valor1 - valor2}')
elif op.lower()=='4':
    print(f'el resultado es: {valor1 / valor2}')
else:
    print('opcion incorrecta')    

#17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia=input('ingrese dia de la semana: ')
if dia.lower()=='lunes':
    print('es lunes')
elif dia.lower()=='viernes':
    print('es viernes')
elif dia.lower()=='sabado' or dia=='domingo':
    print('es finde')
else:
    print('no es ni lunes,viernes,sabado o domingo')      

#18-Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
      
ht=int(input('ingrese horas trabajadas: '))
ph=float(input('ingrese pago por hora: '))
pago=ht*ph
total=0
if ht>48:
    he=ht-48
    pghe=(he*ph)*0.10
    total=pago+pghe
    print(f'usted trabajo horas extras, tiene que cobrar {total}')
else:
    total+=pago
    print(f'usted tiene que cobrar {total}')
#19-Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
cant=int(input('cuantos lapices desea comprar: '))
if cant>0:
    if cant>=1000:
        descuento=(cant*60)*0.07
        total=(cant*60)-descuento
        print(f'usted tiene que pagar {total}')
    else:
        total=cant*60
        print(f'usted tiene que pagar {total}')
else:
    print('no se puede ingresar numero negativos')            
#20-Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
nota1=float(input('ingrese nota1:'))
nota2=float(input('ingrese nota2: '))
nota3=float(input('ingrese nota3: '))
nota4=float(input('ingrese nota4: '))
prom=(nota1+nota2+nota3+nota4)/4
if prom<60:
    print('desaprobado')
else:
    print('aprobado')







   