'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que 
es una persona) y cantidad (puede tener decimales). El titular será obligatorio 
y la cantidad es opcional. Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. El atributo no se puede 
modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se ingresa 
una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en 
números rojos.
'''
print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):




    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)