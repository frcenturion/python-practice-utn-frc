# 2.7 - VOTACION EN EL CONGRESO

# En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita
# ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso

votos_a_favor = int(input('Ingrese la cantidad de votos a favor: '))
votos_en_contra = int(input('Ingrese la cantidad de votos en contre: '))

votos_totales = votos_en_contra + votos_a_favor

porcentaje_favor = (votos_a_favor * 100) / votos_totales
porcentaje_contra = (votos_en_contra * 100) / votos_totales

print('La ley tuvo un total de ', votos_totales, ' votos')
print('El porcentaje de votos a favor es ', porcentaje_favor, '%')
print('El porcentaje de votos en contra es ', porcentaje_contra, '%')

