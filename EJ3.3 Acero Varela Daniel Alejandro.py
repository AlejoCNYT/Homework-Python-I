'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 10 de Junio de 2022
Lenguaje: Python 3.10.5

Ejercicio 3.3

Escribir los primeros n números impares.
Ejemplo. n igual a 7
Resultado. Los primeros 7 números pares son: 1 3 5 7 9 11 13 15

Datos de entrada: n
Datos de salida: impares
'''
def impares_n():
    print("Muestro los primeros números pares hasta un número.")
    n = int(input("¿Cuál es el número? "))
    impar = 1
    while impar <= n:
        print(impar)
        impar = impar + 2

    print("\nGracias por visitarnos.")

impares_n()
