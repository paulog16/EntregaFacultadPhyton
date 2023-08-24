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



   