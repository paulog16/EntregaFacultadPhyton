def ahorcado(palabra,intentos):
    spaces = ["_"] * len(palabra)
    while True:
        letra = input('Ingrese una letra: ')
        for i, character in enumerate(palabra):
            if letra == character:
                spaces[i] = letra
                print(" ".join(spaces))
        if letra not in palabra:
            print('la letra no esta en la palabra!')
            intentos-=1    
        if intentos==0:
            print('se te acabaron los intentos, perdiste')
            break
        if "_" not in spaces:
            print('¡Ganaste!')
            break

    print(f'La palabra era: {palabra}')