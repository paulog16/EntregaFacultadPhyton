'''ejercicio para llegar a monto x de un negocio'''

monto=float((input('ingrese al monto que quiere llegar al negocio: ')))
suma=0

while True:
    print(f'la cuenta actualmente tiene: {suma} pesos')
    if suma>=monto:
        break
    print('Ingrese s  para agregar dinero a la cuenta')
    print('Ingrese r  para restar dinero a la cuenta')
    print('ingrese salir para salir' )
    
    op=input('')
    if op.lower()=='salir':
        break
    elif op.lower()=='s':
        op1=float(input('cuantos productos vendio? '))
        for i in range(1,op1+1):
            pro=float(input(f'ingrese venta del producto {i}: '))
            suma+=pro         
    elif op.lower()=='r':
        op2=float(input('cuanto productos compro? '))
        for i in range(1,op2+1):
            ven=float(input(f'ingrese cuanto gasto en el producto {i}: '))
            suma-=ven
print(f'se llego a la cantidad: {monto}')

'''parcial{
    5 puntos teoria

}'''