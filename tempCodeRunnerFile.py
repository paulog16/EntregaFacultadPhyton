def res(matriz,num):
    contvic=0                    
    contderr=0                    
    contemp=0  
    conpuntos=0                  
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i!=j: 
                if i==num:
                    if matriz[i][j]<matriz[j][i]:
                        
                        contderr+=1
                    elif matriz[i][j]>matriz[j][i]:
                        contvic+=1  
                        conpuntos+=3
                    else:
                        conpuntos+=1
                        contemp+=1
    listaestadisticas=[contvic,contderr,contemp,conpuntos]
    return listaestadisticas
                    
def dif(matriz,num):
    sum=0
    golesrecibidos=0
    cont=0
    for i in matriz[num]:    
        sum+=i
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i!=j:
                    if cont==3:
                        break 
                    if i==num:
                        print(matriz[j][i])
                        golesrecibidos+=matriz[j][i]
                        print(golesrecibidos)
                        
                        cont+=1
    res=sum-golesrecibidos                    
    print(sum,golesrecibidos)
    print(f'equipo{num+1} la diferencia es : {res} ')                   
                          
                        

matriz=[[0,4,2,1],
        [5,0,3,2],
        [0,2,0,1],
        [1,0,2,0]]

estadisticasequipo1=res(matriz,0)
print(f"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}, puntosTotales= {estadisticasequipo1[3]}")
dif(matriz,0)