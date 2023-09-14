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