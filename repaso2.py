
# 1. Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el
# programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un
# signo de interrogación al final. El programa mostrará después la frase final.
frase=input('ingrese frase: ')
if len(frase)==4:
    print(f'{frase}!')
else:
    print(f'{frase}?')    
# 2. Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra
# por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego.
import random
palabras=['paulo','hola','messi']
indiceA=random.randint(0,len(palabras)-1)  
palabrasA=palabras[indiceA]
palabrafinal=palabrasA
print(palabrasA)
intentos=0

while True:    
    letra=input('ingrese una letra: ')
    if letra in palabrasA:
        print('la letra esta en la palabra')
        
        for i in palabrasA:
            if letra==i:
                palabrasA=palabrasA.replace(i,' ')
        if len(palabrasA)==0:
            print(f'adivinaste la palabra {palabrafinal}')  
            break                      
    else:
        print('la letra no esta en la palabra')
        intentos+=1
        print(f'agostaste {intentos} intentos')

    if intentos>=5:
        print('alcanzaste el limite de intentos')
        break
#5 preguntas multiple opcion

# 3. Escribe un programa que cuente cuántas palabras hay en una cadena de texto ingresada por el usuario.
cadena=input('ingrese frase: ')
palabras=cadena.split(' ')
print(len(palabras))

# 4. Una empresa quiere pagar a sus empleados por la asistencia de lunes a viernes y un adicional por las
# horas trabajadas los domingos en tareas especiales.
# ✔ El empleado asistió todo el mes, además entre 3 y 5 horas los domingos, adiciona el 3 % del sueldo.
# ✔ Si asistió todo el mes y entre 6 y 10 horas los domingos, adiciona el 10 %.
# ✔ No asistió todo el mes y entre 3 y 10 horas los domingos, adiciona el 2 %.
sueldobase=int(input('cuanto es el sueldo base? '))
asis=input('asistio todo el mes?s/n ')
if asis.lower()=='s':
    horas=int(input('cuantas horas trabajo el domingo? '))
    if horas>=3 and horas<=5:
        extra=sueldobase*0.03
        sueldobase=sueldobase+extra
        print(f'el sueldo final es de {sueldobase}')
    elif horas>=6 and horas<=10:
        extra=sueldobase*0.10
        sueldobase=sueldobase+extra
        print(f'el sueldo final es de {sueldobase}')
elif asis.lower()=='n':
    horas=int(input('cuantas horas trabajo el domingo? '))
    if horas>=3 and horas<=10:
        extra=sueldobase*0.02
        sueldobase=sueldobase+extra
        print(f'el sueldo final es de {sueldobase}')
else:
    print('opcion incorrecta')


# 5. Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si
# no que los sume.
num1=int(input('ingrese num1: '))
num2=int(input('ingrese num2: '))
if num1==num2:
    multi=num1*num2
    print(f'la multiplicacion da {multi}')
elif num1>num2:
    resta=num1-num2
    print(f'el resultado de la resta es: {resta}')
else:
    suma=num1+num2
    print(f'el resultado de la suma es: {suma}')        
# 6. El ANSES requiere clasificar a las personas que se jubilaran en el año de 2010. Existen tres tipos de
# jubilaciones: por edad, por antigüedad joven y por antigüedad adulta.
# - Las personas adscritas a la jubilación por edad deben tener 60 años o más y una antigüedad en su
# empleo de menos de 25 años.
# - Las personas adscritas a la jubilación por antigüedad joven deben tener menos de 60 años y una
# antigüedad en su empleo de 25 años o más.
# - Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad
# en su empleo de 25 años o más.
# Determinar en qué tipo de jubilación, quedara adscrita una persona.
print('ANSES')
edad=int(input('ingrese edad: '))
antiguedad=int(input('ingrese antiguedad: '))
if edad>=60 and antiguedad<25:
    print('le toca la jubilacion por edad')
elif edad<60 and antiguedad>=25:
    print('le toco la jubilacion por antigiedad joven')
elif edad>60 and antiguedad>=25:
    print('le toco la jubilacion por antiguedad adulta')
else:
    print('no tiene jubilacion')

# 7. Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un
# porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la siguiente
# tabla:
# Tiempo Utilidad
# Menos de 1 año 5 % del salario
# 1 año o más y menos de 2 años 7% del salario
# 2 años o más y menos de 5 años 10% del salario
# 5 años o más y menos de 10 años 15% del salario
# 10 años o más 20% del salario
salario=int(input('ingrese salario: '))
antiguedad=int(input('ingrese antiguedad: '))
if antiguedad<1:
    extra=salario*0.05
    salario+=extra
    print(f'el salario final es {salario}')
elif antiguedad>=1 and antiguedad<2:
    extra=salario*0.07
    salario+=extra
    print(f'el salario final es {salario}')
elif antiguedad>=2 and antiguedad<5:
    extra=salario*0.10
    salario+=extra
    print(f'el salario final es {salario}')
elif antiguedad>=5 and antiguedad<10:
    extra=salario*0.15
    salario+=extra
    print(f'el salario final es {salario}')
elif antiguedad>10:
    extra=salario*0.20
    salario+=extra
    print(f'el salario final es {salario}')    