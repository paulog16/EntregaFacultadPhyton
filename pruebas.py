<<<<<<< HEAD
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
=======
total = 0
while True:
    inp = input("")
    if inp == "":
        break
    operation, mont = inp.split()  # separa la frase en cadenas separadas
    mont = int(mont)

    if operation.upper() == "D":
        total += mont
    elif operation.upper() == "R":
        total -= mont
print(f"el monto total es: {total}")
>>>>>>> 536e5d9119d180ac32dbe52ff95d19363ef142a7
