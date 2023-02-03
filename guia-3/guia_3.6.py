# 3.6 - CALCULO DE SUELDO

# Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional
# al cual pertenece. Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento
# del 8 % sobre su salario actual y un descuento de 2,5 % por servicios, informando los resultados con
# el formato que se especifica a conƟnuación:

# Nombre Empleado: xxxxxxxxx            Nuevo Salario: $ xxx
# Área Funcional: xxxxxxxxxxxx
# Salario Actual: $ xxxx

salario_actual = int(input('Ingrese el salario actual del empleado: '))
nombre = input('Ingrese el nombre del empleado: ')
area = input('Ingrese el area funcional del empleado: ')

nuevo_salario = (salario_actual * 1.08) 
descuento = salario_actual * 0.025

salario_final = nuevo_salario - descuento

print('Nombre empleado:', nombre, '                        Nuevo salario: $',salario_final)
print('Area funcional:', area)
print('Salario actual: $', salario_actual)




