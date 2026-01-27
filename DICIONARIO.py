# DICIONARIO

# print("\n ----------- DICCIONARIO -------------- \n")

# persona = {"nombre": "Juan", "edad": 28, "ciudad": "Bogota"}  # Diccionario inicial

# persona["profesion"] = "Diseñador"   # estoy agregando una profesion al diccionario
# persona["edad"] = 29                 # Estoy cambiando la edad

# print("Keys:", list(persona.keys()))

# for keys, values in persona.items():
#     print(f"{keys}: {values}")


# print("\n ----------- DICCIONARIO - sets -------------- \n")

# lista = [1 , 2 , 2, 3 , 4, 4, 5, 5, 6]
# unicos = set(lista)

# print(f"Sin duplicados: {unicos}")

# pares = {2 , 4, 6, 8}
# impares = {1 , 3, 5, 7}

# print(f"Union: {pares | impares}")
# print(f"5 en impares: {5 in impares}")

print("\n ----------- FINAL -------------- \n")


productos_disponibles = ['Teclado', 'Mouse', 'Pantalla', 'Camisa','Camiseta','Fresa', 'Mora']   # La sintaxis es con [] - es Lista
  
categoria = ('Electronica','Ropa','Alimentos')    # La sintaxis es con () y no se pueden modificar - es Tupla

marca = ["Dell", 'Hp', 'Asus', 'Apple']
marca_unica = set(marca)

informacion_productos = {'Teclado' : {'precio' : 500 , 'categoria' : categoria[1]}  }    # Diccionario

inventario = {}

print(f"{informacion_productos}")

# Agregar producto

nombre = 'Laptop'
productos_disponibles.append(nombre)
inventario[nombre] = { "precio": 99999, 
                       "stock" : 2, 
                       "categoria" : categoria[0] }

marca_unica.add("Linux")

print(f"{inventario}")

# print(f"Sin duplicados: {unicos}")

# pares = {2 , 4, 6, 8}
# impares = {1 , 3, 5, 7}

# print(f"Union: {pares | impares}")
# print(f"5 en impares: {5 in impares}")
