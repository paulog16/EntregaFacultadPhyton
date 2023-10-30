from Persona import Persona

p1= Persona()
p1.edad=20
p1.nombre='paulo'
p1.dni='44841460'
p1.mostrar()
p1.esmayor()
from Cuenta import Cuenta
c1=Cuenta()
ingreso=float(input('ingrese dinero a la cuenta: '))
c1.ingresar(ingreso)
retirar=float(input('retire dinero de la cuenta: '))
c1.retirar(retirar)
c1.titular='paulo'
c1.mostrar()

from Triangulo import Triangulo
t=Triangulo()

t.lado1=14
t.lado2=14
t.lado3=13

t.ladomayor()
t.tipo()


#AGENDAA
from Agenda import Agenda
a1=Agenda()

while True:
    op=input('QUE DESEA HACER?\n1-AÑADIR CONTACTO\n2-LISTA CONTACTOS\n3-BUSCAR CONTACTO\n4-EDITAR CONTACTO\n5-CERRAR AGENDA\nOPCION: ')

    if op=='1':
        a1.añadirContactos()
        
    elif op=='2':
        a1.listaContactos()
    elif op=='3':
        a1.buscarContacto()
    elif op=='4':
        a1.editarContacto()
    elif op=='5':
        print('cerrando agenda....')
        break        




