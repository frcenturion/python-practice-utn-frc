# 3.2 - FECHA COMO CADENA

# Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato “dd/mm/aaaa”, 
# y muestre por separado el día, el mes y el año. Ejemplo:
# si la cadena ingresada es “16/03/2015” el programa debe mostrar: “Día: 16 - Mes: 03 - Año: 2016”

fecha = input('Ingrese una fecha en formato dd/mm/aaaa: ')
fecha_2 = fecha.split('/')

#print('Dia: ', fecha_2[0], ' - Mes: ', fecha_2[1], ' - Anio: ', fecha_2[2])

# Otra forma: concatenando strings

dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]

print('Dia: ', dia, ' - Mes: ', mes, ' - Anio: ', anio)

