# if 

# print("\n ----------- CONDICIONAL IF -------------- \n")

# nombre = (input("Digite su nombre = "))
# edad = int(input("Digite su edad = "))

# if edad >= 18:
#     print(f"Hola {nombre}, eres mayor de edad y puedes entrar")
# else:
#     print(f"Hola {nombre}, eres menor de edad y no puedes entrar")


                    
# print("\n ----------- CONDICIONAL IF - Notas -------------- \n")

# nota = float(input("Digite la nota a evaluar = "))

# if (nota >= 0) and (nota <=59):
#     print(f"La nota {nota} tiene asignada una calificacion = F ")
# elif (nota > 59) and (nota <=69):
#     print(f"La nota {nota} tiene asignada una calificacion = D ")
# elif (nota > 69) and (nota <=79):
#     print(f"La nota {nota} tiene asignada una calificacion = C ")
# elif (nota > 79) and (nota <=89):
#     print(f"La nota {nota} tiene asignada una calificacion = B ")
# elif (nota > 89) and (nota <=100):
#     print(f"La nota {nota} tiene asignada una calificacion = A ")
# else:
#     print(f"La nota {nota} esta fuera del rango esperado ")


# print("\n ----------- CONDICIONAL IF - EDADES con error -------------- \n")

# try:

#     edad_2 = int(input("Digite la edad a evaluar = "))

#     if (edad_2 >= 0) and (edad_2 <=12):
#         print(f"La edad {edad_2} corresponde a la categoria Niño ")
#     elif (edad_2 > 13) and (edad_2 <=17):
#         print(f"La edad {edad_2} corresponde a la categoria Adolecente ")
#     elif (edad_2 > 17) and (edad_2 <=64):
#         print(f"La edad {edad_2} corresponde a la categoria Adulto ")
#     elif (edad_2 > 64):
#         print(f"La edad {edad_2} corresponde a la categoria Adulto mayor ")
#     else:
#         print(f"La edad {edad_2} no es valida ")

# except ValueError:
#     print("Error: debe ingresar una edad adecuada ")


# print("\n ----------- CONDICIONAL IF - validacion de usuario -------------- \n")

# try:

#     usuario_correcto = "nestor"
#     password_correcto = "1234"

#     usuario = (input("Digite el usuario = "))
#     password = (input("Digite la contraseña = "))

#     usuario_final = usuario.lower().strip().replace(" ","_")

#     if (usuario_correcto == usuario_final) and (password_correcto == password):
#         print(f"Bienvenido al sistema usuario {usuario_final}!")
#     else:
#         print("Credenciales incorrectas para el usuario {usuario_final}")

# except ValueError:
#     print("Error: debe ingresar unas credenciales adecuadas ")

print("\n ----------- CONDICIONAL IF - validacion de numeros -------------- \n")

try:

    numero_1 = input("Digita el primer valor = ")
    numero_1 = float(numero_1)

    numero_2 = float(input("\nDigite el segundo valor = "))

    operacion = (input("\nDigite el simbolo de la operacion que desee (+ , - , * , /) = "))

    if operacion == "+":
        print(f"\n SUMA: {numero_1} + {numero_2} = {numero_1 + numero_2} \n" )
    elif operacion == "-":
        print(f"\nRESTA: {numero_1} - {numero_2} = {numero_1 - numero_2} \n" )
    elif operacion == "*":
        print(f"\nMULTIPLICACION: {numero_1} * {numero_2} = {numero_1 * numero_2} \n" )
    elif operacion == "/":
        print(f"\nDIVISION: {numero_1} / {numero_2} = {numero_1 / numero_2} \n" )
    else:
        print("\nLa operacion seleccionada no esta en mis libros")

except ValueError:
    print("\nError: debe ingresar unas credenciales adecuadas ")