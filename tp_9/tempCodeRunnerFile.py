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