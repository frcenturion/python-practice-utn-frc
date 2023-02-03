# 3.10 - TIEMPOS DE TRIATLON

# Un triatlón es una compeƟción deporƟva en que los parƟcipantes realizan tres carreras: una de
# natación, una ciclista y una pedestre.
# Desarrollar un programa que permita ingresar el Ɵempo (en minutos y segundos) logrados en cada
# etapa por uno de los deporƟstas parƟcipantes.
# Con esos datos determinar:

# Tiempo total de la prueba (en formato hh:mm:ss)
# Tiempo máximo y mínimo (en segundos)
# Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)

# Consejo: converƟr a segundos los horarios ingresados, para facilitar las operaciones

tiempo_natacion = input('Ingrese el tiempo en minutos:segundos en natacion: ')
tiempo_ciclismo = input('Ingrese el tiempo en minutos:segundos en ciclismo: ')
tiempo_pedestre = input('Ingrese el tiempo en minutos:segundos en pedestre: ')

tiempo_natacion_2 = tiempo_natacion.split(':')
tiempo_ciclismo_2 = tiempo_ciclismo.split(':')
tiempo_pedestre_2 = tiempo_pedestre.split(':')

tiempo_natacion_final = list(map(int, tiempo_natacion_2))
tiempo_ciclismo_final = list(map(int, tiempo_ciclismo_2))
tiempo_pedestre_final = list(map(int, tiempo_pedestre_2))











