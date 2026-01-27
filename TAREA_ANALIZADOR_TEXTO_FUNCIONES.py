# ANALIZADOR DE TEXTO - FUNCIONES


print("\n ----------- ANALIZADOR DE TEXTO - FUNCIONES -------------- \n")

salida_texto = ""


def limpiar_texto(texto):

    print("\nFUNCION LIMPIAR TEXTO *************\n")

    salida_texto = texto.lower().strip()

    print(f"{salida_texto}")

    return salida_texto

def contar_palabras(texto):

    print("\nFUNCION CONTAR PALABRAS  *************\n")

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
    
    print("\nFUNCION PALABRA MAS COMUN ************* \n")
    
    palabras_mas_comun = None
    frecuencia_maxima = 0
    
    for palabra, frecuencia in dict_frecuencias.items():
               
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            palabras_mas_comun = palabra

    print(f"{palabras_mas_comun} : {frecuencia_maxima}")

    return (palabras_mas_comun, frecuencia_maxima)

def generar_reporte(texto):

    print("\nFUNCION GENERAR REPORTE ************* \n")

    reporte ={}

    texto_limpio = limpiar_texto(texto)

    reporte["Texto_Limpio"] = texto_limpio

    dict_contar_palabras = contar_palabras(texto_limpio)

    for item, value in diccionario_palabras.items():
        reporte[item] = value

    key_comun , item_comun = palabras_mas_comun(dict_contar_palabras)

    reporte["Palabra_mas_comun"] = key_comun
    reporte["Frecuencia_palabra_mas_comun"] = item_comun

    print(f"\n{reporte}")

    return reporte


input_texto = str(input(f"Ingrese el texto: "))



salida_texto = limpiar_texto(input_texto)

diccionario_palabras = contar_palabras(salida_texto)
print(f"{diccionario_palabras}")

frecuencia_palabra = palabras_mas_comun(diccionario_palabras)

reporte_1 = generar_reporte(input_texto)

#print(f"{frecuencia_palabra}")