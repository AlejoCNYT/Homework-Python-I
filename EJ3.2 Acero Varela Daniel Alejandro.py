'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 10 de Junio de 2022
Lenguaje: Python 3.10.5

Ejercicio 3.2

Pedir al usuario las coordenadas de los tres vértices de un triángulo. Averiguar si el triángulo se encuentra en un
cuadrante, y decir en cuál, o en varios.

Ejemplo 1. Vértices: (-14.2, 9.2) (-4.0, 8.0) (-10.9, 1.4)
Resultado. El triángulo de vértices (-14.2, 9.2) (-4.0, 8.0) (-10.9, 1.4) se encuentra en el cuadrante II.

Ejemplo 2. Vértices: (-20.5, -10.0) (24.8, -18.0) (0.0, 12.8)
Resultado. Los vértices del triángulo ((-20.5, -10.0) (24.8, -18.0) (0.0, 12.8)) no están en un solo cuadrante.

Datos de entrada: v1, v2, v3
Datos de salida: cuadrante (s)
'''
def cuadrantes_triangulo():
    print("Le digo en cuál (es) cuadrantes está un triángulo.")
    vx1 = float(input("Ingrese el componente x del vértice 1: "))
    vy1 = float(input("Ingrese el componente y del vértice 1: "))
    vx2 = float(input("Ingrese el componente x del vértice 2: "))
    vy2 = float(input("Ingrese el componente y del vértice 2: "))    
    vx3 = float(input("Ingrese el componente x del vértice 3: "))
    vy3 = float(input("Ingrese el componente y del vértice 3: "))

    if vx1 > 0 and vy1 > 0 and vx2 > 0 and vy2 > 0 and vx3 > 0 and vy3 > 0:
        print("El triángulo de vértices (", vx1, ", ", vy1, "), (", vx2, ", ", vy2, "), (",  vx3, ", ", vy3, ") se encuentra en el cuadrante I.")
    else:
        if vx1 < 0 and vy1 < 0 and vx2 < 0 and vy2 < 0 and vx3 < 0 and vy3 < 0:
            print("El triángulo de vértices (", vx1, ", ", vy1, "), (", vx2, ", ", vy2, "), (",  vx3, ", ", vy3, ") se encuentra en el cuadrante III.")
        else:
            if vx1 < 0 and vy1 > 0 and vx2 < 0 and vy2 > 0 and vx3 < 0 and vy3 > 0:
                print("El triángulo de vértices (", vx1, ", ", vy1, "), (", vx2, ", ", vy2, "), (",  vx3, ", ", vy3, ") se encuentra en el cuadrante II.")
            else:
                if vx1 > 0 and vy1 < 0 and vx2 > 0 and vy2 < 0 and vx3 > 0 and vy3 < 0:
                    print("El triángulo de vértices (", vx1, ", ", vy1, "), (", vx2, ", ", vy2, "), (",  vx3, ", ", vy3, ") se encuentra en el cuadrante IV.")
                else:
                    print("Los vértices del triángulo ((", vx1, ", ", vy1, "), (", vx2, ", ", vy2, "), (",  vx3, ", ", vy3, ")) no están en un solo cuadrante.")
    #print("Fin.")
                
cuadrantes_triangulo()

'''
"El triángulo de vértices (", vx1, end = ", ", vy1, end = "), (" vx2, end = ", ", vy2, end = "), (",  vx3, end = ", ", vy3, end = ") se encuentra en el cuadrante III."

    if vx1 < 0:
        if vx2 < 0:

            if vx3 < 0:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("Ii y III.")
                        else:
                            print("II.")
            else:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("I, II, III y IV.")
                    else:
                        if vy3 < 0:
                            print("II, III y IV.")
                        else:
                            print("I, II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II, III y IV.")
                        else:
                            print("I, II y III.")
                    else:
                        if vy3 < 0:
                            print("I y II, III y IV.")
                        else:
                            print("I y II.")
        else:
            if vx3 < 0:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("Ii y III.")
                        else:
                            print("II.")
            else:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("I, III y IV.")
                    else:
                        if vy3 < 0:
                            print("I, III y IV.")
                        else:
                            print("I, II, III y IV.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("I, II, III y IV.")
                        else:
                            print("I, II y IV.")
                    else:
                        if vy3 < 0:
                            print("I y II, III y IV.")
                        else:
                            print("I y II.")
        if vx2 < 0:

            if vx3 < 0:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("Ii y III.")
                        else:
                            print("II.")
            else:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("I, II, III y IV.")
                    else:
                        if vy3 < 0:
                            print("II, III y IV.")
                        else:
                            print("I, II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II, III y IV.")
                        else:
                            print("I, II y III.")
                    else:
                        if vy3 < 0:
                            print("I y II, III y IV.")
                        else:
                            print("I y II.")
        else:
            if vx3 < 0:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("II y III.")
                        else:
                            print("II y III.")
                    else:
                        if vy3 < 0:
                            print("Ii y III.")
                        else:
                            print("II.")
            else:
                if vy1 < 0:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("III y IV.")
                        else:
                            print("I, III y IV.")
                    else:
                        if vy3 < 0:
                            print("I, III y IV.")
                        else:
                            print("I, II, III y IV.")
                else:
                    if vy2 < 0:
                        if vy3 < 0:
                            print("I, II, III y IV.")
                        else:
                            print("I, II y IV.")
                    else:
                        if vy3 < 0:
                            print("I y II, III y IV.")
                        else:
                            print("I y II.")

                
                
        
    else:
        if vx2 < 0:
            if vx3 < 0:
                print("El triángulo de vértices (", vx1, end = ", ", vy1, end = "), (" vx2, end = ", ", vy2, end = "), (",  vx3, end = ", ", vy3, end = ") se encuentra en el cuadrante III.")
            else:
                if vx3 < 0:
                    print("El triángulo de vértices (", vx1, end = ", ", vy1, end = "), (" vx2, end = ", ", vy2, end = "), (",  vx3, end = ", ", vy3, end = ") se encuentra en el cuadrante III.")
                else:
                    print("El triángulo de vértices (", vx1, end = ", ", vy1, end = "), (" vx2, end = ", ", vy2, end = "), (",  vx3, end = ", ", vy3, end = ") se encuentra en el cuadrante III.")


cuadrante_triangulos()
'''
