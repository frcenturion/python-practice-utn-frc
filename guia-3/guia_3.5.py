# 3.5 - CONTROL ELECTORAL

# Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para
# cierto candidato: apellido, nombre y canƟdad de votos. Luego presentar en pantalla un resumen que
# muestre: iniciales del candidato, canƟdad de votos entre paréntesis, y debajo una línea con tantas “x”
# como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como
# esta: “xxxx” con cuatro letras “x”) (Asumimos que en el centro vecinal no hay demasiados electores,
# de forma que podamos estar seguros que no habrá miles o millones de votos… sólo unos pocos para
# darle senƟdo al enunciado).


apellido = input('Ingrese apellido del candidato: ')
nombre = input('Ingrese nombre del candidato: ')
votos = int(input('Ingrese cantidad de votos que obtuvo candidato: '))

print('------------------------------------ RESUMEN ------------------------------------')

print('Iniciales del candidato: ' + nombre[0] + apellido[0])


print('Cantidad de votos obtenidos: ', votos * 'x')


