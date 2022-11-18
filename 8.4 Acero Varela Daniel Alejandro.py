'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Acero Varela Daniel Alejandro
Lenguaje: Python

6.3. Inicializar un vector con las primeras n potencias de 2.
'''

def pide_ent_pos_msj (que):
    n = -1	
    while n < 1:
        print (que, "(>0)", end = " ")
        n = int (input ( ))
    return n

def inivec_pot (n):
    num = [0 for pos in range (0, n)] # Se crea el vector con par y del tamaño que indique cant_num.
    print ("Primeras", n , end="-potencias de 2\n")
    for pos in range (0, n):
        num [pos] = 2 ** pos
    return num

def escvec (num, cant_num):
    for pos in range (0, cant_num):
        print (num [pos], end = " ")     # No cambia de línea y deja un espacio entre los números.  
           
def main ( ):
    print ("\nInicializo vector con las primeras n potencias de 2.")
    cant_num = pide_ent_pos_msj ("n = ") 
    num = inivec_pot (cant_num)
    escvec (num, cant_num)
    print ("\n\nFin.\n")

main ( )
