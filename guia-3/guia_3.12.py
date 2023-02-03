# 3.12 - CALCULO DE POSTA DE NATACION

# En la disciplina olimpica una de las pruebas mas esperadas es en la natacion la posta 4 x 100 esƟlos.
# En esta disciplina el equipo nadador registro los siguientes Ɵempos en cada esƟlo:

# Espalda 52 seg 15 centesimas
# Pecho 1 minuto 2 segundos 75 centesimas
# Mariposa 59 segundos 80 centesimas
# Crol o Libre 48 segundos 15 centesimas

# Usted debe averiguar el Ɵempo total de la carrera del equipo ganador y representarlo en minutos,
# segundos y centesimas

# Para recordar
# 1 minutos son 60 segundos
# 1 segundo son 100 centesimas


centesimas_espalda = 52 * 100 +  15
centesimas_pecho = 1 * 60 * 100 + 2 * 100 + 75
centesimas_mariposa = 59 * 100 + 80
centesimas_crol = 48 * 100 + 15


tiempo_total = centesimas_espalda + centesimas_pecho + centesimas_mariposa + centesimas_crol

minutos = tiempo_total // 6000          # entero de la divison nos da los minutos 
resto = tiempo_total % 6000             # el resto de la division nos devuelve los segundos en centesimas

segundos = resto // 100                 # pasamos las centesimas del resto a segundos
centesimas = resto % 100                # y el resto de esta division nos da las centesimas finales

print('El equipo ganador tardo ', minutos, ':', segundos, ':', centesimas, ' en completar la competicion')






