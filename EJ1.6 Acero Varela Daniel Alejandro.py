'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.6.  Pedir al usuario un número real y guardar la parte entera en una variable y la parte decimal en otra. Mostrar los tres datos al usuario con un mensaje claro y conciso.

Entrada: número real.
Salida: parte entera, parte decimal y valor real.
'''

def divParteNum():
    print("Este programa separa la parte decimal y la parte entera de un número real para mostrarlas por separado.")
    num = float(input("Ingrese el número real: "))
    z = int(num)
    dec = float(num - z)
    print("El número real es", num)
    print("El valor entero del número es", z)
    print("El valor decimal del número es", round(dec, 4))
    print("No olvides darnos tu opinión.")

divParteNum()
