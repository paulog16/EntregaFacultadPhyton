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
