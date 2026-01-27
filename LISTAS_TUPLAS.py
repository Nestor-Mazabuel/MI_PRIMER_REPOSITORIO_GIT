# LISTAS 

# print("\n ----------- LISTAS -------------- \n")

# Numeros = ['Uno','Dos','Tres','Cuatro']   # La sintaxis es con []
# print(f"{Numeros}")
# print(f"{Numeros[1]}")
# print(f"{Numeros[0:2]}")
# print(f"{len(Numeros)}")
# print(f"{Numeros,'Enteros','Reales'}")

# Numeros[0] = 'Cinco'  # Cambia el item de la posicion 0

# print(f"{Numeros}")

# Numeros.append('Seis')  # La funcion agrega items a la lista

# print(f"{Numeros}")

# reales = ['Siete','Ocho','Nueve']

# Numeros.append(reales)   # Agregamos a la lista lo que hay en la otra lista de reales siendo una lista

# print(f"{Numeros}")

# Numeros.extend(reales)   # Agregamos a la lista lo que hay en la otra lista como adicion a la lista

# print(f"{Numeros}")


# # TUPLAS

# print("\n ----------- TUPLAS -------------- \n")

# coordenadas = (20,30)                  # La sintaxis es con () y no se pueden modificar
# puntos_mapa = (1.5, -2.7, 30)

# # Unpacking   - desempaqueta la tupla, y almacena la informacion en una nueva variable

# x , y , z = puntos_mapa

# suma = abs(x) + abs(y) + abs(z)

# print(f"Variables de la tupla = {x , y , z}")
# print(f"Suma = {suma}")

# coordenadas[0] = 2


print("\n ----------- TUPLAS y LISTAS -------------- \n")



Lista = ['Juan','Camilo','Carlos','Sara','Valentina']   # La sintaxis es con [] - es Lista
    
Materias = ('Matematicas','Sociales','Fisica','Quimica')    # La sintaxis es con () y no se pueden modificar - es Tupla

# Unpacking   - desempaqueta la tupla, y almacena la informacion en una nueva variable

Lista.append("David")
Lista.remove("Juan")

print(f"La lista es\n")

for est in Lista:
    print(f"\n{est} cursa\n")
    for mat in Materias:
        print(f"{mat}")



