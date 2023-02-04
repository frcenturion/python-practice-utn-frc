# 4.10 - EDAD MINIMA

# Ingresar por teclado las edades de 3 parƟcipantes de un concurso.
# Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por
# teclado

edades = []

for i in range(1,4):
    edades.append(int(input(f'Ingrese la edad del participante {i}: ')))
    
edad_minima = int(input('Ingrese la edad minima: '))

cumple = all(edad >= edad_minima for edad in edades)

print(cumple)


