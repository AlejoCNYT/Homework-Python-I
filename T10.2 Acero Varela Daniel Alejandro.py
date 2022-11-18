'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 10. Programación modular en Python con matrices. 

10.2    Inicializar por filas una matriz con los números desde el producto de filas y columnas hasta 1, en orden
        descendente.

        Ejemplo. Filas = 4, Columnas = 5

        Ver más detalles en el pdf.
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
      matriz = [[0 for c in range (nc)] for f in range (nf)]  # Crea la matriz.
      num = nf * nc
      for f in range (nf):
           for c in range (nc):
                matriz [f][c] = num
                num = num - 1
      return matriz

def escribe_mat (m, nf, nc):
      print ("\n\tMatriz con", nf * nc, "valores, en orden descendente, hasta 1:\n\n\t", end = " ")
      for f in range (nf):
           for c in range (nc):
               print (format (m [f][c], "2d"), end = " ")
           print ("\n\t", end = " ")    # Cambia de línea después de escribir una fila.
   
def main ( ):
      print ("\nInicializa una matriz por filas con el producto de filas*columnas hasta 1.\n")
      [fil, col] = dim_mat (MCF, MCC)
      matriz = inicmat (fil, col)
      escribe_mat (matriz, fil, col)
      print ("\nTarea finalizada.\n")

main ( )
