# 4.3 - JORNAL DE UN OPERARIO

# Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. 
# Usted deberá cargar por teclado el código de turno
# que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la canƟdad de horas
# trabajadas.
# La políƟca de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno
# diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo
# hace en el turno diurno cobra 35.50 pesos la hora

turno = int(input(('''Ingrese el codigo de turno en que trabajo el operario
      
1 - Diurno
2 - Nocturno
      
Codigo: ''')))

horas_trabajadas = int(input('Ingrese cantidad de horas trabajadas por el operario: '))

if turno == 1:
    jornal = 35.50 * horas_trabajadas
else:
    jornal = 40.60 * horas_trabajadas


print('El jornal del operario es: ', jornal)