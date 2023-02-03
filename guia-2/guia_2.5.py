# 2.5 -  CALCULO DE ANGULOS

# Se sabe que la suma de dos ángulos desconocidos (𝛼+𝛽) es igual a cierto valor 𝑥 que se carga por
# teclado. Además se sabe que la diferencia entre esos mismos dos ángulos (𝛼−𝛽) es igual a otro valor
# 𝑦 que también se carga por teclado. Desarrolle un programa que dados los valores 𝑥 e 𝑦, determine
# el valor de los dos ángulos 𝛼 y 𝛽. No es necesario convertir a grados, minutos y segundos el valor de
# cada ángulo: expréselos como números reales, tal cual hayan sido obtenidos

x = float(input('Cargue el valor de x: '))
y = float(input('Cargue el valor de y: '))

beta = (x - y) / 2
alpha = y + beta

print('El valor de alpha es ', alpha, ' y el valor de beta es ', beta)