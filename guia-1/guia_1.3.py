# 1.3 - AREA DE UN TRIANGULO

# Desarrolle un programa para calcular el area de un triangulo, cargando el valor por teclado de la base, pero sabiendo que
# su altura es igual al cuadrado de la base. (Observar que la altura no es un dato... solo se indica la forma de calcularla)

base = int(input('Cargue el valor de la base del triangulo: '))
altura = base**2

area_triangulo = (base*altura) / 2

print('El area del triangulo es', area_triangulo)
