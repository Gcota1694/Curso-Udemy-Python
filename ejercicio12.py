#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.


candidato=input('Ingrese el candidato que desea elegir (A,B,C):')

if candidato.upper() =='A':
    print('Usted a elegido Rojo')
elif candidato.upper() =='B':
    print('Usted elegido al candidato Verde')
elif candidato.upper() =='C':
    print('Usted a elgido al candidato Azul')

else:
    print('Opción errónea')