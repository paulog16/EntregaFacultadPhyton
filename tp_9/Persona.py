class Persona():
    def __init__(self):
        self.__nombre=''
        self.__edad=0
        self.__dni=''

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,new_at):
        self.__nombre= new_at 
         
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,new_at):
        self.__edad= new_at


    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,new_at):
        self.__dni= new_at  


    def mostrar(self):
        print(f'nombre: {self.__nombre}')     
        print(f'edad: {self.__edad}')     
        print(f'dni: {self.__dni}')

    def esmayor(self):
        esmayor=True
        if self.__edad<=18:
            esmayor=False
            print('mayor')
        else:
            esmayor=True
            print('menor')             