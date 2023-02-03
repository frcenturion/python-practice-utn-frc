# 4.4 - GALERIA DE ARTE

# Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba
# con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si
# todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y
# terminó en el año 2000). Determinar cuántos Ɵenen anƟgüedad inferior a 10 años. Si no hay ninguno,
# imprimir el mensaje “Renovar stock”

cuadro1 = int(input('Ingrese anio en que fue creada la primera obra: '))
cuadro2 = int(input('Ingrese anio en que fue creada la segunda obra: '))
cuadro3 = int(input('Ingrese anio en que fue creada la tercer: '))


ANIO_ACTUAL = 2023

renovar_stock = True

def antiguedad_menor_a_10(cuadro):
    return (ANIO_ACTUAL - cuadro) < 10

def del_siglo_pasado(cuadro):
    return cuadro < 1901

if antiguedad_menor_a_10(cuadro1) or antiguedad_menor_a_10(cuadro2) or antiguedad_menor_a_10(cuadro3):
    renovar_stock = False

son_antiguas = del_siglo_pasado(cuadro1) and del_siglo_pasado(cuadro2) and del_siglo_pasado(cuadro3)



if son_antiguas:
    print('Todas las obras de arte son anteriores al siglo XX')

if renovar_stock:
    print('Todas las obras tienen mas de 10 anios de antiguedad, se debe renovar el stock')
