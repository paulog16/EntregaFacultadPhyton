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