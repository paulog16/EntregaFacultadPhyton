'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
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



import funciones

listapasajeros=[]    
listaciudades=[]

while True:

    print('''OPCIONES:
    1:agregar pasajeros
    2:agregar ciudades
    3:Dado el DNI de un pasajero, ver a qué ciudad viaja.
    4:Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
    5:Dado el DNI de un pasajero, ver a qué país viaja.
    6:Dado un país, mostrar cuántos pasajeros viajan a ese país.
    7:Salir del programa''')

    op=int(input(''))
    if op==1:
        funciones.llenarPasajeros(listapasajeros)
    elif op==2:
        funciones.llenarciduades(listaciudades)
    elif op==3:
        funciones.buscar_ciudad_por_dni(listapasajeros)
    elif op==4:
        funcones.cant_pasajeros_ciudad(listapasajeros)
    elif op==5 or op==6:
        print('no entiendo estas opciones, ya que nunca indicamos pais al que viaja, indicamos solamente ciudad')
    elif op==7:
        break    


'''
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
contenga cada domicilio una sola vez.
'''


import funciones
lista=[]
sett=set()

while True:
    op=input('1: agregar facturas, 2: mostrar domicilios, 3: salir ')
    if op=='1':
        funciones.agregarcompras(lista)
    elif op=='2':
        funciones.mostrardirecciones(lista,sett)
    if op=='3':
        break
    

'''Crear un programa para gestionar datos de los socios de un club, permitiendo:
- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar
son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar
con los datos de los socios fundadores ya cargados:
o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad
ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
- Imprimir el listado de socios completo.'''
import funciones
socios = {
    1: {"nombre": "Paulo guidolin", "fecha_ingreso": "27/03/2019", "cuota_al_dia": True},
    2: {"nombre": "lucas Molina", "fecha_ingreso": "15/05/2018", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "fecha_ingreso": "13/03/2018", "cuota_al_dia": True}
}


while True:
    print("\nOpciones:")
    print("1. Pagar cuotas")
    print("2. Corregir fecha de ingreso")
    print("3. Dar de baja a un socio")
    print("4. Imprimir listado de socios")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        numero_socio = int(input("Ingrese el número de socio que pagó las cuotas: "))
        funciones.pagar_cuotas(numero_socio,socios)
    elif opcion == "2":
        funciones.corregir_fecha_ingreso(socios)
    elif opcion == "3":
        nombre_apellido = input("Ingrese el nombre y apellido del socio a dar de baja: ")
        funciones.dar_de_baja(nombre_apellido,socios)
    elif opcion == "4":
        funciones.imprimir_listado_socios(socios)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

