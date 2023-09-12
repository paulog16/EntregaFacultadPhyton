<<<<<<< HEAD
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
=======
nums=[2,3,4,5,2,1,4,8,9]
numE=int(input('what search a number: '))
for i in nums:
    if nums[i]==numE:
        break
    print(i)
print(f'la lista salio en el numero: {numE} y era la posicion {i}')
>>>>>>> 536e5d9119d180ac32dbe52ff95d19363ef142a7
