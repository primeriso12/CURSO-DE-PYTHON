#Unidad Dos Coke.copy
#Vamos a suponer la venta de coca cola por mdio de una maquina dispensadora de 50 centavos con estos deniminadores:
#25 centavos - 10 centavos y 5 centavos; en un archivo llamado coke.py programa que solicite al usuario que inserte 
#una moneda, una por vez, informandoles al usuario el monto adeudado cada vez. Una vez que el usuario haya ingresado
#al menos 50 centavos, muestre la cantidad de centavos de cambio que se le adeuda, suponga que el usuario solo va a ingresar 
#enteros e ignore cuakquier entero que no sea una denominación aceptada.

precio = 50
denominaciones = [25,10,5]
ingresado = 0
adeudado = precio

while adeudado > 0:
    moneda = int(input("ingresa una moneda 25, 10, 5 centavos): "))
    if moneda in denominaciones:
        ingresado += moneda
        adeudado -= moneda
        print("Monto adeudado: {}centavos". format(adeudado))
    else:
        print("Moneda no aceptada. ingrese una moneda de 25, 10, 5 centavos")

if ingresado > precio:
    cambio = ingresado - precio
    print("Cambio: {} centavos". format(cambio))