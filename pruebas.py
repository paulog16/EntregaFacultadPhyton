
def facto(num):
    if num<0:
        return 0
    elif num==0:
        return 1
    else:
        return num *(num-1)
    
num = int(input("Ingrese un número para calcular su factorial: "))
resultado = facto(num)
print(f"El factorial de {num} es {resultado}")    

      

        
         
      
  
    
