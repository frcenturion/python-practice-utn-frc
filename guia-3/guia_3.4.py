# 3.4 - DURACION DE UN VUELO

# Desarrollar un programa que, conociendo el horario de parƟda y llegada de un vuelo (hora y minutos), 
# determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir
# del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?

minutos_taxi = 45

horario_partida = input('Ingrese el horario de partida del vuelo: ')
horario_llegada = input('Ingrese el horario de llegada del vuelo: ')


horas_minutos_partida = horario_partida.split(':')
horas_minutos_llegada = horario_llegada.split(':')


minutos_partida = int(horas_minutos_partida[1]) + int((horas_minutos_partida[0])) * 60
minutos_llegada = int(horas_minutos_llegada[1]) + int((horas_minutos_llegada[0])) * 60


duracion_vuelo = minutos_llegada - minutos_partida


print('La duracion del vuelo es de ', duracion_vuelo, ' minutos')

hora_llegada_hotel = (minutos_llegada + minutos_taxi) // 60
minutos_llegada_hotel = (minutos_llegada + minutos_taxi) % 60

print('El pasajero llegara a las ' + str(hora_llegada_hotel) + ':' + str(minutos_llegada_hotel))