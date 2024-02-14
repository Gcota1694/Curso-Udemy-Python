#Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
#en este paso ponemos todo lo que ocupamos preguntar al usuario
practica1=float(input('Ingrese el valor de la practica 1:'))
practica2=float(input('Ingresa el valor de la practica 2:'))
practica3=float(input('Ingresa el valor de la practica 3:'))
ExamenParcial=float(input('Ingrese el valor del examen parcial:'))
ExamenFinal=float(input('Ingrese el valor del examen final:'))
#aqui se haecen las operaciones correspondientes
Promediopracitca=(practica1+practica2+practica3)/3
promedioFinal=(Promediopracitca+2*ExamenParcial+3*ExamenFinal)/6
print('Los promedio de practica estudiante es de:  \n',Promediopracitca,'\n y el promedio final es de: \n',promedioFinal )
