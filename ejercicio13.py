#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

lista=[20, 50, "Curso", 'Python', 3.14]
print('esta es la lista original: \n',lista)
dato1=(input('ingresa un dato: '))
dato2=(input('ingresa otro dato: '))

lista[0]=dato1
lista[1]=dato2
print('esta es la lista con los datos agregados: \n',lista)
