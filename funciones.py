
def ahorcado(palabra,intentos,letrasI):
    spaces = ["_"] * len(palabra)
    while True:
        letra = input('Ingrese una letra: ')
        letrasI.append(letra)
        print(f'letras ingresadas: {letrasI}')
        for i, character in enumerate(palabra):
            if letra == character:
                spaces[i] = letra
                print(" ".join(spaces))
        if letra not in palabra:
            print('la letra no esta en la palabra!')
            intentos-=1    
        if intentos==0:
            print('se te acabaron los intentos, perdiste')
            break
        if "_" not in spaces:
            print('¡Ganaste!')
            break

    print(f'La palabra era: {palabra}')


def llenarPasajeros(lista):
    nombre=input('ingrese nombre: ')
    while True:
        dni=input('ingrese dni: ')
        if len(dni)==7 or len(dni)==8:
            break
        else:
            print('ingrese devuelta')
    destino=input('ingrese destino al que quiere ir: ')
    pasajero=(nombre,dni,destino)
    lista.append(pasajero)

def llenarciduades(lista):
    provincia=input('ingrese provincia: ')
    pais=input('ingrese pais: ')
    lista.append(provincia,pais) 

def buscar_ciudad_por_dni(listaV):
    dni = input("Ingrese el DNI del pasajero: ")
    for i in listaV:
        if i[1]==dni:
            print(f'{i[0]} viaja a {i[2]}')
        else:
             print("No se encontró un pasajero con ese DNI o no se ha registrado su destino.")           



def cant_pasajeros_ciudad(listaV):
    cont=0
    ciudad=input('ingrese una ciudad: ')
    for i in listaV:
        if i[2]==ciudad:
          cont+=1                      
    print(f'a esa ciudad van {cont} personas')



def agregarcompras(lista):
    cliente=input('ingrese nombre del cliente: ')
    dia_mes=input('ingrese dia del mes: ')
    monto=input('ingrese monto: ')
    domicilio=input('ingrese domicilio del cliente: ')
    tupla=(cliente,dia_mes,monto,domicilio)
    lista.append(tupla)

def mostrardirecciones(lista,sett):
    for i in lista:
        sett.add(i[3])
    print(sett)


def pagar_cuotas(numero_socio,socios):
    if numero_socio in socios:
        socios[numero_socio]['cuota_al_dia']=True
        print(f"El socio n°{numero_socio} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"No se encontró al socio n°{numero_socio}.") 

def corregir_fecha_ingreso(socios):
    for i,k in socios.items():
        if k['fecha_ingreso']=='13/03/2018':
            k['fecha_ingreso']='14/03/2018'

def dar_de_baja(nombre_apellido,lista):
    for i,datos in lista.items():
        if datos['nombre']==nombre_apellido:
            del lista[i]
        else:
            print('no se encontro el socio')

def imprimir_listado_socios(socios):
    print("Listado de socios:")
    for numero, datos in socios.items():
        if datos['cuota_al_dia']:
            cuota_estado='al dia'
        else:
            cuota_estado='adeudada'    
        print(f"Socio n°{numero}: {datos['nombre']}, Ingreso: {datos['fecha_ingreso']}, Cuota: {cuota_estado}")    