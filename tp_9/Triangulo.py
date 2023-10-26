"""3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

class Triangulo:
    def __init__(self):
        self.__lado1=0
        self.__lado2=0
        self.__lado3=0
    @property
    def lado1(self):
        return self.__lado1

    @lado1.setter
    def lado1(self,new_at):
        self.__lado1= new_at

    @property
    def lado2(self):
        return self.__lado2

    @lado2.setter
    def lado2(self,new_at):
        self.__lado2= new_at

    @property
    def lado2(self):
        return self.__lado2

    @lado2.setter
    def lado2(self,new_at):
        self.__lado2= new_at

    def ladomayor(self):
        if self.__lado1>self.__lado2 and self.__lado1>self.__lado3:
            print(f'el lado mayor es {self.__lado1}')
        elif self.__lado2>self.__lado1 and self.__lado2>self.__lado3:
            print(f'el lado mas grande es {self.__lado2}')
        elif self.__lado3>self.__lado1 and self.__lado3>self.__lado2:
            print(f'el lado mas largo es {self.__lado3}')
        else:
            print('son todos iguales')

    def tipo(self):
        if self.__lado1 == self.__lado2 and self.__lado2 == self.__lado3:
            print('equilátero')
        elif self.__lado1 == self.__lado2 or self.__lado1 == self.__lado3 or self.__lado2 == self.__lado3:
            print('isósceles')
        else:
             print('escaleno')

