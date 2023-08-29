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


        
        



