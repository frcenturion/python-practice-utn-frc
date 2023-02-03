# 2.4 - POLINOMIO DE SEGUNDO GRADO

# Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado, y calcule 
# y muestre el valor del polinomio en el punto x (cargando también x por teclado).
# Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación

# la formula de un polinomio de segundo grado es: a*(x**2) + b*x + c

a = int(input('Cargue el valor de a: '))
b = int(input('Cargue el valor de b: '))
c = int(input('Cargue el valor de c: '))
x = int(input('Cargue el valor del punto x: '))

valor_polinomio = a*(x**2) + b*x + c

# La fomrmula para calcular el discriminante es: b**2 - 4*a*c

valor_discriminante = b**2 - 4*a*c


print('Para el polinomio dado, el valor del mismo en el punto ', x, ' es ', valor_polinomio, ' y el valor del discriminante es ', valor_discriminante)


