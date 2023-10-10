
"""1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse."""
list_number=[]
while True:
    num=int(input('ingrese numeros, ingrese 0 para finalizar:\n'))
    if num!=0:
        list_number.append(num)
    if num==0:
        break
print(list_number)
"""2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar."""
number=int(input('ingrese numero que quiera eliminar:\n'))
if number in list_number:
    list_number.remove(number)
else:
    print('no hay coincidencias')                
print(list_number)
#3.	Imprimir la sumatoria de todos los números de la lista.
suma=0
for i in list_number:
    suma+=i
print(f'la suma es: {suma}')    
#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
other_number=int(input('ingrese un numero: '))
other_lista=[]
for i in list_number:
    if i<other_number:
        other_lista.append(i)
for i in other_lista:
    print(i)
#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]
listanueva=[]
tupla=()
for i in list_number:
    cont=0
    for k in list_number:
        if i ==k:
            cont+=1
            tupla=(i,cont)
    listanueva.append(tupla)   

listaset=set(listanueva)            
print(listaset)
    
#6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.



listanombresPrimaria=[]
listanombresSecundaria=[]
while True:
    nombresp=input('ingrese nombres de primaria, para finalizar ingrese X:\n')
    if nombresp!='x':
        listanombresPrimaria.append(nombresp)
    if nombresp=='x':
        break
while True:
    nombress=input('ingrese nombres de secundaria, para finalizar ingrese X:\n')
    if nombress!='x':
        listanombresSecundaria.append(nombress)
    if nombress=='x':
        break
#a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.    
todoslosnombres=listanombresPrimaria+listanombresSecundaria
nombressinrepetir=set(todoslosnombres)
print(nombressinrepetir)

#b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
nombresrepetidos=[]
nombresnorepetidos=[]
for i in listanombresPrimaria:
    for k in listanombresSecundaria:
        if i==k:
            nombresrepetidos.append(i)
        #c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
        if i not in listanombresSecundaria:
            nombresnorepetidos.append(i)
nombresrepetidos=set(nombresrepetidos)
nombresnorepetidos=set(nombresnorepetidos)
print(nombresrepetidos)
print(nombresnorepetidos)
#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
#‘r’:5
#‘%’:3
#‘a’:8
#‘9’:1

listastr=[]
contt=0
while True:
    string=input('ingrese una string: \n')
    listastr.append(string)
    contt+=1
    if contt==50:
        break
listanuevastr=[]
tuplastr=()
for i in listastr:
    cont=0
    for k in listastr:
        if i ==k:
            cont+=1
            tuplastr=(i,cont)
    listanuevastr.append(tuplastr)   

listaset=set(listanuevastr)            
print(listaset)

#8 trabajo de los equipos de futbol
def res(matriz, num):
    contvic = 0
    contderr = 0
    contemp = 0
    conpuntos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                if i == num:
                    if matriz[i][j] < matriz[j][i]:
                        contderr += 1
                    elif matriz[i][j] > matriz[j][i]:
                        contvic += 1
                        conpuntos += 3
                    else:
                        conpuntos += 1
                        contemp += 1
    listaestadisticas = [contvic, contderr, contemp, conpuntos]
    return listaestadisticas


def dif(matriz, num):
    sum = 0
    golesrecibidos = 0
    cont = 0
    for i in matriz[num]:
        sum += i
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i != j:
                    if cont == 3:
                        break
                    if i == num:
                        golesrecibidos += matriz[j][i]

                        cont += 1
    res = sum - golesrecibidos

    return f"equipo{num+1} la diferencia es : {res} "


matriz = [[0, 4, 2, 1], [5, 0, 3, 2], [0, 2, 0, 1], [1, 0, 2, 0]]

estadisticasequipo1 = res(matriz, 0)
print(
    f"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}, puntosTotales= {estadisticasequipo1[3]}"
)
dif1 = dif(matriz, 0)
print(dif1)


estadisticasequipo2 = res(matriz, 1)
print(
    f"Equipo 2: Victorias={estadisticasequipo2[0]}, Derrotas={estadisticasequipo2[1]}, Empates={estadisticasequipo2[2]},  puntosTotales= {estadisticasequipo2[3]}"
)
dif2 = dif(matriz, 1)
print(dif2)

estadisticasequipo3 = res(matriz, 2)
print(
    f"Equipo 3: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}, puntosTotales= {estadisticasequipo3[3]}"
)
dif3 = dif(matriz, 2)
print(dif3)

estadisticasequipo4 = res(matriz, 3)
print(
    f"Equipo 4: Victorias={estadisticasequipo4[0]}, Derrotas={estadisticasequipo4[1]}, Empates={estadisticasequipo4[2]}, puntosTotales= {estadisticasequipo4[3]}"
)
dif4 = dif(matriz, 3)
print(dif4)