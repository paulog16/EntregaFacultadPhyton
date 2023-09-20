'''ejercicio para llegar a monto x de un negocio'''
#declaro el monto al que quiero llegar
monto=float((input('ingrese al monto que quiere llegar al negocio: ')))
#inicializo una variable suma en 0
suma=0
print('SISTEMA DE CONTROL DE VENTAS DE UN NEGOCIO')
while True:
    #muestro el estado de la cuenta actualmente
    print(f'la cuenta actualmente tiene: {suma} pesos')
    #si la suma es igual o superior al monto, sale del programa
    if suma>=monto:
        break
    print('Ingrese s  para agregar dinero a la cuenta')
    print('Ingrese r  para restar dinero a la cuenta')
    print('ingrese salir para salir' )
    #ingreso opcion
    op=input('')
    #si la opcion es 'salir' salgo del programa
    if op.lower()=='salir':
        break
    #si la opcion es 's', pregunto cuantos productos vendio
    elif op.lower()=='s':
        op1=float(input('cuantos productos vendio? '))#pregunto cuantos productos vendio
        #hago un for para añadir el precio de los productos
        for i in range(1,op1+1):
            pro=float(input(f'ingrese venta del producto {i}: ')) #declaro el precio de venta
            suma+=pro        #sumo cada venta a la suma 
    #si la opcion es 'r', pregunto cuantos productos compro        
    elif op.lower()=='r':
        op2=float(input('cuanto productos compro? ')) #declaro cuantos productos compro para vender
        for i in range(1,op2+1):
            ven=float(input(f'ingrese cuanto gasto en el producto {i}: '))#indico precio de compra
            suma-=ven #se lo resto a la suma
print(f'se llego a la cantidad: {suma}') #salgo del while y muestro a cuanto se llego

'''parcial{
    5 puntos teoria

}'''