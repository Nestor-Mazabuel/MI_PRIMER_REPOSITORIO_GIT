# PROYECTO CALCULADORA INTERACTIVA

# Menu interactivo de calculadora:

# 1. Menu que se repita hasta Salir (while True)
# 2. Opciones: Sumar, Restar, Multiplicar, Dividir, Historial, Salir
# 3. Sumar: pedir cuantos numeros, usar for para pedirlos
# 4. Otras operaciones: pedir 2 numeros
# 5. Guardar resultados en string "historial"
# 6. Historial: mostrar operaciones anteriores
# 7. Validar division por cero
# 8. break para salir

# Combina: while True, for, range, break, if/elif/else

print("\n ----------- CALCULADORA INTERACTIVA -------------- \n")

seleccion = 0
op = 1
historial = [] 

while seleccion != 6:

    print("\n -- MENU -- \n")

    menu = ["sumar", "restar", "multiplicar", "dividir", "historial", "salir"]
    cantidad_menu = len(menu)

    for i , accion in enumerate(menu, start=1):
        print(f"{i}. {accion}")
    print("\n")


    while True:
        
        seleccion = (input(f"Ingrese el numero de seleccion (1 - 6): "))
       
        if seleccion.isdigit() :  # Como puedo hacer la validacion de que lo que ingrese este entre 1 - 6 si es texto?
            seleccion = int(seleccion)
            if 0 < seleccion < 7:
                break
            else:
                print("\nError: El numero debe estar entre 1 y 6\n")
        else:
            print("\nError: El valor ingresado no es permitido dentro del listado\n")
            continue
    
    operacion = 0

    match seleccion:
        case 1:
            print("\nSUMA\n")
            
            cantidad_numeros = int(input("Digite la cantidad de numeros a Sumar = "))

            for i in range(1,cantidad_numeros+1):
                numeros = int(input("Digite el numero = "))
                operacion += numeros
            
            historial.append({  "op" : op,
                                "item": seleccion,
                                "nombre": menu[seleccion-1],
                                "resultado": operacion})

            print(f"\nLa suma de los {cantidad_numeros} numeros es igual a = {operacion}")
            op += 1
        case 2:
            print("\nRESTA\n")

            numero_1 = int(input("Digite el Numero 1 = "))
            numero_2 = int(input("\nDigite el Numero 2 = "))
            operacion = numero_1 - numero_2

            historial.append({  "op" : op,
                                "item": seleccion,
                                "nombre": menu[seleccion-1],
                                "resultado": operacion})

            print(f"\nLa resta entre {numero_1} y {numero_2} es igual a = {operacion}")
            op += 1
        case 3:
            print("\nMULTIPLICACION\n")

            numero_1 = int(input("Digite el Numero 1 = "))
            numero_2 = int(input("\nDigite el Numero 2 = "))
            operacion = numero_1 * numero_2

            historial.append({ "op" : op,
                               "item": seleccion,
                               "nombre": menu[seleccion-1],
                               "resultado": operacion})

            print(f"\nLa Multiplicacion entre {numero_1} y {numero_2} es igual a = {operacion}")
            op += 1
        case 4:
            print("\nDIVISION\n")

            numero_1 = int(input("Digite el Numero 1 = "))
            numero_2 = int(input("\nDigite el Numero 2 = "))
            operacion = numero_1 / numero_2

            historial.append({ "op" : op,
                               "item": seleccion,
                               "nombre": menu[seleccion-1],
                               "resultado": operacion})

            print(f"\nLa Division entre {numero_1} y {numero_2} es igual a = {operacion}")
            op += 1
        case 5:
            print("\nHISTORIAL\n")
            
            if not historial:
                print("No hay operaciones registradas")
            else:
                for h in historial:
                    print(
                        f"Op #{h['op']} | "
                        f"Item {h['item']} ({h['nombre']}) | "
                        f"Resultado: {h['resultado']}"
                    )
                #print(f"{historial}")
print("\n Saliendo el programa ... gracias \n")



