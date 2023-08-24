#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
anios=int(input('ingrese cantidad de años de su pc: '))
if(anios<=2):
    print('su pc es menor o igual a 2 años')
elif (anios>2):
    print('su pc es mayor a 2 años')  
#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
elif(anios<0):
    print('no puede ingresar numeros negativos')

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.
nombre1=input('ingrese nombre1: ')
nombre2=input('ingrese nombre2: ')
if (nombre1[0]==nombre2[0]):
    print('coincidencia')
else:
    print('no coincidencia')

#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
elegido=input('ingrese candidato a cual votar, A.B.C').lower
if (elegido=='a'):
    print('eligio al partido rojo')
elif(elegido=='b'): 
    print('eligio al partido verde')
elif(elegido=='c'):
    print('eligio al partido azul')
else:
    print('partido inexistente') 

#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
vocal=input('ingrese letra: ')
if(vocal=='a' or vocal=='e' or vocal=='i' or vocal=='u' ):
    print('es vocal')     
elif(len(vocal)>1):
    print('no se puede ingresar mas de un caracter')
else:
    print('no es vocal')

#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
anio=int(input('ingrese año: '))
if(anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print('es bisiesto')
else:
    print('no es bisiesto') 

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
num1=int(input('ingrese num1'))
num2=int(input('ingrese num2'))
num3=int(input('ingrese num3'))
if(num1<num2 and num1<num3):
    print(f'el numero mas chico es {num1}')
elif(num2<num1 and num2<num3):
    print(f'el numero mas chico es {num2}')
else:
    print(f'el numero mas chico es {num3}')

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
user='Paulo'
password='Godoycruz'
usuario=input('ingrese usuario: ')
contrasenia=input('ingrese contraseña')
if (usuario==user and contrasenia==password):
    print('acceso habilitado')
else:
    print('acceso denegado')

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre=input('ingrese su nombre: ')
sexo=input('ingrese sexo H,M: ')        
if(sexo=='M' and nombre[0]<'M') or (sexo=='H' and nombre[0]>'N'):
    print('corresponde al grupo A')
else:
    print('corresponde al grupo b')    

#10-Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad=int(input('ingrese edad: '))
if edad<4:
    print('entra gratis')
elif edad>=4 and edad <=18:
    print('debe pagar $500')
else:
    print('debe pagar $1000')

#11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipopizza=input('desea una pizza vegetariana o no?')
if tipopizza=='si':
    print('INGREDIENTES:PIMIENTO,TOFU ')
    ing=input('ingrese el ingrediente que desea: ')
    print(f'usted eligio una pizza vegana con {ing}')  
else:
    print('INGREDIENTES:PEPERONI,JAMON,SALOMON ')
    ing=input('ingrese el ingrediente que desea: ')
    print(f'usted eligio una pizza no vegetariana con {ing}')
            
#12-Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
anioActual=int(input('igrese año actual: '))
anioCualquiera=int(input('ingrese año cualquiera'))
resto=abs(anioActual-anioCualquiera)
print(f'han pasado o falta para llegar: {resto} años') 

#13-Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1=int(input('ingrese num1: '))
num2=int(input('ingrese num2: '))

if num1<0 and num2<0:
    print('los numeros son negativos')
else:
    if num1>num2:
        if (num1 % num2)==0:
            print(f'el numero {num1} es multiplo de {num2}')
        else:
            print(f'el numero {num1} no es multiplo de {num2}')
    else:
         if (num2 % num1)==0:
            print(f'el numero {num2} es multiplo de {num1}')
         else:
            print(f'el numero {num2} no es multiplo de {num1}')     

#14-Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, #o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
#x = -b / a

b=int(input('ingrese valor de b: '))
a=int(input('ingrese valor de a: '))
print(f'{a}x + {b} = 0 ')
x= -b/a
print(f'el valor de x es: {x}')

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

op=input('que desea calcular? triangulo(t) o circulo(c): ')
if op=='t':
    base=float(input('ingrese base'))
    altura=float(input('ingrese altura'))
    area= 1/2 * base * altura
    print(f'el area del triangulo es: {area}')








   