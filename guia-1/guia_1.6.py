# 1.6 -  VIAJE CORDOBA-ROSARIO

# Un vehiculo parte de la ciudad de cordoba y se dirige a rosario por autopista.
# La distancia aproximada entre ambas ciudades es de 400 km. El vehiculo se desplaza con una velocidad promedio de 122 km/h
# Desarrolle un programa que calcule el tiempo total en horas que demorara ese vehiculo en llegar a Rosario
# No es necesario convertir a horas, minutos y segundos: exprese el resultado como un numero real, tal cual lo haya obtenido del calculo.


# Sabiendo que d = v * t

velocidad = 122
distancia = 400

tiempo_total = distancia / velocidad

print('El tiempo total que tarda un vehiculo que va a ', velocidad, ' km/h desde Cordoba a Rosario es de ', tiempo_total, ' horas')
