# ANALIZADOR DE TEXTO - FUNCIONES


print("\n ----------- ANALIZADOR DE TEXTO - FUNCIONES -------------- \n")

salida_texto = ""


def limpiar_texto(texto):

    salida_texto = texto.lower().strip()

    print(f"{salida_texto}")

    return salida_texto

def contar_palabras(texto):

    frecuencia = {}

    lista_palabras = texto.split()    # Divide la frase en palabras mediante los espacios " "
    cantidad_palabras = len(lista_palabras)

    print(f"{lista_palabras}, {cantidad_palabras}")

    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabras_mas_comun(dict_frecuencias):


    return 

def generar_reporte(texto):


    return 


input_texto = str(input(f"Ingrese el texto: "))



salida_texto = limpiar_texto(input_texto)
diccionario_palabras = contar_palabras(salida_texto)

print(f"{diccionario_palabras}")