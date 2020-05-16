'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser
fresca y el coste final total.
'''

barra_de_pan = 3.49
descuento = 0.4
precio_con_descuento = barra_de_pan * descuento

numero_de_barras = int(input("Introduce en número de barras vendidas "))

print("Precio habitual de una barra " + str(barra_de_pan))
print("Descuento " + str(precio_con_descuento))
print("Coste fin " + str(numero_de_barras * precio_con_descuento))