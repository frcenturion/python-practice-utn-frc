# 3.3 - IMPORTE COMO CADENA

# Desarrollar un programa que cargue por teclado un importe (canƟdad de dinero) expresado como
# número en coma flotante y muestre un mensaje con esa canƟdad pero en dos formatos: en uno debe
# aparecer precedida por el signo “$” y en el otro debe aparecer precedida por la palabra “pesos”

importe = float(input('Cargue un importe: '))

formato_1 = 'Usted tiene $' + str(importe)
formato_2 = 'Usted tiene pesos' + str(importe) 


print(formato_1)
print(formato_2)