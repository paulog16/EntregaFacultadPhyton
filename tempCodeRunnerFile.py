tipopizza=input('desea una pizza vegetariana o no?')
if tipopizza=='si':
    print('INGREDIENTES:PIMIENTO,TOFU ')
    ing=input('ingrese el ingrediente que desea: ')
    print(f'usted eligio una pizza vegana con {ing}')  
else:
    print('INGREDIENTES:PEPERONI,JAMON,SALOMON ')
    ing=input('ingrese el ingrediente que desea: ')
    print(f'usted eligio una pizza no vegetariana con {ing}')