# 3.8 - CALCULO DISTANCIA DE VIAJE

# Un persona cauƟvada por los paisajes argenƟnos se le ocurrió la loca idea de unir los puntos mas
# extemos (Ushuahia y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.
# Nuestro aventurero efecƟvamente inició la travesía pero se accidentó y solo recorrió X metros
# según su GPS.
# Usted debe solicitar ese valor e informar cuantos kilómetros y metros recorrió nuestro aventurero
# y que porcentaje represento lo recorrido del total de km a recorrer de Ushuahia a La Quiaca (para el
# porcentaje usted debera realizar los calculos en metros)

km_totales = 3641.3 
metros_totales = km_totales * 1000


metros_recorridos = int(input('Indique cuantos metros recorrio el ciclista: '))
km_recorridos = metros_recorridos / 1000

porcentaje_travesia = (metros_recorridos * 100) / metros_totales

print('El ciclista recorrio ', km_recorridos, ' kilometros')
print('Eso representa un ', porcentaje_travesia ,'% de la travesia que planeaba realizar')
