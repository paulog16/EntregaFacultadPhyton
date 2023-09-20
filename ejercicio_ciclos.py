arregloM=[]
numCorrer=int(input('cuantos lugares quieres correr: '))
for i in range(1,6):
     mensaje=input(f'ingrese el mensaje al ofical{i}: ')
     arregloM.append(mensaje)

print(arregloM)
abecedario='abcdefghijklmnopqrstuvwxyz'
arregloPalabras=[]
for p in arregloM:
     msj_enc = ''
     for letra in p:
         if letra in abecedario:
             ind=abecedario.find(letra)
             ind = (ind+numCorrer)%26
             msj_enc += abecedario[ind]
         else:
               msj_enc+=letra
     arregloPalabras.append(msj_enc)
print(arregloPalabras)

# punto2
"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
contparesT=0
contimparesT=0
while True:
    n=int(input('ingrese numeros positivos, ingrese 0 para finalizar: '))
    if n==0:
        break
    contpares=0
    contimpares=0
    for i in str(n):
        if int(i)%2==0:
            contpares+=1
            contparesT+=1
        else:
            contimpares+=1
            contimparesT+=1
    print(f'el numero tiene {contpares} numeros pares y {contimpares} numeros impares')
print(f'numeros pares totales: {contparesT}')    
print(f'numeros impares totales: {contimparesT}') 
