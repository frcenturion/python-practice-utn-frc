# 1.5 - CONVERSION  DE MEDIDAS

# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

# yardas
# pulgadas
# centimetros
# metros

# Sabiendo que 

# 1 pie = 12 pulgadas
# 1 yarda = 3 pies
# 1 pulgada = 2.54 centimetros
# 1 metro = 100 centimetros

medida_en_pies = float(input('Ingrese una medida en pies: '))

medida_en_yardas = medida_en_pies / 3
medida_en_pulgadas = medida_en_pies * 12 
medida_en_centimetros = medida_en_pulgadas * 2.54
medida_en_metros = medida_en_centimetros / 100


print(f'''{medida_en_pies} pies equivalen a:
     
      {medida_en_yardas} yardas 
      {medida_en_pulgadas} pulgadas 
      {medida_en_centimetros} centimetros 
      {medida_en_metros} metros
      
      ''')





