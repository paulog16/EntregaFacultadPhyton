kc1=float(input('cuantos kilometros puedes recorrer con un litro de combustible'))
capacidad=int(input('que capacidad tiene el tanque '))
kilometros=int(input('cuantos kilometros recorreran'))
tanquesN=(kilometros/kc1)/capacidad
print(f'tanques necesarios para el viaje: {tanquesN}')