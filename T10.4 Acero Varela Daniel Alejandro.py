'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 10. Programación modular en Python con matrices. 

10.4    Pedir los datos enteros de una matriz y luego, hallar el mayor de los números que sean positivos y pares.
        Puede que no haya ninguno. En los resultados debe escribir los datos de entrada.

        Ejemplo. Filas = 4, Columnas = 5

        Ver más detalles en el pdf.

        Resultado. Además de la matriz, decir que el mayor de los números positivos y pares es 88.
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
      print ("\nPor favor, ingrese los números de la matriz\n\n")
      m = [[0 for c in range (nc)] for f in range (nf)]  # Crea la matriz.
      for f in range (nf):
           for c in range (nc):
                m [f][c] = int ( input ("\t#:"))
      return m

def maypospar_mat (m, nf, nc):
    num = -1
    for f in range (nf):
        for c in range (nc):
            if m [f][c] > num and m [f][c] % 2 == 0:
                num = m [f][c]
    return num

def resultados (m, nf, nc, num):
    print ("\nEn la matriz\n")
    escribe_mat (m, nf, nc)
    if num >= 0:
        print ("\nel mayor de los números positivos y pares es", num, end = ".")
    else:
        print ("\nno hay números positivos y pares.")

def escribe_mat (m, nf, nc):
      for f in range (nf):
           for c in range (nc):
               print (format (m [f][c], "2d"), end = " ")
           print ("\n\t", end = " ")    # Cambia de línea después de escribir una fila.
   
def main ( ):
      print ("\nInicializa una matriz por columnas con las primeras potencias de un número ingresado por el usuario\n")
      [fil, col] = dim_mat (MCF, MCC)
      matriz = inicmat (fil, col)
      mayorpospar = maypospar_mat (matriz, fil, col)
      resultados (matriz, fil, col, mayorpospar)
      print ("\nTarea finalizada.\n")

main ( )
