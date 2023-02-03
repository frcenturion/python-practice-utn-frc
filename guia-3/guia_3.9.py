# 3.9 - COSTOS DEL PROYECTO

# Una pequeña empresa de informaƟca Ɵene que desarrollar un sistema de informacion (a.k.a un
# super programa) y para ello Ɵene un presupuesto X para cubrir los costos de crear el sistema. Sabiendo
# que Ɵene pensado ganar almenos 17 % por el proyecto, determine cual es el valormáximo que pueden
# alcanzar los costos del proyecto


presupuesto = int(input('Ingrese el presupuesto del proyecto: '))

ganancia_estimada = presupuesto * 0.17

costos = presupuesto - ganancia_estimada

print('Los costos del proyecto no deben exceder los $', costos)

