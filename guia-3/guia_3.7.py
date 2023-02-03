# 3.7 - CALCULO PRESUPUESTARIO

# En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto
# anual del hospital se reparte de la siguiente manera:

#       Área          Presupuesto
#   Urgencias           37 %
#   Pediatría           42 %
#   Traumatología       21 %

#Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que
#recibirá cada área.

presupuesto_total = int(input('Ingrese el monto del presupuesto total del hospital: '))

presupuesto_urgencias = presupuesto_total * 0.37
presupuesto_pediatria = presupuesto_total * 0.42
presupuesto_traumatologia = presupuesto_total * 0.21

print('Presupuesto urgencias: ', presupuesto_urgencias)
print('Presupuesto pediatria: ', presupuesto_pediatria)
print('Presupuesto traumatologia: ', presupuesto_traumatologia)