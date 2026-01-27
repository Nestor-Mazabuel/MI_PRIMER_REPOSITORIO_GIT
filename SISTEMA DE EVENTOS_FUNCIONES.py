# SISTEMA DE EVENTOS - FUNCIONES

print("\n ----------- FUNCIONES ARGUMENTOS - sistema de eventos -------------- \n")

data_base = []   # Se van almaceando los eventos

def registrar_evento(nombre, fecha, *participantes, **detalles):

    """
    Docstring for registrar_evento
    
    Se solicitan los parametros nombre y fecha
    El parametro participantes es *arg, se recibe como tupla
    El parametro detalles es **kwargs, se recibe como diccionario {item : value}
    
    Almacena el evento con los argumentos ingresados, y en cada llamado o uso
    de la funcion, se va almacenando en la base de datos "Database"
    """

    evento = {

        "Nombre" : nombre, 
        "Fecha": fecha,
        "Participantes" : participantes,
        "Detalles" : detalles

    }

    print(f"\n=========Evento========== \n")

    for item, valor in evento.items():
       print(f"{item} : {valor}")

    print(f"\n========================= \n")

    data_base.append(evento)

    return evento


def buscar_eventos_por(**filtros):

    for event in data_base:

        band = 1

        # Tener en cuenta que en la base de datos, cada evento tiene dos niveles
        # siendo el nivel dos el diccionario que compone la llave "Detalles"
        # Entonces hay que buscar dentro del nivel 1 y tambien el nivel 2

        for key, items in filtros.items():   
            # El event[key] accede a la llave del diccionario evento, y con esa forma 
            # (Eevent[key]) esta accediendo al item de esa llave, por eso se compara con el item del filtro
            if key in event and event[key] == items:  # Busqueda en nivel 1
                continue
            
            # el event["Detalles"] esta accediendo al valor que almacena la llave "Detalles" dentro de event
            # En este caso el valor de "Detalles" es otro diccionario, por ende busca inicialmente la llave Key del filtro dentro del diccionario "Detalles"
            # luego se necesita acceder a los items de cada llave dentro del diccionario "Detalles"
            # esto se hace con esto (event["Detalles"][key]), ya que inicialmente accede l diccionario detalles, y ya dentro de detalles, accede con Key a los items que contiene cada llave
            elif key in event["Detalles"] and event["Detalles"][key] == items: # Busqueda en nivel 2 dentro de detalles
                continue
            
            else:
                band = 0
                break
            
        if band == 1:
            #print(f"{event}")
            print(f"\n")

            for key, valor in event.items():
                print(f"{key} : {valor}")
            
            print(f"\n")
            
    return

def generar_reporte(*eventos):

    frecuencia_ubicaciones = {}
    cantidad_participantes = 0

    for evento in eventos:
        
        cantidad_participantes += evento["Detalles"]["participantes"]
        
        ubicacion = evento["Detalles"]["ubicacion"]

        if ubicacion in frecuencia_ubicaciones:
            frecuencia_ubicaciones[ubicacion] += 1
        else:
            frecuencia_ubicaciones[ubicacion] = 1

    for ubicacion, cantidad in frecuencia_ubicaciones.items():
        print(f"{ubicacion} : {cantidad}")
        
    for ubicacion, cantidad in frecuencia_ubicaciones.items():
        if cantidad == 1:
            print(f"ubicacion unica en = {ubicacion}")
    
    promedio_participantes = cantidad_participantes/len(eventos)

    print(f"\nLa cantidad total de participantes en los eventos fue : {cantidad_participantes}")
    print(f"El promedio de participantes fue : {promedio_participantes}")



    return 

evento1 = registrar_evento("Juan", "2026-01-26", "Andres", "Cristian", "Nestor", 
                           ubicacion = "Popayan", direccion = "Calle 10 # 50 - 52", tipo = "Tecnologia", capacidad = 100, participantes = 50)

evento2 = registrar_evento("Carlos", "2026-01-27", "Valentina", "Nestor", 
                           ubicacion = "Cali", direccion = "Calle 10 # 50 - 52", tipo = "Tecnologia", capacidad = 50, participantes = 40)

evento3 = registrar_evento("Sara", "2026-01-28", "Andres", "Cristian", "Nestor", 
                           ubicacion = "Cali", direccion = "Calle 10 # 50 - 52", tipo = "Negocios", capacidad = 100, participantes = 20)



print(f"\n=========FILTRO========== \n")

tecnologia = buscar_eventos_por(tipo="Tecnologia")

reporte = generar_reporte(evento1,evento2, evento3)

#print(f"{data_base}")