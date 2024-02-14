#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

#• Imprima los dos primeros caracteres.

#• Imprima los tres últimos caracteres.

#• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

#• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

#• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.


cadena1=('Te quiero solo como amigo')
cadena2=('recta')

print(len(cadena1))
print(cadena1[: 2])
print(cadena1[-3: ])
print(cadena2[::2])
print(cadena1[::-1])
print(cadena1+cadena1[:: -1])