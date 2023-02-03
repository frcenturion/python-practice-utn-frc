# 4.2 - SUMA - DIVISION - POTENCIA

# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado
# es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado
# al cubo.

num1 = int(input('Ingrese numero 1: '))
num2 = int(input('Ingrese numero 2: '))
num3 = int(input('Ingrese numero 3: '))


suma = num1 + num2 + num3

if suma > 2:
    suma // 2
else:
    suma ** 2
