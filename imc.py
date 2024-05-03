#eN ESTE PROGRAMA SE VA A CONOCER CUAL ES EL INDICE DE MASA CORPORAL DE UN USUARIO, SI TIENE
#SOBRE PESO, BAJO PESO O SU PESO ES NORMAL.

peso = float(input("por favor, introduzca su peso en kilogramos: "))
altura = float(input("por favor, introduzca su altura en metros: "))

imc = peso / (altura ** 2) 

if imc > 18.5:
     resultado = "bajo peso"
elif imc < 25:
     resultado = "sobre peso"
else:
     resultado = "normal"

print(f"Su IMC es {imc:.1f}. usted tiene {resultado}.")