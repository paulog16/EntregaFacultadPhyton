'''Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Por ejemplo:
*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.
'''
def validar_dni(dni):
    if len(str(dni))==8 or len(str(dni))==7:
        return True
    else:
        return False

def agregarPasajeros(lista_pasajero):
    nombre=input("Ingrese su nombre")
    while True:
        dni=int(input("Ingrese su dni"))
        if validar_dni(dni):
            break
        else:
            print("Ingrese un dni valido")
    destino=input("Ingrese su destino")
    pasajero=(nombre,dni,destino)
    lista_pasajero.append(pasajero)
    print(f"{nombre} ya fue registrado en el viaje ")

def origen (lista_origen):
    city=input("Ingrese su ciudad de origen")
    country=input("Ingrese el país de origen")
    lista_1=(city,country)
    lista_origen.append(lista_1)
    print(lista_origen)


lista_origen=[]   
lista_pasajero=[]
while True:
    decision=input("Desea ingresar un pasajero? (SI/NO) ")
    if decision.lower()=="si":
        agregarPasajeros(lista_pasajero)
    elif decision.lower()=="no":
        break
    decision1=input("Desea ingrsar alguna ciudad? (SI/NO) ")
    if decision.lower()=="si":
        origen(lista_origen)
    elif decision1.lower()=="no":
        break
    #p
