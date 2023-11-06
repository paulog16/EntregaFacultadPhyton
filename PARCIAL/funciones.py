def llenar_matriz(adn): #declaro funcion para llenar la matriz manuelmente
    for i in range(6): #hago un for para que se ejecute 6 veces lo de a continuacion:
        sequence_valid = True # declaro una secuencia valida para ir viendo si lo que ingresamos es valido
        while True:
            sequence = input('Ingrese secuencia de letras: ')
            if len(sequence) == 6: #si la secuencia es de 6 caracteres
                for letra in sequence: # recorremos cada caracter de la secuencia ingresada
                    if letra.upper() not in 'ATGC': # si la 'letra' no se encuentra en ninguna de las mencionadas, la secuencia es falsa
                        sequence_valid = False #la asignamos como falsa  
                        print('Secuencia no válida')
                if sequence_valid: #cuando sea verdadera
                    adn.append(sequence.upper())  #agregamos la secuencia a la matriz llamada adn
                    break
            else: #si la lonigtud de la secuencia no es 6, mostramos este mensaje
                print('Longitud de secuencia incorrecta. Debe ser de longitud 6.')  
                            
                        



def is_mutant(adn): #creo la funcion "is_mutant"
    mutant=False #declaro la variable mutant para ir viendo si es mutante o no 

    def buscarElementosJuntos(cadena): #hago esta funcion me permite saber si la secuencia 'AAAA','CCCC',etc se encuentra en la lista que le paso por parametro, si es asi, la funcion retorna True
        secuencia=''.join(cadena) #esto convertira la cadena en una secuencia unida
        if ('AAAA' in secuencia) or ('TTTT' in secuencia) or ('CCCC' in secuencia) or ('GGGG' in secuencia): 
           return True

   
    for row in adn: #recorro las filas de adn, si se cumple la funcion "buscarelementosJuntos" es mutante
        if buscarElementosJuntos(row): 
            mutant=True
            return mutant

    
    columna=[] #creo una lista columna, que se le van a ir agregando los elementos de las columnas
    for row in range(6): # recorro todas las filas, en este caso 6
        for colum in range(6): #recorro todas las columnas, en este caso 6
            element=adn[colum][row] # declaro variable element, que es cada elemento de las columnas 
            columna.append(element) # y lo agrego a la lista columna
    if buscarElementosJuntos(columna): # si se cumple la funcion "buscarelementosJuntos" es mutante, (le pasamos por parametro la lista columna)
        mutant=True
        return mutant        


    

    for row in range(len(adn)-3):  # recorre las filas de la matriz
        for column in range(len(adn)-3):  # recorre las columnas de la matriz
            diagonal = []  # se crea una lista llamada diagonal para añadir elementos de las diagonales
            for k in range(4):  # recorre 4 elementos para obtener una secuencia de 4 elementos
                diagonal.append(adn[row + k][column + k])  # Agrega cada elemento a la lista diagonal

    if buscarElementosJuntos(diagonal):  # Verifica si alguna de las secuencias cumple la funcion "buscarelementosJuntos" 
        mutant = True  
        return mutant  












            



    


   