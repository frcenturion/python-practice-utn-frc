# 2.9 - DATOS DE UN RECTANGULO

# Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el
# perímetro y la superficie del mismo.

ancho = float(input('Ingrese el ancho del rectangulo: '))
alto = float(input('Ingrese el alto del rectangulo: '))


superficie = alto * ancho
perimetro = alto*2 + ancho*2

print('La superficie del rectangulo es ', superficie)
print('El perimetro del rectangulo es ', perimetro)