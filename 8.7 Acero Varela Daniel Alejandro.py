'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 6. Con vectores. 

7.  Hallar la edad promedio de n personas. Lo vimos en clase, sin vectores.
'''

def pide_ent_pos_msj (que):
    n = -1	
    while n < 1:
        print (que, "(>0)", end = " ")
        n = int (input ( ))
    return n

def leedad_vec (n):
    v = [0 for pos in range (0, n)]
    for pos in range (n):
        print ("Edad de la persona", pos + 1, end = " ")
        edad = int ( input ())
        v[pos] = edad
    return v
    
def calcula_edad_prom (n, v):
    suma_e = 0
    for edad in range(0, n):
        suma_e = suma_e + v[edad]
    return suma_e // n

def escvec (v, tv):
    print ("\nEn el vector ", end = " ")
    for pos in range (0, tv):
        print (v [pos], end = " ")
        
def resulta (prom, v, tv):
    print ( "\nDadas las edades", end = " ")
    escvec (v, tv)
    print ( ". La edad promedio de las", tv, "edades es", prom, end = ".")    
    
def main ( ):
    print ("\nCalculo la edad promedio de varias personas.\n")
    n = pide_ent_pos_msj ("\n¿cuántas personas son?")
    vec_edad = leedad_vec(n) 
    prom = calcula_edad_prom (n, vec_edad)
    resulta (prom, vec_edad, n)
    print ("\nFin.")
    
main ( )
