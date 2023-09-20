<<<<<<< HEAD

import funciones.py
import random
palabras=[
    'messi',
    'ronaldo',
    'neymar'
]
intentos=5
palabraA=random.choice(palabras)
funciones.ahorcado(palabraA,intentos)
=======
<<<<<<< HEAD
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
else:
    horas=int(input('cuantas horas trabajo el domingo? '))
    if horas>=3 and horas<=10:
        extra=sueldobase*0.02
        sueldobase=sueldobase+extra
        print(f'el sueldo final es de {sueldobase}')
=======
<<<<<<< HEAD
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
=======
nums=[2,3,4,5,2,1,4,8,9]
numE=int(input('what search a number: '))
for i in nums:
    if nums[i]==numE:
        break
    print(i)
print(f'la lista salio en el numero: {numE} y era la posicion {i}')
>>>>>>> 536e5d9119d180ac32dbe52ff95d19363ef142a7
>>>>>>> 8f02c9fb9711b761b973540510ac6dcb6e464937
>>>>>>> 06067a17751fd8bac3288d4bfd3f652e919e3e9c
