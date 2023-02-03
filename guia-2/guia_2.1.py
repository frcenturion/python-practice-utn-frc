# 2.1 - CUADRADOS Y CUBOS

# Leer dos numeros y calcular 

# La suma de sus cuadrados
# El promedio de sus cubos

num1 = float(input('Ingrese un numero: '))
num2 = float(input('Ingrese otro numero: '))

suma_cuadrados = num1**2 + num2**2
promedio_cubos = (num1**3 + num2**3) / 2

print('La suma de los cuadrados de ', num1, ' y ', num2, ' es ', suma_cuadrados)
print('El promedio de los cubos de ', num1, ' y ', num2, ' es ', promedio_cubos)


