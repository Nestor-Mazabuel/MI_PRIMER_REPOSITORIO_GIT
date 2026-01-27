# FUNCIONES ARGUMENTOS DEFOULT

print("\n ----------- FUNCIONES ARGUMENTOS DEFAULT -------------- \n")

def crear_perfil(nombre, edad, ciudad="Desonocida", activo = True):

    """ Se crea la funcion, nombre y edad son obligatorios, ciudad y activo tienen el valor por Default """

    return{
        "Nombre" : nombre,
        "Edad" : edad,
        "Ciudad" : ciudad,
        "Activo" : activo
    }


perfil1 = crear_perfil("Ana" , 32)

perfil2 = crear_perfil("Juan" , 25, "Madrid", False)

print(f"{perfil1}")
print(f"{perfil2}")


# FUNCIONES + *Arg

print("\n ----------- FUNCIONES - PARAMETROS DEFOUT Y *ARG -------------- \n")

def calcular_total( descuento = 0, *productos):

    """ Se genera la funcion para calcular el total de los productos, se deben ingresar los precios de cada producto como primer parametro, y como ultimo el valor del descuento
      en caso de no agregar valor al descuento, no sera tenido en cuenta o descuento = 0  """

    subtotal = sum(productos)
    descuento_porcentaje = descuento/100

    total = subtotal - (subtotal*descuento_porcentaje)

    return {
        "subtotal" : subtotal,
        "descuento_aplicado" : descuento,
        "total" : total
    }

def generar_ticket(nombre_cliente,descuento=10,*productos):

    """ Se genera la funcion para generar tickets, se ingresa el nombre del cliente, se deben ingresar los precios de cada producto como parametro, y como ultimo el valor del descuento
    en caso de no agregar valor al descuento, no sera tenido en cuenta o descuento = 10  """

    subtotal = sum(productos)
    descuento_porcentaje = descuento/100
    valor_descuento = subtotal*descuento_porcentaje

    total = subtotal - valor_descuento

    ticket = {"Ciente" : nombre_cliente,
        "Productos" : productos,
        "subtotal" : subtotal,
        "descuento" : valor_descuento,
        "total": total}

    print(f"\n=========Ticket========== \n")

    for parametro, item in ticket.items():
       print(f"{parametro} : {item}")
    
    #print(f"{ticket}")

    print(f"\n========================= ")

    return ticket


compra1 = calcular_total(50, 10000,20000,30000,50)

print(f"El valor de la compra 1 es = {compra1} ")

compra_ticket = generar_ticket("Juan" , 50 , 50, 60 , 60 )