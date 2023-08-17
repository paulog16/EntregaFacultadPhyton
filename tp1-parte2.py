#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.*
import math


base=float(input('ingrese base: '))
altura=float(input('ingrese altura: '))
perimetro=(base*2)+(altura*2)
area=base*altura
print(f'area: {area}, perimetro: {perimetro}')
#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
print(f"La hipotenusa del triángulo rectángulo es: {hipotenusa}")
#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
num1=5
num2=7
print(f'suma: {num1+num2}, resta: {num1-num2}, multiplicacion: {num1*num2}, division: {num1/num2}')
#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
f=float(input('ingrese grados f'))
c=(f-32)*5/9
print(f'grados celcius: {c}')
#5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
nombre='paulo'
a=input(f'{nombre}, ¿cual es tu cancion favorita?')
#b)	precio = input(“Precio: “)
#total = precio + (precio * 0.1)
precio=float(input('precio: '))
#c)	edad = int(input(“Edad: “))
#print(tu edad es, edad)
print(f'tu edad es, {edad}')

#d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)
print(f'veamos si tu edad es 18... {edad==18}')

#6.	Calcular la media de tres números pedidos por teclado.
num1=float(input('ingrese num1'))
num2=float(input('ingrese num2'))
num3=float(input('ingrese num3'))
media=(num1+num2+num3)/3
#7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minu=1000
horas=minu//60
minRes=minu%60
print(f'{minu}, minutos es {horas} horas y {minRes} minutos')
#8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza 
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base=float(input('ingrese sueldo base'))
venta1=250
venta2=500
venta3=200
sueldo_total=sueldo_base+((venta1*0.10)+(venta2*0.10)+(venta3*0.10))
#9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
precioP=2000
descuento=precioP*0.15
precioF=precioP-descuento
#10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.

nota1=7
nota2=9
nota3=10
promedio=(nota1+nota2+nota3)/3
examenfinal=8
trabajofinal=7
calificacionFinal=(promedio*0.55)+(examenfinal*0.30)+(trabajofinal*0.15)
#11.Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)
num1=float(input('ingrese num1 y num2: '))
num2=float(input())
abso=abs(num1-num2)
print(f'la distancia absoluta que hay es de {abso}')
#12.Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
num=9
raizC=math.sqrt(num)
raizCu=num**(1/3)
#13.Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
num=32
unidades=num%10
decena=num//10
invertido=unidades*10+decena
print(invertido)
#14.Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
a=5
b=7


c=a #c=5
a=b #a=7
b=c #b=5
print(a)
print(b)
#15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
horaSalida=float(input('indique hora de salida: '))
minutosSalida=float(input('indique minuto de salida: '))
segundosSalida=float(input('indique segundos de salida: '))
tsegundos=float(input('indique los segundos totales que se demoro para llegar: '))
horaLlegada=tsegundos//3600
minutosLlegada=(tsegundos%3600)//60
segundosLlegada=tsegundos%60
print(f'el ciclista llego a las {horaLlegada+horaSalida} hs, {minutosLlegada+minutosSalida} min y {segundosLlegada+segundosSalida} seg')
#16.Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre=input('ingrese nombre: ')
apellido1=input('ingrese apellido1: ')
apellido2=input('ingrese apellido2: ')
print(f'primer letra del nombre: {nombre[0]}, primer letra del apellido1: {apellido1[0]}, primer letra del apellido2: {apellido2[0]}')
#17.Solicitar al usuario que ingrese su nombre.
#  El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario=input('ingrese su nombre: ')
print(f'Ahora estás en la matrix {usuario}')
#18.Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante.
#  A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.
cena=int(input('cuanto costo la cena? '))
preciototal=cena+(cena*0.6)+(cena*0.10)
print(f'el monto total a pagar es: {preciototal}')
#19.Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica 
# (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.
dia=int(input('ingrese dia '))
mes=int(input('ingrese mes '))
anio=int(input('ingrese año '))
print(f'{dia}/{mes}/{anio}')
#20:Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
from datetime import datetime
fecha_str = "16022003"
fecha_obj = datetime.strptime(fecha_str,"%d%m%Y")
print(fecha_obj)
#21.Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, 
# para saber cuántos tanques de combustible consumirá el viaje entero.
#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible,
#qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.
kc1=float(input('cuantos kilometros puedes recorrer con un litro de combustible: '))
capacidad=int(input('que capacidad tiene el tanque: '))
kilometros=int(input('cuantos kilometros recorreran: '))
tanquesN=(kilometros/kc1)/capacidad
print(f'tanques necesarios para el viaje: {tanquesN}')

#INTEGRANTES: PAULO GUIDOLIN,SANTIAGO OJEDA,SEBASTIAN ASTUDILLO
 