# 2.3 - ECUACION DE EINSTEIN

# La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
# 𝐸 = 𝑚𝑐2
# Donde c es la velocidad de la luz cuyo valor es 𝑐 = 299792.458𝑘𝑚/𝑠𝑒𝑔.
# Desarrolle un programa que lea el valor de una masa 𝑚 en kilogramos y obtenga la cantidad de energía 𝐸 producida en la conversión.

velocidad_de_la_luz = 299792.458

masa = float(input('Ingrese el valor de una masa en kilogramos: '))

energia = masa * (velocidad_de_la_luz**2)

print('La cantidad de energia producida en la conversion es de ', energia)





