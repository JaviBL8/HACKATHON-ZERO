"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contrasena = "abcd"

user_password = input("Introduzca la contraseña: ")

if user_password.capitalize() == contrasena.capitalize():
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta")