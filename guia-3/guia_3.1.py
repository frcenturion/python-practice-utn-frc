# 3.1 - PLAZO FIJO

# Desarrollar un programa que cargue por teclado la canƟdad de dinero depositada en plazo fijo por
# un cliente de un banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que
# el interés pactado era de 2.3 % y que el banco cobra una tasa fija de gastos por servicios financieros
# igual $20 por cuenta

tasa_fija = 20
tasa_interes = 0.70

cantidad_depositada = float(input('Ingrese la cantidad de dinero a depositar en el plazo fijo: '))

dinero_despues_del_plazo = (cantidad_depositada * (tasa_interes + 1)) - tasa_fija

print('La cantidad de dinero que tendra la cuenta al finalizar el plazo sera de $', dinero_despues_del_plazo)
