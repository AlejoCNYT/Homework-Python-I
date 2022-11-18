'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 8 de Junio de 2022
Lenguaje: Python 3.10.5

EJ2.2 Pedir un número entero positivo al usuario y averiguar si es múltiplo de otro entero positivo.

Datos de entrada: número 1, número 2
Datos de salida: validación
'''

def multiplo_de_entero_positivo():
    print("Hola. En este programa se verifica si un número entero positivo es múltiplo de otro número entero positivo...")    
    num1 = int(input("Primer número ingresado: "))
    num2 = int(input("Segundo número ingresado: "))
    if num1 > 0 and num2 > 0:
        if num1 % num2 == 0:
            print(num1, "sí es múltiplo de", num2, end = ".")
        else:
            print(num1, "no es múltiplo de", num2, end = ".")
    else:
        print("El número", num1, "y/o el número", num2, "no pertenece a los enteros positivos.")
    print(end = "¡Éxitos!")    
    
multiplo_de_entero_positivo()
