# 2.8 -  RINDE DE UN CAMPO AGRICOLA

# Un productor agrícola desea saber cuantos quintales de trigo puede producir en su parcela, por lo
# tanto, se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que
# en 10 m2 se obƟene 2 quintales.

largo_parcela = float(input('Ingrese el largo de la parcela en metros: '))
ancho_parcela = float(input('Ingrese el ancho de la parcela en metros: '))

metros_cuadrados_parcela = largo_parcela * ancho_parcela

quintales_a_producir = (metros_cuadrados_parcela * 2) / 10

print('Los quintales a prodcuir en la parcela son ', quintales_a_producir)