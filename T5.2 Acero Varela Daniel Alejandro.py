'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Examen - Tercio 1. Estructuras de control condicional if y while.

2.  Se sabe que uno de los vértices de un triángulo es (0.0, 0.0). Solicite las coordenadas de los
    otros dos vértices que están sobre los ejes coordenados (suponga que así es), primero el que
    está sobre el eje de las abscisas y luego el que está sobre el eje de las ordenadas.

    Cuando el triángulo esté en el cuadrante:

    a. I: hallar y escribir el área.
    b. II: hallar y escribir la longitud de la hipotenusa.
    c. III: hallar y escribir el perímetro.
    d. IV: hallar y escribir la base y la altura.

    En cualquiera de los casos, debe decir en qué cuadrante está el triángulo.

    La distancia entre dos puntos 𝑃1(𝑥1, 𝑦1) y 𝑃2(𝑥2, 𝑦2) es ((𝑥2 − 𝑥1)2 + (𝑦2 − 𝑦1))**0.5

    Datos de entrada: x, y
    Datos de salida: cuadrante y operación
'''

def pide_coordenada (msj):
    print (msj)
    coordenada = float ( input (  ) )
    return coordenada

def clasifica (b, h):
    if b > 0:
        if h > 0:
            return ["I. Área del triángulo =", (b * h) / 2]
        else:
            return ["IV", b]
    else:
        if h > 0:
            return ["II. Longitud de la hipotenusa =", round((b ** 2 + h ** 2) ** 0.5, 1)]
        else:
            return ["III. Perímetro =", round(- h - b + (b ** 2 + h ** 2) ** 0.5, 1)] # La medida de la altura y de la base siempre deben ser positivas

def resultados (cuadrante, resultado, b, h):
    if cuadrante != "IV":
        print ("\n\nEl triángulo de coordenadas (", b, ", 0 ) y, ( 0 ,", h, "), se encuentra en el cuadrante", cuadrante, resultado, end = ".")
    else:
        print ("\n\nEl triángulo de coordenadas (", b, ", 0 ) y, ( 0 ,", h, "), se encuentra en el cuadrante", cuadrante, "del plano cartesiano.", end = " ")
        print ("Su base =", resultado, "y su altura =", - h, end = ".")    # La medida de la altura siempre debe ser positiva

def main():
    print ("Clasifico un triángulo en su respectivo cuadrante del plano cartesiano y, realizo la operación correspondiente: ")
    print ("\nPlano I: área del triángulo.")
    print ("Plano II: longitud de la hipotenusa.")
    print ("Plano III: perímetro.")
    print ("Plano IV: Base y altura.")
    x = pide_coordenada ("\nPor favor, ingrese la abscisa del punto sobre el eje x (x, 0), donde x: ")
    y = pide_coordenada ("Por favor, ingrese la ordenada del punto sobre el eje y (0, y), donde y: ")
    [cuadrante, resultado] = clasifica (x, y)
    resultados (cuadrante, resultado, x, y)
    print("\n\nFin.\n\n")

main()
