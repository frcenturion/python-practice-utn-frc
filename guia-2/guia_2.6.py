# 2.6 - PRECIO DE VENTA

# Conociendo el precio de lista de un arơculo, determinar:

# Precio de venta al contado (10 % de descuento)
# Precio de venta con tarjeta (5 % de recargo)


precio_lista = float(input('Ingrese el precio de lista de un arituclo: '))

precio_contado = precio_lista - precio_lista*0.10

precio_tarjeta = precio_lista*1.05

print('El precio al contado del articulo es ', precio_contado, ' y el precio con tarjeta es ', precio_tarjeta)
