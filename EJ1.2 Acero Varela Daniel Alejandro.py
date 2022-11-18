'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.1. Calcular y escribir el área de un círculo, definido por el usuario, y el perímetro de su circunferencia.

Entrada: Radio
Constante: Pi
Salida: Área y perímetro
'''

def areaPerCirc():
    print("Este programa calcula el área de un círculo y el perímetro de su circunferencia, asignando un valor al radio.")
    pi = 3.1415
    r = float(input("Ingrese el radio en unidades lineales: "))
    area = pi * (r ** 2)
    perimetro = 2 * pi * r
    print("El área del círculo es", round(area, 3), "unidades cuadradas aproximadamente.")
    print("El perímetro del círculo es", round(perimetro, 3), "unidades lineales aproximadamente.")
    print("El programa ha finalizado su función !Éxitos¡")

areaPerCirc()
