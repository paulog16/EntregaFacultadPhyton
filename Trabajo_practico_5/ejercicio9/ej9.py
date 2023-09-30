import funciones9

intentos=3

while True:
    user=input('ingrese usuario: ')
    password=input('ingrese contraseña: ')
    if funciones9.login(user,password):
        print('felicitaciones, ingresaste')
        break
    else:
        intentos-=1 
    if intentos==3:
        print('has alcanzado el limite')
        break
           