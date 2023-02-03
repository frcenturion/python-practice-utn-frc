# 4.1 - GENERADOR DE DIRECCION DE MAIL

# Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre 
# y apellido ingresado de acuerdo a las siguientes reglas:

# Componer la dirección de correo de la siguiente manera:
# <primera letra del nombre><apellido>@<dominio>
# Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería: 
# fsteffolani@frc.utn.edu.ar

# Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar:
# <nombre>.<apellido>@<dominio>
# Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la
# dirección de mail sería:
# soledad.steffolani@colegiorosarito.edu.ar


nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
dominio = input('Ingrese dominio: ')

nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()

primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_apellido == primera_letra_nombre:
    direccion = nombre + '.' + apellido + '@' + dominio
else:
    direccion = primera_letra_nombre + apellido + '@' + dominio
    
print(direccion)