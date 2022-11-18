'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 8 de Junio de 2022
Lenguaje: Python 3.10.5

EJ2.1 Solicitar al usuario un intervalo cerrado y un número real. Debe informar si el número está a la izquierda, a la derecha o si pertenece al intervalo.
Datos de entrada: a, b, r 
Datos de salida: ubicación del número real ingresado
'''

def ubica_real():
    print("¡Bienvenid@!...")
    print("Ubica un número entero ingresado, con relación a un intervalo...")
    a = int(input("Ingrese el número inicial del intervalo cerrado: "))
    b = int(input("Ingrese el número final del intervalo cerrado: "))
    print("El intervalo dado es [", a, ",", b, "].")
    r = float(input(("Ingrese el número real: ")))
    print("El número dado es: ", int(r))
    if r > a and r < b:
        print(int(r), "permanece en el intervalo[", a, ",", b, "].")
    else:
        if r > b and r > a:
            print(int(r), "está a la derecha del intervalo[", a, ",", b, "].")
        else:
            print(int(r), "está a la izquierda del intervalo[", a, ",", b, "].")
    print("Fin.")
ubica_real()
            
    
