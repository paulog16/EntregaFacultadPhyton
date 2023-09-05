'''Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se
dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.'''

dia_dd_mm=input('dia, dd/mm')
diaS=dia_dd_mm[0:dia_dd_mm.find(',')].lower()
dd=dia_dd_mm[dia_dd_mm.find(' ')+1:dia_dd_mm.find('/')]
mm=dia_dd_mm[dia_dd_mm.find('/')+1:]

print(f'{diaS}/{dd}/{mm}')


if(diaS=='lunes' or diaS=='martes' or diaS=='miercoles' or diaS=='jueves' or diaS=='viernes' or 
   diaS=='sabado' or diaS=='domingo' ) and (int(dd)>0 and int(dd)<=31) and (int(mm)>0 and int(mm)<=12):
   print('la fecha es valida') 
   if(diaS=='lunes' ):
    print('Clases nivel inicial')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))    
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')
    
elif(diaS=='martes'):
    print('Clases nivel intermedio')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))   
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')
    
elif(diaS=='miercoles'):
    print('Clases nivel avanzado')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')

elif(diaS=='jueves'):
    print('dia de practica hablada no se dicta ningun examen')
    porc=float(input('ingrese porcentaje a clases: '))
    if(porc>=50):
        print('aisitio a la mayoria de las clases')
    else:
         print('no asistio a la mayoria de la clase')

    
elif(diaS=='viernes') and  ((int(dd)==1 and int(mm)==1) or (int(dd)==1 and int(mm)==7)) :

    print('Comienzo de nuevo ciclo')
    alum_nuevo_ciclo=int(input('ingrese cantidad de alumnos del nuevo ciclo: '))
    cuota=float(input('ingrese valor cuota: '))
    total=alum_nuevo_ciclo*cuota
    print(f'el total que recibe el colegio es: {total}$')
    
    # print('Dia de ingles extranjero no se dictan examenes')
else:
    print('la fecha es invalida')

