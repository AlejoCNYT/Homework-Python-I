'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 10. Programación modular en Python con matrices. 

10.1    Inicializar por columnas una matriz de máximo 40 filas y 30 columnas con las primeras potencias del
        número que también ingresará el usuario. En los resultados se debe saber qué número dio el usuario.

        Ejemplo. Filas = 4, Columnas = 2, Potencias de 3

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

def pide_ent_pos ( ):
    n = -1	# Fuerza la entrada a la estructura while para que el valor sea solicitado por lo menos una vez.
    while n < 1:
        print ("\nIngrese un entero positivo", end = " ")
        n = int (input ( ))
    return n
    
def dim_mat (maxf, maxc):
      fil = pide_entero_interv_msj (1, maxf, "Filas")
      col = pide_entero_interv_msj (1, maxc, "Columnas")
      return [fil, col]

def inicmat (nf, nc, num):
      m = [[0 for c in range (nc)] for f in range (nf)]  # Crea la matriz.
      cont = 0
      for c in range (nc):
           for f in range (nf):
                m [f][c] = num ** cont
                cont = cont + 1
      return m

def escribe_mat (m, nf, nc, num):
      print ("\n\tMatriz con las prineras", nf * nc, "potencias de", num, "\n\n\t", end = " ")
      for f in range (nf):
           for c in range (nc):
               print (format (m [f][c], "2d"), end = " ")
           print ("\n\t", end = " ")    # Cambia de línea después de escribir una fila.
   
def main ( ):
      print ("\nInicializa una matriz por columnas con las primeras potencias de un número ingresado por el usuario\n")
      [fil, col] = dim_mat (MCF, MCC)
      num = pide_ent_pos ()
      matriz = inicmat (fil, col, num)
      escribe_mat (matriz, fil, col, num)
      print ("\nTarea finalizada.\n")

main ( )
