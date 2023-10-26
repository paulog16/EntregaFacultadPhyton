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


