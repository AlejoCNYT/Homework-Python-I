'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 10. Programación modular en Python con matrices. 

10.3    Pedir los datos reales de una matriz y luego, calcular el producto de los números que están guardados en
        las posiciones de la matriz con fila impar (1, 3,...) y columna par (0, 2, ...). En los resultados debe escribir
        los datos de entrada.

        Ejemplo. Filas = 3, Columnas = 5

        Ver más detalles en el pdf.

        Resultado. Además de la matriz, decir que el producto de de los números que están guardados en las
        posiciones de la matriz con fila impar (1, 3,...) y columna par (0, 2, ...) es 632.1.
'''

MCF = 40	# Máxima cantidad de filas.
MCC = 30	# Máxima cantidad de columnas.

def pide_entero_interv_msj (linf, lsup, mensaje):
    num = linf - 1
    while num < linf or num > lsup:
        print (mensaje, "(entre", linf, "y", lsup, ")", end = " ")
        num = int (input ( ))
    return num
 
def dim_mat (maxf, maxc):
      fil = pide_entero_interv_msj (1, maxf, "Filas")
      col = pide_entero_interv_msj (1, maxc, "Columnas")
      return [fil, col]

def inicmat (nf, nc):
      print ("\nPor favor, ingrese la matriz\n")
      m = [[0 for c in range (nc)] for f in range (nf)]  # Crea la matriz.
      for f in range (nf):
           for c in range (nc):
                m [f][c] = float (input ("\t#: "))
      return m

def calcprod_mat (m, nf, nc):
      prod = 1
      for f in range (1, nf, 2):
          for c in range (0, nc, 2):
                  prod = prod * m [f][c]
      return prod

def resultados (m, nf, nc, p):
      print ("\nEn la matriz\n\n\t", end = "")
      escribe_mat (m, nf, nc)
      print ("\nel producto de de los números que están guardados en las posiciones de la matriz con fila impar (1, 3,...) y columna par (0, 2, ...) es", p, end = ".\n")

def escribe_mat (m, nf, nc):
      for f in range (nf):
           for c in range (nc):
               print (m [f][c], end = " ")
           print ("\n\t", end = " ")    # Cambia de línea después de escribir una fila.
       
def main ( ):
      print ("\nInicializa una matriz por filas y calcula el producto de los valores ingresados en las filas impares y columnas pares.\n")
      [fil, col] = dim_mat (MCF, MCC)
      matriz = inicmat (fil, col)
      producto = calcprod_mat (matriz, fil, col)
      resultados (matriz, fil, col, producto)
      print ("\n\nTarea finalizada.\n")

main ( )
