print("\n ----------- SISTEMA DE ESTUDIANTES -------------- \n")

estudiantes = [] #Diccionario
historial_notas = []
lista_estudiantes_nombre = []
lista_estudiantes_aprobados = []
lista_mejores_estudiantes = []
lista_peores_estudiantes = []
mejor_promedio_estudiante = 0
peor_promedio_estudiante = 0
mejor_promedio = 0
peor_promedio = 0

def agregar_estudiante(nombre, calificaciones):  # Recibe el nombre del estudiante y la lista de notas

    print(f"Estudiante {nombre}\n")
    promedio = sum(calificaciones) / len(calificaciones)
    
    if promedio >= 70:
        status = "Aprobado"
    else:
        status = "No Aprobado"
        
    estudiantes.append({ "Nombre" : nombre, 
                        "Promedio" : promedio,
                        "Status" : status })

    print(f"{estudiantes}")

    return estudiantes

def obtener_aprobados(lista_estudiantes):

    for i in lista_estudiantes:
        if i["Promedio"] >= 70:
            lista_estudiantes_aprobados.append(i["Nombre"])

    return lista_estudiantes_aprobados

def mostrar_estadisticas(lista_estudiantes):
    
    conteo = 0
    Sumatoria_general = 0

    mejor_promedio_estudiante = max(lista_estudiantes, key=lambda e: e["Promedio"] )
    peor_promedio_estudiante = min(lista_estudiantes, key=lambda e: e["Promedio"] )

    mejor_promedio = mejor_promedio_estudiante["Promedio"]
    peor_promedio = peor_promedio_estudiante["Promedio"]

    for i in lista_estudiantes:
        Sumatoria_general += i["Promedio"] 
        conteo += 1

        lista_estudiantes_nombre.append(i["Nombre"])

        if i["Promedio"] == mejor_promedio:
            lista_mejores_estudiantes.append(i["Nombre"])

        if i["Promedio"] == peor_promedio:
            lista_peores_estudiantes.append(i["Nombre"])

    promedio_general = Sumatoria_general / conteo

    return promedio_general, mejor_promedio, peor_promedio


# Seleccionar la cantidad de estudiantes que desea ingresar 

cantidad_estudiantes = int(input("Digite la cantidad de estudiantes a ingresar = "))

# Ingresar la informacion de los estudiantes con nombre y calificaciones

for i in range(cantidad_estudiantes):
    
    lista_notas = [] 
    estudiante = (input(f"Digite el nombre del {i+1} estudiante = "))

    for notas in range(3):
        nota_estudiante = float(input(f"Digite la nota {notas+1} del estudiante = "))
        lista_notas.append(nota_estudiante)

    historial_notas.append(lista_notas)

    agregar_estudiante(estudiante,lista_notas)

obtener_aprobados(estudiantes)
mostrar_estadisticas(estudiantes)

print(f"\nEstudiante {estudiante}")
print(f"Notas {lista_notas}")
print(f"Historial de notas {historial_notas}")
print(f"Lista de estudiantes {lista_estudiantes_nombre}")
print(f"Lista de estudiantes aprobados {lista_estudiantes_aprobados}")
print(f"Lista de mejores estudiantes {lista_mejores_estudiantes}")
print(f"Lista de peores estudiantes {lista_peores_estudiantes}")
print(f"Lista de mejores estudiantes {mejor_promedio}")
print(f"Lista de peores estudiantes {peor_promedio}")