'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Acero Varela Daniel Alejandro
Lenguaje: Python

6.3. Inicializar un vector con los primeros n números pares en orden descendente.
'''

def pide_ent_pos_msj (que):
    n = -1	
    while n < 1:
        print (que, "(>0)", end = " ")
        n = int (input ( ))
    return n

def inivec_par (n):
    num = [0 for pos in range (0, n)] # Se crea el vector con par y del tamaño que indique cant_num.
    print ("\nNúmeros pares\n")
    par = 2
    for pos in range (0, n):
        num [n - pos - 1] = par
        par = par + 2
    return print(num)

def escvec (num, cant_num):
    for pos in range (0, cant_num):
        print (num [pos], end = " ")     # No cambia de línea y deja un espacio entre los números.  
           
def main ( ):
    print ("\nInicializo vector con los primeros n pares en orden descendente.")
    cant_num = pide_ent_pos_msj ("Cantida de números.") 
    num = inivec_par (cant_num)
    escvec (num, cant_num)
    print ("\n\nFin.\n")

main ( )
