'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

3.  Solicitar a un usuario las coordenadas de n puntos en el plano cartesiano y dar como resultado la cantidad de puntos en cada cuadrante y cuántos están sobre los ejes.

Ejemplo.    Cantidad de puntos (n) igual a 11.
            Puntos dados:     (-2.5, 3.0) (-1.0, 0.0) (5.2, 3.7) (4.0, 3.1) (-2.0, -1.0) (0.0, 0.0)
                              (0.5, 0.5) (3.2, -2.6) (-1.5, -1.5) (0.0, -2.5) (4.4, 0.0)


Datos de entrada: n, x, y
Datos de salida: I, II, III, IV
'''

def main():
    print("Clasificación de puntos dentro de un plano cartesiano.")
    n = int(input("n = "))
    cont = 0
    cuadrante_uno = 0
    cuadrante_dos = 0
    cuadrante_tres = 0
    cuadrante_cuatro = 0
    eje = 0
    
    while cont < n:
        x = float( input ( "\nx = " ) )
        y = float( input ( "y = " ) )

        if x != 0 and y != 0:
            if x < 0:
                if y < 0:
                    cuadrante_tres = cuadrante_tres + 1
                else:
                    cuadrante_dos = cuadrante_dos + 1
            else:
                if y < 0:
                    cuadrante_cuatro = cuadrante_cuatro + 1                
                else:
                    cuadrante_uno = cuadrante_uno + 1
        else:
            eje = eje + 1            
            
        cont = cont + 1
    print("\nDe los", n, "puntos dados,", cuadrante_uno, "están ubicados en el cuadrante I,", cuadrante_dos, "en el II,", cuadrante_tres, "en el III y", cuadrante_cuatro, " en el IV. Los puntos sobre los ejes son", eje, ".")
    print("Los puntos han sido clasificados satisfactoriamente.")

main()
