# 5.1 - OPERACIONES DE ORDEN CON TRES NUMEROS

# Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es
# el resto de la división de los dos primeros


numeros = []

for i in range(0,3):
    numeros.append(int(input('Ingrese un numero: ')))

numeros.sort(reverse = True)

if numeros[0] % numeros[1] == numeros[2]:
    print('El numero ', numeros[2], ' es el resto de la division entre ', numeros[0], ' y ', numeros[1])


