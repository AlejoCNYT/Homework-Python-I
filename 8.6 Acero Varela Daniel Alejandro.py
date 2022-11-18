'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 6. Con vectores. 

6.  Solicitar máximo 100 palabras y guardar en un vector las posiciones
    que contienen cierto valor que también indica el usuario.
    Tenga en cuenta que es posible que el valor no exista en el vector.

   Vea más detalles en el PDF.
'''

def pide_ent_pos_msj (que):
    print (que, "(>0 y <=100)", end = " ")
    n = int (input ( ))
    if n <= 0 or n > 100:
        print("Imposible trabajar con", n, "números.")
    else:           
        return n
    
def leevec_e (tv):
    v = [0 for pos in range (0, tv)] # Se crea el vector con impare y del tamaño que indique cant_num.
    print ("\nDatos del vector\n")
    for pos in range (0, tv):
        v [pos] = input ("Ingrese palabra ")
    return v

def ubicapos_vec (v, tv):
    v_pos = [0 for pos in range (0, tv)]
    palabra = input ("\nPalabra buscada ")
    for pos in range (0, tv):
        if palabra == v[pos]:
            v_pos[pos] = pos
    return v_pos

def datos_vec (msj, v, tv):
    print(msj, end = " ")
    for pos in range (0, tv):
        print (v [pos], end = " ")

def resultado (v, tv, vp, msj):
    datos_vec ("\nel vector contiene", v, tv)
    print(msj, "contiene la(s) palabra(s) en la(s) posicion(es)")
    
    
def main ( ):
    print ("\nIndico la(s) posicion(es) de una palabra en un vector.\n")
    cant_num = pide_ent_pos_msj ("\nCantida de palabras")
    vector = leevec_e (cant_num)
    vec_ubica = ubicapos_vec (vector, cant_num)
    resultado(vector, cant_num, vec_ubica, "\nEl vector")
    print ("\n\nFin.\n\n")
    
main ( )
