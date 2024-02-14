#Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

from math import sqrt

a=int(input('ingresa el valor a: '))
b=int(input('ingresa el valor b : '))
c=int(input('ingresa el valor c: ' ))

x1= 0
x2= 0

if ((b**2)-(4*a*c)) < 0:
    print('no se puede realizar la operacion')
else:
    x1= (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2= (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print ('la solucion es:\nX1=',x1,'\nX2=',x2)