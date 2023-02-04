# 4.6 - TARJETA DE BINGO

# Realizar un programa que genere 15 numero aleatorios enteros en el rango del 1 al 100, 
# que representaria la tarjeta de bingo de una persona. Una vez generado los numeros aleatorios solicitar al
# usuario que ingrese 3 numeros enteros, a parƟr de alli mostrar los siguientes mensajes:
# Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador Ɵene mala suerte,
# no marco ninguna casilla”.
# Caso contrario mostrar “El jugador marco algun numero de la tarjeta”


import random

tarjeta_bingo = []

for i in range(0,15):
    tarjeta_bingo.append(random.randint(1,100))    


print(tarjeta_bingo)

numeros_jugador = []

for i in range(0,3):
    numeros_jugador.append(int(input('Ingrese un numero: ')))
    
for i in numeros_jugador:
    booleano = i in tarjeta_bingo
    print(booleano)
    if booleano:
        break
    

# variable = any(i in numeros_jugador for i in tarjeta_bingo)             # TENGO DUDAS ACERCA DE ESTO


#print(variable)

    



