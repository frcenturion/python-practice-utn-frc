# 4.8 - TIRADA DE MONEDA

# Programar una Ɵrada de una moneda (opciones: cara o cruz) aleatoriamente. PermiƟr que un
# jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta

import random

moneda = ['cara', 'cruz']

apuesta = input('Haga su apuesta, cara o cruz: ')

apuesta.lower()

comando = input('Presione t para tirar la moneda: ')

while comando == 't':
    resultado = random.choice(moneda)
    if resultado == apuesta:
        print('Acertaste')
    else:
        print('Fallaste')
    comando = input('Presione t para tirar la moneda: ')




    

