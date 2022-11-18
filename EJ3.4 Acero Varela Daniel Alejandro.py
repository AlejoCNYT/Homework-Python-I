'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 10 de Junio de 2022
Lenguaje: Python 3.10.5

Ejercicio 3.3

Hallar y escribir la suma de los n números ingresados por el usuario.
Ejemplo. n igual a 4
         Números dados: 100.8 24.0 -44.8 50.7

Resultado. La suma de los 4 números dados es 130.7

Datos de entrada: n, números
Datos de salida: suma
'''
def suma_numeros():
    print("Yo sumo números.")
    n = int(input("¿cuántos números desea ingresar? "))
    cont = 1
    suma = 0
    print("A continuación, ingrese los números...")
    while cont <= n:
        num = float(input("Diga el número: "))
        suma = suma + num
        cont = cont + 1

    print("La suma de los", n, "números dados es", round(suma, 1))
    print("Fin.")

suma_numeros()
