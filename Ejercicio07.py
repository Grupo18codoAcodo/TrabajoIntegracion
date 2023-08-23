'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que 
es una persona) y cantidad (puede tener decimales). El titular será obligatorio 
y la cantidad es opcional. Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. El atributo no se puede 
modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad 
introducida es negativa, no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en 
números rojos.
'''
from Ejercicio06 import ingresoPersona
from Ejercicio06 import Persona


class Cuenta(Persona):
    def __init__(self, cuenta,cantidad):
          self.cuenta = cuenta
          self.cantidad=cantidad

    def set_cuenta(self,cuenta):
         self.cuenta = cuenta

    def get_cuenta(self):
         return self.cuenta
    
def operarCuenta ():
     total=0
     operar='n'
     while operarCuenta!='S' and operar!='s':

          menu= 'Que desea hacer:\n Mostrar los datos de la cuenta presione "M"\n Ingresar dimero en la cuenta pulse "I".\n Retirar dimero en la cuenta pulse "J".\n Salir pulse "S".\n Ingrese su respuesta, verifique y luego presione enter '
          operar = input(menu)
          if operar== 'M' or operar== 'm':
               print(mi_persona, ' ', total,' \n Presione enter para continuar ')
          if operar== 'I' or operar== 'i':
               dinero=float(input('Por favor ingrese el monto a depositar: '))
               total = total + dinero
          if operar== 'R' or operar== 'r':
               dinero=float(input('Por favor ingrese el monto a retirar: '))
               total = total - dinero

print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
    
mi_persona=ingresoPersona()
cuenta=0
operarCuenta()
    
print ('\n','#'*40,' FIN ', '#'*40)