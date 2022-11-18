'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

1.  Averiguar si un número entero positivo dado por el usuario es múltiplo de otro, también ingresado por éste, haciendo únicamente sumas o restas.
Es decir, no puede usar los operadores de multiplicación o división.

Ejemplo 1.     Número dado: 42
        ¿Múltiplo de 5?
        Resultado. 42 no es múltiplo de 5.

Ejemplo 2.     Número dado: 60
        ¿Múltiplo de 12?
        Resultado. 60 es múltiplo de 12.

Ejemplo 3.     Número dado: 33
        ¿Múltiplo de 11?
        Resultado. 33 es múltiplo de 11.

Datos de entrada: num, mult
Datos de salida: validación
'''

def main ( ):
    print ("Averigüo si un número es múltiplo de otro.")
    num = int (input ("\nNúmero dado : "))
    mult = int (input ("¿múltiplo de?: ")) 
    if num > 0 and mult > 0: # Valida si los números suministrados por el usuario son positivos.
        dif = num - mult
        while dif > 0: # Mira si debe seguir haciendo la diferencia (dif) o no.
            dif = dif - mult
        if dif == 0:
            print (num, "es múltiplo de", mult, end = ".")
        else:
            print (num, "no es múltiplo de", mult, end = ".")
    else:
        print ("\nEl número ingresado no es un entero positivo.")
    print ("\nFin.")

main ( )   # Se invoca o llama la función para que se ejecute.
