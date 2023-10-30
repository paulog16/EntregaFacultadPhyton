class Agenda:
    def __init__(self):
        self.__nombre=''
        self.__telefono=''
        self.__email=''
        self.__contactos=[]

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,new_at):
        self.__nombre= new_at


    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self,new_at):
        self.__telefono= new_at


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,new_at):
        self.__email= new_at
              

    def añadirContactos(self):

        self.__nombre=input('ingrese nombre del contacto: ')
        self.__telefono=input('ingrese telefono del contacto: ')
        self.__email=input('ingrese email del contacto: ')

        contacto={'nombre':self.__nombre,'telefono':self.__telefono,'email':self.__email}
        self.__contactos.append(contacto)

    def listaContactos(self):
        for i in self.__contactos:
            print(i)


    def buscarContacto(self):
        search_person=input('digame el nombre del contacto: ')
        for i in self.__contactos:
            if i['nombre']==search_person:
                    print(i)
            else:
                print('el contacto no se encuentra')

    def editarContacto(self):
        while True:
            op=input('que opcion quiere editar?\nnombre\ntelefono\nemail\nsalir\nopcion: ')
            
            if op=='nombre':
                person=input('de quien quiere editar el nombre: ')
                nombreNuevo=input('que nombre quiere ponerle? ')
                for i in self.__contactos:
                   
                    if i['nombre']==person:
                        i['nombre']=nombreNuevo
                    else:
                        print('no se encuentra el contacto')

            elif op=='telefono':
                person=input('de quien quiere editar el nombre: ')
                telefonoNuevo=input('que telefono quiere ponerle? ')
                for i in self.__contactos:
                        if i['nombre']==person:
                            i['telefono']=telefonoNuevo
                        else:
                            print('no se encuentra el contacto')
            
            elif op=='email':
                person=input('de quien quiere editar el nombre: ')
                emailNuevo=input('que nombre quiere ponerle? ')
                for i in self.__contactos:
                    if i['nombre']==person:
                        i['email']=emailNuevo
                    else:
                        print('no se encuentra el contacto')
            else:
                break                                



