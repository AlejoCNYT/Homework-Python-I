'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.1. Calcular el área y el perímetro de un rectángulo cualquiera.

Entrada: Base y altura
Salida: Área y perímetro
'''

def areaPerRec():
    print("Este programa calcula el área y perímetro de un rectángulo, dada su base y altura lineales.")
    b = float(input("Digite la base del rectángulo: "))
    h = float(input("Digite la altura del rectángulo: "))
    area = b * h
    perimetro = 2 * b + (2 * h)
    print("El área del rectángulo de base", b, "y altura", h, "es:", round(area, 3), "unidades cuadradas aproximadamente.")
    print("Su perímetro es de", round(perimetro, 3), "unidades lineales aproximadamete.")
    print("El programa ha finalizado su tarea con éxito.")

areaPerRec()
