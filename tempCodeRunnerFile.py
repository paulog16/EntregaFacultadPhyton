<<<<<<< HEAD
def res(matriz,num):
    contvic=0                    
    contderr=0                    
    contemp=0                    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i!=j: 
                if i==num:
                    if matriz[i][j]<matriz[j][i]:
                        
                        contderr+=1
                    elif matriz[i][j]>matriz[j][i]:
                           
                        contvic+=1  
                    else:
                        
                        contemp+=1
    listaestadisticas=[contvic,contderr,contemp]
    return listaestadisticas                    
matriz=[[0,4,2,1],
        [5,0,3,2],
        [0,2,0,1],
        [1,0,2,0]]

estadisticasequipo1=res(matriz,0)
print(f"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}")
estadisticasequipo2=res(matriz,1)
print(f"Equipo 2: Victorias={estadisticasequipo2[0]}, Derrotas={estadisticasequipo2[1]}, Empates={estadisticasequipo2[2]}")
estadisticasequipo3=res(matriz,2)
print(f"Equipo 3: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}")
estadisticasequipo3=res(matriz,3)
print(f"Equipo 4: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}")
=======
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
        pagar_cuotas(numero_socio,socios)
    elif opcion == "2":
        corregir_fecha_ingreso(socios)
    elif opcion == "3":
        nombre_apellido = input("Ingrese el nombre y apellido del socio a dar de baja: ")
        dar_de_baja(nombre_apellido,socios)
    elif opcion == "4":
        imprimir_listado_socios(socios)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
>>>>>>> aecd9f5cc4d5b94b7b247e2c52d2c877403136d1
