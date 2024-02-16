#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal


letra=input("ingresa una vocal:")

if letra.lower() in 'aeiou':
    print('es una vocal')

else:
    print('no es una vocal')