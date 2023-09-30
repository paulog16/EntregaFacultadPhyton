import funciones3

socios=[]
cant_socios=int(input('ingrese cantidad de socios: '))
for i in range(1,cant_socios+1):
    print(f'ingrese nombre del socio {i}')
    nombre=input('')
    while True:
        print(f'ingrese dni del socio {i}')
        dni=input('') 
        if len(dni)==7 or len(dni)==8:
            break 

    socios.append(funciones3.id_unico(nombre,dni))
print('los id de los usuarios son: ')
print(socios)            