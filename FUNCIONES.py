# FUNCIONES 

print("\n ----------- FUNCIONES -------------- \n")

def saludo():           # Se define la funcion
    print("Hola")

saludo()                # Se llama la funcion y ejecuta lo que tenga adentro

print("\n ----------- FUNCION Y LLAMARLA 3 VECES -------------- \n")

def despedida():
    print("\nHasta luego")


despedida()
despedida()
despedida()

print("\n ----------- FUNCION, PARAMETROS Y ARGUMENTOS -------------- \n")

def saludar(nombre):
    print(f"\nHola {nombre}")

saludar("Juan")

print("\n ----------- FUNCION, PARAMETROS Y ARGUMENTOS y return -------------- \n")

def calcular_area(base, altura):
    area = base * altura
    return area                     # El return devuelve el valor de la variable y queda disponible para usarse en otras cosas

resultado = calcular_area(5, 3)     # Como el return devuelve el area, entonces se almacena area en resultado
print(f"\nEl resultado es {resultado}")
print(f"\nEl resultado es {calcular_area(5, 3)}")


print("\n -----------CALCULADORA - --- FUNCION, PARAMETROS Y ARGUMENTOS y return -------------- \n")

seleccion = 0

def operaciones (num_1,num_2):
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 / num_2

    return suma, resta, multiplicacion, division

while seleccion != 5:

    print("\n -- MENU -- \n")

    menu = ["sumar", "restar", "multiplicar", "dividir", "salir"]
    cantidad_menu = len(menu)

    for i , accion in enumerate(menu, start=1):
        print(f"{i}. {accion}")
    print("\n")

    while True:
        
        seleccion = (input(f"Ingrese el numero de seleccion (1 - 5): "))
       
        if seleccion.isdigit() :  # Como puedo hacer la validacion de que lo que ingrese este entre 1 - 6 si es texto?
            seleccion = int(seleccion)
            if 0 < seleccion < 6:
                break
            else:
                print("\nError: El numero debe estar entre 1 y 6\n")
        else:
            print("\nError: El valor ingresado no es permitido dentro del listado\n")
            continue

    match seleccion:
            case 1:
                print("\nSUMA\n")
                
                numero_1 = input("Digita el primer valor = ")
                numero_1 = float(numero_1)

                numero_2 = float(input("Digite el segundo valor = "))

                resultado = operaciones (numero_1,numero_2)

                print(f"\nLa suma es igual a = {resultado[0]}")
                
            case 2:
                print("\nRESTA\n")

                numero_1 = int(input("Digite el Numero 1 = "))
                numero_2 = int(input("\nDigite el Numero 2 = "))

                resultado = operaciones (numero_1,numero_2)

                print(f"\nLa resta es igual a = {resultado[1]}")
        
            case 3:
                print("\nMULTIPLICACION\n")

                numero_1 = int(input("Digite el Numero 1 = "))
                numero_2 = int(input("\nDigite el Numero 2 = "))
                peracion = numero_1 * numero_2

                resultado = operaciones (numero_1,numero_2)

                print(f"\nLa multiplicacion es igual a = {resultado[2]}")

            case 4:
                print("\nDIVISION\n")

                numero_1 = int(input("Digite el Numero 1 = "))
                numero_2 = int(input("\nDigite el Numero 2 = "))

                resultado = operaciones (numero_1,numero_2)

                print(f"\nLa division es igual a = {resultado[3]}")
print("\n Saliendo el programa ... gracias \n")


