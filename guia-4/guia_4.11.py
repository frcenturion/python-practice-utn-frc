# 4.11 - TERRENO

# Se ingresan las medidas de frente y fondo de un terreno.
# Determinar si es cuadrado o rectangular y calcular su superficie.

frente = float(input('Ingrese la medida del frente del terreno: '))
fondo = float(input('Ingrese la medida del fondo del terreno: '))

if frente == fondo:
    forma = 'cuadrada'
else:
    forma = 'rectangular'

superficie = frente * fondo


print('El terreno tiene forma ', forma, ' y su superficie es ', superficie)



