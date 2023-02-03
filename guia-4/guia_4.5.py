# 4.5 - TEMPERATURA DIARIA

# Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un día y determinar:
# Cual es el promedio de las temperaturas
# Si existe alguna temperatura que sea mayor al promedio

temperatura1 = int(input('Ingrese la temperatura de la maniana: '))
temperatura2 = int(input('Ingrese la temperatura de la tarde: '))
temperatura3 = int(input('Ingrese la temperatura de la noche: '))

promedio_temperaturas = (temperatura1 + temperatura2 + temperatura3) / 3

def es_mayor_al_promedio(temperatura, promedio):
    return temperatura > promedio

existe_temp_mayor_al_promedio = es_mayor_al_promedio(temperatura1) or es_mayor_al_promedio(temperatura2) or es_mayor_al_promedio(temperatura3)

if existe_temp_mayor_al_promedio:
    print('Existe una temperatura mayor al promedio')