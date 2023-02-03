# 2.2 - DESCUENTO EN MEDICINAS

# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar
# por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35 %.
# Mostrar el precio actual, el monto del descuento y el monto final a pagar.

precio_medicamento = float(input('Cargar precio del medicamento: '))

descuento = precio_medicamento * 0.35

precio_final = precio_medicamento - descuento

print('El precio actual del medicamento es ', precio_medicamento)
print('El descuento es ', descuento)
print('El precio final del medicamento es ', precio_final)