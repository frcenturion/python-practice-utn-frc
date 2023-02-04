# 4.7 - ANALISIS DE PALABRA

# Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular
# los siguientes puntos:
# Determinar la canƟdad de letras que Ɵene la palabra
# Mostrar un mensaje que informe si la palabra termina en vocal

palabra = input('Ingrese una palabra: ')

cantidad_letras = len(palabra)

termina_en_vocal = palabra[-1] in 'aAeEiIoOuU'

print('La cantidad de letras de la palabra es: ', cantidad_letras)

if termina_en_vocal:
    print('La palabra termina en vocal')
else:
    print('La palabra NO termina en vocal')