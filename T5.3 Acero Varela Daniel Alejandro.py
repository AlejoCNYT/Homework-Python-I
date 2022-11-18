'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Examen - Tercio 1. Estructuras de control condicional if y while.

UNIVERSIDAD ESCUELA COLOMBIANA DE INGENIERÍA
Asignatura: Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Fecha: 16 de junio de 2022.
Ref.: Tarea No. 5 (Examen – Tercio 1). Estructuras de control condicional if y while.
Cada archivo se debe llamar T5.# Apellidos Nombre, donde # será 2 o 3 según corresponda.
El archivo comprimido se debe llamar T5 Apellidos Nombre.
Les doy hecho el primero.
Construya un programa en Python (una función) que solucione cada uno de los siguientes
problemas:

3.  Conscientes de que el cuidado del medioambiente es responsabilidad de todos, separar la basura
    en la casa se está volviendo un hábito.
    Realizar y procesar una encuesta en la que se pida a n personas responder la pregunta ¿Usted
    separa la basura en su casa para facilitar su posterior reciclaje? Las personas responderán:

    1: sí lo hacen
    0: no lo hacen
    Cualquier otro número: no saben

    Se quiere saber cuántos separan la basura en la casa, cuántos no lo hacen y cuántos no saben si
    lo hacen. También, cuál respuesta primó (puede que ninguna).

    Un ejemplo de resultado sería:

    A la pregunta ¿Usted separa la basura en su casa para facilitar su posterior reciclaje?, los encuestados respondieron
    así:

    Sí: 60
    No: 48
    No saben: 12

    La cantidad de participantes fue 120 y la respuesta que primó fue Sí

    Datos de entrada: n, opcion
    Datos de salida: cont_si, cont_no, cont_ni_si_ni_no
'''

def pide_ent_pos_msj (que):
    n = -1	# Fuerza la entrada a la estructura while para que el valor sea solicitado por lo menos una vez.
    while n < 1:
        print (que, end = " ")
        n = int (input ( ))
    return n

def encuesta ( n ):
    cont_si = 0
    cont_no = 0
    cont_ni_si_ni_no = 0
    cont = 1
    while cont <= n:
        opcion = int ( input ( " Opción: ") )
        cont = cont + 1
        if opcion == 1:
            cont_si = cont_si + 1
        elif opcion == 0:
            cont_no = cont_no + 1
        else:
            cont_ni_si_ni_no = cont_ni_si_ni_no + 1 
    return cont_si, cont_no, cont_ni_si_ni_no

def resultados ( n, si, no, ni_si_ni_no ):
    print ( "\nA la pregunta ¿Usted separa la basura en su casa para facilitar su posterior reciclaje?", end = ", " )
    print ( "los encuestados respondieron así: " )
    print ( "\nSí: ", si )
    print ( "No: ", no ) 
    print ( "No saben: ", ni_si_ni_no )
    if si > no and si > ni_si_ni_no :
        print( "\nLa cantidad de participantes fue", n, "y la respuesta que primó fue Sí." )
    elif no > si and no > ni_si_ni_no :
        print( "\nLa cantidad de participantes fue", n, "y la respuesta que primó fue No." )
    elif ni_si_ni_no > si and ni_si_ni_no > no :
        print( "\nLa cantidad de participantes fue", n, "y la respuesta que primó fue No saben." )
    else:
        print( "\nLa cantidad de participantes fue", n, "y varias respuestas primaron sobre las demás." )

def main (  ):

    print( "Encuesta sobre reciclaje en casa." )
    print( "A la pregunta ¿Usted separa la basura en su casa para facilitar su posterior reciclaje? Responda: " )
    print( "\n1: Sí lo hacen" )
    print( "2: No lo hacen" )
    print( "Cualquier otro número: no saben" )
    
    n = pide_ent_pos_msj ("\nCantidad de encuestados (>0): ")
    cont_si, cont_no, cont_ni_si_ni_no = encuesta ( n )
    total = resultados ( n, cont_si, cont_no, cont_ni_si_ni_no )
    print ( "\n\nEncuesta finalizada.\n\n" )
    
main(  )
