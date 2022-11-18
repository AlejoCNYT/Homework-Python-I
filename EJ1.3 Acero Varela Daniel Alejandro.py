'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.3. Calcular y escribir la pendiente de una recta, dados dos puntos que pertenecen a ella. Suponga que la recta no es vertical.

Entrada: x1, x2, y1, y2
Salida: pendiente
'''

def m():
    print("Este programa calcula la pendiente de una recta, que no es vertical, dados dos de sus puentos.")
    x1 = float(input("Ingrese la componente equis del punto inicial: "))
    y1 = float(input("Ingrese la componente ye del punto inicial: "))
    x2 = float(input("Ingrese la componente equis del punto final: "))
    y2 = float(input("Ingrese la componente ye del punto final: "))
    m = round((y2 - y1)/(x2 - x1), 3)
    print("El valor de la pendiente con punto inicial (", x1, ",", y1, ") y punto final (", x2, ",", y2, ") es", m, "aproximadamente.")
    print("Cálculo realizado, vuelva pronto.")

m()
