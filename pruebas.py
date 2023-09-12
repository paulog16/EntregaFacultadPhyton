x=0
while True:
   x+=1
   if x>=30:
    break
   if x==15:
    break
   if x==4 or x==6 or x==10:
    print(f'el numero{x} se saltea')
   else:
    print(x)
print(f'el bucle termino por que el valor de x es {x}') 
