# COMPARACIONES

print("\n ----------- COMPARACIONES -------------- \n")

numero_1 = input("Digita el primer valor = ")
numero_1 = float(numero_1)

numero_2 = float(input("Digite el segundo valor = "))


print(f"\n{numero_1} == {numero_2}  ? - respuesta {numero_1 == numero_2} \n" )
print(f"{numero_1} != {numero_2}    ? - respuesta {numero_1 != numero_2} \n" )
print(f"{numero_1} > {numero_2}     ? - respuesta {numero_1 > numero_2} \n" )
print(f"{numero_1} < {numero_2}     ? - respuesta {numero_1 < numero_2} \n" )
print(f"{numero_1} >= {numero_2}    ? - respuesta {numero_1 >= numero_2} \n" )
print(f"{numero_1} <= {numero_2}    ? - respuesta {numero_1 <= numero_2} \n" )



print("\n ----------- VALIDACION DE PASSWORD -------------- \n")

password = input("Digite la contraseña, debe ser mayor a 8 caracteres y no puede ser 'password' ni '12345678' : ")
password = (password)

if (len(password) >= 8) and (password != 'password') and (password != '12345678') :
    print(f"\n La contraseña es valida? { (len(password) >= 8) and (password != 'password') and (password != '12345678') }")
else:
    print(f"\n La contraseña es valida? { (len(password) >= 8) and (password != 'password') and (password != '12345678') }")
    