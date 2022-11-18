'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.4.  Calcular y escribir las coordenadas de los puntos de corte con los ejes coordenados de la recta ingresada por el usuario en la forma 𝑦 = 𝑚𝑥 + 𝑏. Suponga que la recta siempre los
corta (es decir, no será una recta vertical u horizontal). En los resultados debe escribir la recta que ingresó el usuario y las coordenadas de los puntos de corte.

Entrada: punto de corte con el eje y (b) y, pendiente.
Salida: coordenadas de los puntos de corte y recta
'''
def puntosCorte():
    print("Este programa calcula las coordenadas de los puntos de corte de una recta ingresada por el usuario, siempre que esta no sea horizontal ni vertical.")
    m = float(input("Ingrese la pendiente de la recta: "))
    b = float(input("Ingrese el punto de corte con el eje y: "))
    print("La recta ingresada por el usuario es y = (", m, "* x ) +", b)
    x = -(b / m)
    y2 = b
    print("La coordenada de corte con el eje y es ( 0 ,", y2, ") y la coordenada de corte con el eje x es (", x, ", 0 ).")
    print("Espero, le halla sido de ayuda.")
    print("Fin.")

puntosCorte()
