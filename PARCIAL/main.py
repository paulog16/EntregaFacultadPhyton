#PARCIAL 2-MAIN
adn=[]
#declaro matriz 

import funciones



while True:
    print('MENU')
    option=input('QUE DESEA HACER?\n1-INGRESAR LETRAS DE LOS GENES Y VERIFICAR SI ES MUTANTE\n2-SALIR\n')
    if option=="2":
        break
    elif option=="1":
        funciones.llenar_matriz(adn)
        print(adn)
        mutante=funciones.is_mutant(adn)
        if mutante:
            print('es mutante')
        else:
            print('no es mutante')
    else:
        print('opcion incorrecta')            


#EJEMPLOS DE MATRICES MUTANTES

#MATRIZ HORIZONTAL                      

#['AAAACG'],
#['CTGTGC'],
#['TTATTA'],
#['AGAGCG'],
#['CCCTAC'],
#['TCACTG']

#MATRIZ VERTICAL

#['ATGCAT'],
#['CTGTGC'],
#['TTATTA'],
#['TTAGCG'],
#['CCCTAC'],
#['TCACTG']

#MATRIZ DIAGONAL

#['AGTTAC']
#['GATTCA']
#['TGACGT']
#['TTCACG']
#['TGACCT']
#['ATCCCA']


#EJEMPLO DE MATRIZ NO MUTANTE

#['ATGCAT'],
#['CAGTGC'],
#['TTAGTA'],
#['AGACCG'],
#['CCCTAC'],
#['TCACTG']