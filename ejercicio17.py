#Escribir una tupla con los meses del año, luego pedir al usuario el número del mes que desee imprimir en pantalla. Obtener el mes de la tupla

tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre")

print(tupla)

numero = int(input("Ingrese el número del mes que desea mostrar: "))

print(tupla[numero-1])