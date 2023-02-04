# 4.9 - LANZAMIENTO DE DADOS

# Simular un juego en el que se lanzan dos dados.
# Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana
# la máquina

import random

dado1 = [1,2,3,4,5,6]

dado2 = dado1


comando = input('Presione t para tirar los dados: ')

while comando == 't':
    numero_dado_1 = random.choice(dado1) 
    numero_dado_2 = random.choice(dado2)
    
    son_iguales = numero_dado_1 == numero_dado_2
    suma_par = (numero_dado_1 + numero_dado_2) % 2 == 0
    
    print('Los dados que obtuviste son: ', numero_dado_1, ' y ', numero_dado_2)

    if son_iguales or not suma_par:
        print('Ganaste')
    else:
        print('Perdiste')
        
    comando = input('Presione t para tirar los dados: ')
    
    




