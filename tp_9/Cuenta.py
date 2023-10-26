"""
2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
•	mostrar(): Muestra los datos de la cuenta.
•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

class Cuenta:
    def __init__(self):
        self.__titular=''
        self.__cantidad=float(0)
       
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,new_at):
        self.__titular= new_at 
         
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,new_at):
        self.__cantidad= new_at

    def mostrar(self):
        print(f'titular {self.__titular}')    
        print(f'cantidad {self.__cantidad}')    

    def ingresar(self,dinero):
        
        self.__cantidad+=dinero

    def retirar(self,retirar):
    
        if retirar>self.__cantidad:
            print('no se puede')
        else:
            self.__cantidad-=retirar
                 

    

