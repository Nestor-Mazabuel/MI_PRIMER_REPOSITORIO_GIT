try:
    numero_1 = float(input("Digite el primer valor: "))
    numero_2 = float(input("Digite el segundo valor: "))
    operacion = input("Digite la operación (+, -, *, /): ")

    if operacion == "+":
        resultado = numero_1 + numero_2
        print("Resultado:", resultado)

    elif operacion == "-":
        resultado = numero_1 - numero_2
        print("Resultado:", resultado)

    elif operacion == "*":
        resultado = numero_1 * numero_2
        print("Resultado:", resultado)

    elif operacion == "/":
        if numero_2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            resultado = numero_1 / numero_2
            print("Resultado:", resultado)

    else:
        print("Operación no válida")  

except ValueError:
    print("Error: debe ingresar números válidos")