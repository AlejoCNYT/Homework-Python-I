'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python 
Ref.: Ejercicios No. 6. Con vectores. 

5. Solicitar máximo 100 números reales y guardarlos en un vector.
   Luego, averiguar si la suma de los contenidos de las posiciones pares (0, 2,…)
   coincide con el producto de los contenidos de las posiciones impares.

   Vea más detalles en el PDF.

IMPORTANTE:
- El programa modular debe estar formado por mínimo cuatro funciones, 
  incluida la función principal main. 
  Los resultados los dará en una función aparte.
- Haré caso omiso de funciones que hagan lo pedido y no sean de su autoría.
- En la función main se debe ver claramente el plan de desarrollo de la solución del problema.
- Sólo debe utilizar lo que hemos visto en clase.
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
    print ("\nDatos del vector")
    for pos in range (0, tv):
        v [pos] = float (input ("Ingrese número entero "))
    return v

def suma_pares(v, n):
    sum_par = 0
    for pos in range(0, n, 2):
        sum_par = sum_par + v[pos]
    return sum_par

def producto_impares(v, n):
    prod_imp = 1
    for pos in range(1, n, 2):
        prod_imp = prod_imp * v[pos]
    return prod_imp

def escvec (v, tv):
    print (end = "\nEn el vector ")
    for pos in range (0, tv):
        print (v [pos], end = " ")

def resultados (sum_par, prod_imp, msj, vector, cant_num):
    escvec (vector, cant_num)
    if sum_par == prod_imp:
        coincide = "y coincide con el producto de los contenidos de las posiciones impares que es"
    else:
        coincide = "y no coincide con el producto de los contenidos de las posiciones impares que es"
    print (msj, sum_par, coincide, prod_imp, ".")
    print ("\n\nFin.\n")
    
def main ( ):
    print ("\nSolicita máximo 100 números reales.\n")
    cant_num = pide_ent_pos_msj ("Cantidad de números")
    vector = leevec_e (cant_num)
    adicion = suma_pares(vector, cant_num)
    producto = producto_impares(vector, cant_num)
    resultados (adicion, producto, "\nLa suma de los contenidos de las posiciones pares es", vector, cant_num)
    print ("\n\nFin.\n\n")
    
main ( )
