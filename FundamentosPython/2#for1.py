'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas.
'''

num = int(input("Introduzca el número para realizar la cuenta atrás "))

for i in range(num, -1, -1):
    print(str(i) + " ")