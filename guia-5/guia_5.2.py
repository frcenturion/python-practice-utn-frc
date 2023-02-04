# 5.2 - ELECCIONES PRESIDENCIALES

# Según la Ley Electoral de la República ArgenƟna, el Presidente y el Vicepresidente se eligen de
# acuerdo a las siguientes reglas:
# Arơculo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %)
# de los votos afirmaƟvos válidamente emiƟdos; en su defecto, aquella que hubiere obtenido el cuarenta
# por ciento (40 %) por lo menos de los votos afirmaƟvos válidamente emiƟdos y, además, exisƟere una
# diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmaƟvos válidamente
# emiƟdos, sobre la fórmula que le sigue en número de votos.
# Arơculo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escruƟnio
# ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la
# Asamblea LegislaƟva atento lo dispuesto por el arơculo 120 de la presente ley, se realizará una segunda
# vuelta dentro de los treinta (30) días.
# Arơculo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas en la
# primera, resultando electa la que obtenga mayor número de votos afirmaƟvos válidamente emiƟdos.

# Desarrollar un programa que permita ingresar, para los 3 parƟdos más votados: fórmula (presidente + vice) y canƟdad de votos obtenidos.

# Luego determinar:

# Qué fórmula obtuvo el mayor porcentaje.
# Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes
#parƟcipan de la segunda vuelta


votacion = []

for i in range(0, 3):
    presidente, vice, votos = input('Ingrese presidente: '), input('Ingrese vicepresidente: '), int(input('Ingrese cantidad de votos: '))
    print('\n')
    formula = presidente, vice, votos
    votacion.append(formula)

votos_formula_1 = votacion[0][2] 
votos_formula_2 = votacion[1][2]
votos_formula_3 = votacion[2][2]

votos_totales = votos_formula_1 + votos_formula_2 + votos_formula_3

porcentaje_formula_1 = (votos_formula_1 * 100) / votos_totales
porcentaje_formula_2 = (votos_formula_2 * 100) / votos_totales
porcentaje_formula_3 = (votos_formula_3 * 100) / votos_totales


resultado_formula_1 = votacion[0][0], votacion[0][1], porcentaje_formula_1 
resultado_formula_2 = votacion[1][0], votacion[1][1], porcentaje_formula_2 
resultado_formula_3 = votacion[2][0], votacion[2][1], porcentaje_formula_3 


votacion.clear()
votacion.append(resultado_formula_1) 
votacion.append(resultado_formula_2) 
votacion.append(resultado_formula_3) 


primer_puesto = max(votacion, key = lambda x : x[2])    # esto nos devuelve la tupla con el mayor porcentaje de votos

votacion.remove(primer_puesto)

segundo_puesto = max(votacion, key = lambda x : x[2])  # esto nos devuelve la segunda formula mas votada, porque anteriormente elimninamos de la lista la primera



segunda_vuelta = False

if primer_puesto[2] >= 45 or (primer_puesto[2] >= 40 and (primer_puesto[2] - segundo_puesto[2] >= 10)):
    print('Gano la formula de ', primer_puesto[0], ' y ', primer_puesto[1])
else:
    print('Habra segunda vuelta entre la formula de ', primer_puesto[0], ' y la de ', segundo_puesto[0])














