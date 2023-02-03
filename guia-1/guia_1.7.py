# 1.7 - PRECIO DEL BOLETO

# Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo
# del mismo se debe considerar el monto base (que se cobra siempre), más un valor extra calculado en
# base a la cantidad de kilómetros a recorrer: Por cada kilómetro a recorrer se cobra $0,30 de adicional


kilometros_a_recorrer = float(input('Ingrese los kilomteros a recorrer en el viaje: '))

monto_base = float(input('Ingrese el monto base del viaje: '))
monto_extra = 0.30 * kilometros_a_recorrer

print('El precio del boleto de viaje es de ', monto_base + monto_extra)

