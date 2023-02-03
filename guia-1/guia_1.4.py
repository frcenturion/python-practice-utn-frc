# 1.4 - ULTIMOS DIGITOS

# Como usaria el operador resto para obtener el valor del ultimo digito de un numero entero?
# Y como obtendria los ultimos dos digitos?

# Desarrolle un programa que cargue un numero entero por teclado, y muestre el ultimo digito y los ultimos dos digitos

# Ayuda: cuales son los posibles restos que se obtienen al dividir un numero cualquiera por 10?

numero = int(input('Escriba un numero: '))

unidad = numero % 10
decena = numero % 100


print('El ultimo digito del numero ingresado es ', unidad, ' y los ultimos dos digitos son ', decena)


