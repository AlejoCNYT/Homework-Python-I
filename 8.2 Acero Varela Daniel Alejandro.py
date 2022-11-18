'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Acero Varela Daniel Alejandro
Lenguaje: Python

6.2. Inicializar un vector con los primeros n números impares.
'''

def pide_ent_pos_msj (que):
    n = -1	
    while n < 1:
        print (que, "(>0)", end = " ")
        n = int (input ( ))
    return n

def inivec_e (n):
    num = [0 for pos in range (0, n)] # Se crea el vector con impare y del tamaño que indique cant_num.
    print ("\nNúmeros impares\n")
    impar = 1
    for pos in range (0, n):
        num [pos] = impar
        impar = impar + 2
    return num

def escvec (num, cant_num):
    for pos in range (0, cant_num):
        print (num [pos], end = " ")     # No cambia de línea y deja un espacio entre los números.  
           
def main ( ):
    print ("\nInicializo vector con los primeros n impares.")
    cant_num = pide_ent_pos_msj ("Cantidad de números") 
    num = inivec_e (cant_num)
    escvec (num, cant_num)
    print ("\n\nFin.\n")

main ( )
