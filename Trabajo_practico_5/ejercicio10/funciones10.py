def carrito(a,b):
    precio_final=0
    for product,precio in a.items(): #recorro clave-valor
        if product in b: #si clave esta en b(descuentos) 
            descuento=precio*(b[product]/100)
            #creo variable descuento que es el porcentaje
            precio-=descuento
            precio_final+=precio
    return precio_final