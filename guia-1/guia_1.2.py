# 1.2 - CUADRADO DE UN BINOMIO

# Plantear un script que permita mostrar, para dos valores de a y b, que:
# Un binomio al cuadrado (suma) es igual al cuadrado del primer termino, mas el doble producto del primero por el segundo mas el cuadrado del segundo

a = int(input("Ingrese un valor de a: "))
b = int(input("Ingrese un valor de b: "))

binomio_1 = (a + b) * (a + b)

binomio_2 = a**2 + 2*a*b + b**2

print('Notemos que ', binomio_1, 'es igual a ', binomio_2)



