'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva 
clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea 
esta nueva clase, además del titular y la cantidad se debe guardar una bonificación 
que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
 Un constructor.  Los setters y getters para el nuevo atributo. 
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero 
si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación 
de la cuenta.
'''
print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):




    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)