# METODOS

print("\n ----------- METODOS -------------- \n")

texto = input("Ingrese su nombre completo: ")
texto = (texto)

print(f"\nTexto en mayuscula = {texto.upper()} \n" )
print(f"Texto en minuscula = {texto.lower()} \n" )
print(f"Texto en Capitaliza las palabras o en fotmato de titulo = {texto.title()} \n" )
print(f"Texto en con primera letra en mayuscula = {texto.capitalize()} \n" )
print(f"Texto quita espacios = {texto.lstrip()} \n" )
print(f"Texto sin espacios = {texto.strip()} \n" )


print(f"Texto sin espacios = {texto.strip().upper()} \n" )

# Nestor David Mazabuel Ortiz

email = input("Ingrese su email: ")
email = (email)


print(f"Texto sin espacios = {email.find('@')} \n" )
print(f"Texto sin espacios = {email.count('@')} \n" )

