'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

4.  Solicitar n números enteros al usuario y hacer lo siguiente:

Escribir los números que son el cuadrado del anterior número ingresado (penúltimo), en la forma que se muestra en el ejemplo.
Escribir la cantidad de números que eran el cuadrado del anterior.

Ejemplo 1:  n igual a 10
            Números dados: 13  -5  25  8  1  1  4  16  256  -2
        
            Resultado.

                    25 = -5 X -5
                    1 = 1 X 1
                    16 = 4 X 4
                    256 = 16 X 16
        
            De los 10 números dados, 4 cumplieron la condición de ser el cuadrado del anterior.

Ejemplo 2:  n igual a 5
            Números dados: 7  -4  -16  8  2
        
            Resultado.     De los 5 números dados, 0 cumplieron la condición de ser el cuadrado del anterior.

Datos de entrada: n, num
Datos de salida: cuadrado
'''

def main():
    print("Números cuadrados del anterior.")
    n = int ( input (" n = " ) )
    numero = int ( input (" número = ") )
    cont = 1
    cant = 0

    while cont < n:
        cont = cont + 1
        anterior = numero
        numero = int ( input(" número = ") )
        if anterior * anterior == numero:
            print(numero, "=", anterior, "x", anterior)
            cant = cant + 1
    print("De los", n, "números dados,", cant, "cumplieron la condición de ser el cuadrado del anterior.")
    print("Fin.")

main()
