# contador y condicionales 

import time

# contador = 1

# while contador <= 10:
#     print(f"Numero: {contador}")
#     contador += 1
#     time.sleep(1)

# print("Despegue")

# contador y condicionales 

# numero = 0

# while numero <= 20:

#     numero += 1
#     time.sleep(1)

#     if numero % 3 != 0:   # No es multiplo de 3 -  si es = 0 es por que Si es multiplo de 3
#         print(f"Numero: {numero}")

#     if numero == 15:
#         break

# print("Fin")

# intentos = 0

# while True:
    
#     password = input("\nIngrese su password: ")
#     validar_password = password == "python123"
#     intentos += 1

#     if intentos == 3:
#         print(f"\nNumero de intentos excedidos = {intentos}\n")
#         break

#     if  validar_password == True:
#         print(f"\nContraseña Correcta despues de {intentos} intentos\n")
#         break
#     else:
#         print("\nContraseña incorrecta, intente nuevament\n")


# print("\n ----------- JUEGO DE ADIVINANZAS -------------- \n")
# print("Ingrese un numero del 1 al 50, tienes 7 intentos para adivinar el numero adecuado ")

# intentos = 1

# while True:
    
#     numero = int(input(f"\nIngrese el numero del intento {intentos}: "))
#     validar_numero = numero == 7

#  #   while (numero >= 0 and numero <= 50) and numero.isdigit():
    
#     if intentos == 7:
#         print(f"\nNumero de intentos excedidos = {intentos}, game over, el nuemero era {numero}\n")
#         break

#     if  validar_numero == True and intentos < 7:
#         print(f"\nfelicidades, adivinaste el numero en {intentos} intentos, numero = {numero}\n")
#         break
#     else:
#         print(f"\nNumero incorrecto, sigue intentando, vas en el intento {intentos}\n")

#     intentos += 1


# print("\n ----------- CONDICIONAL FOR  -------------- \n")

# numero = int(input(f"Ingrese el numero: "))

# print(f"\ntabla del {numero}")

# for i in range(1,11):  # 1 - 10
#     resultado = numero*ipython123

#     print(f"\n{numero} * {i} = {resultado}")
#     time.sleep(1)


# print("\n ----------- CONDICIONAL FOR  -------------- \n")

# vocales = "aeiouAEIOU"
# contador = 0
# contador_u = 0
# contador_o = 0
# contador_e = 0
# contador_i = 0
# contador_a = 0

# texto = input(f"Ingrese un texto: ")


# for vocal in texto:  # 1 - 10
    
#     if vocal in vocales:
#         print(f"{vocal}")
#         contador += 1
    
#     if vocal == "a" or vocal == "A":
#         contador_a += 1
        
#     if vocal == "e" or vocal == "E":
#         contador_e += 1

#     if vocal == "i" or vocal == "I":
#         contador_i += 1

#     if vocal == "o" or vocal == "O":
#         contador_o += 1

#     if vocal == "u" or vocal == "U":
#         contador_u += 1
    
# print(f"\na = {contador_a}\ne = {contador_e}\ni = {contador_i}\no = {contador_o}\nu = {contador_u}\n ")



# print("\n ----------- CONDICIONAL FOR  -------------- \n")

# frutas = ["Manzana", "Banana","Cereza"]
# i = 0
# for fruta in frutas:
#     print(f"{i}. {fruta}")
#     i += 1

# print("\n ----------- CONDICIONAL FOR  -------------- \n")

# frutas = ["Manzana","Banana","Cereza"]

# for i, fruta in enumerate(frutas):
#     print(f"{i}. {fruta}")


# print("\n ----------- CONDICIONAL FOR  -------------- \n")

# menu = ["Pizza", "Hamburguesa", "Perros", "Tacos", "Salchipapa"]

# for posicion, elemento in enumerate(menu, start=1):  # La funcion enumerate(menu, start=1) entrega dos valores, la posicion y el elemento los cuales se asignan a las variables "posicion" y "elemento" del FOR
#     print(f"{posicion}. {elemento} \n")

# numero = int(input(f"Ingrese el numero de seleccion (1 - 5): "))

# for i, comida in enumerate(menu, start=1):
#     if i == numero:
#         print(f"{comida}")


print("\n ----------- CONDICIONAL FOR FIGURAS -------------- \n")

tamaño = int(input(f"Ingrese el tamaño: "))

for i in range(1,tamaño+1):  
    print("*" * i ) 

print("\n")

for i in range(1,tamaño+1):  
    print("*" * tamaño )

print("\n")

for i in range(tamaño,0,-1):  
    print("*" * i )