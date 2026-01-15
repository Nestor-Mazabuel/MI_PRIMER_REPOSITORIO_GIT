# CALCULADORA MEJORADA

print("\n ----------- CALCULADORA -------------- \n")

numero_1 = input("Digita el primer valor = ")
numero_1 = float(numero_1)

numero_2 = float(input("Digite el segundo valor = "))

resultado = numero_1 + numero_2

print(f"\n SUMA: {numero_1} + {numero_2} = {numero_1 + numero_2} \n" )
print(f"RESTA: {numero_1} - {numero_2} = {numero_1 - numero_2} \n" )
print(f"MULTIPLICACION: {numero_1} * {numero_2} = {numero_1 * numero_2} \n" )
print(f"DIVISION: {numero_1} / {numero_2} = {numero_1 / numero_2} \n" )
print(f"DIVISION ENTERA: {numero_1} // {numero_2} = {numero_1 // numero_2} \n" )
print(f"RESIDUO: {numero_1} % {numero_2} = {numero_1 % numero_2} \n" )
print(f"POTENCIA: {numero_1} ** {numero_2} = {numero_1 ** numero_2} \n" )

print("\n ----------- AREA DEL CIRCULO -------------- \n")

radio = int(input("Digite el valor del radio del circulo = "))
pi = float(3.1416)

print(f"\n El area del circulo se da por - Area = {pi} * {radio} ** 2 = { pi * (radio ** 2)} \n" )

print("\n ----------- CONVERSION DE FARENHEIT A CENTIGRADOS -------------- \n")

farenheit = float(input("Digite los grados Farenheit para convertir a Celsius = "))

print(f"\n La conversion de los grados {farenheit} °F a Celsius es = { ((farenheit-32) * 5)/9 } \n" )