'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

2.  Suponga que la Asociación de Egresados de la Escuela Colombiana de Ingeniería (AECI),
    preocupada por la situación económica actual de algunos estudiantes,
    ha decidido darles un auxilio para la matrícula, de acuerdo con la siguiente tabla:

    | Porcentaje (%) auxilio | Condición |
    |         4 veces        | Semestre  |
 1  |  el semestre ponderado | ponderado |
    |     del estudiante     |   entre   |
 2  |           30           |   1 y 5   |


Calcular el valor de la matrícula promedio de esos n estudiantes de la Escuela
y el total de los auxilios que dará la AECI con el fin de proceder a la debida legalización.
Adicionalmente, hay que escribir para cada estudiante el valor del auxilio y el porcentaje al que corresponde.

Ejemplo.    Cantidad de estudiantes (n): 2

        Estudiante 1    Valor de la matrícula: $8’000,000
        Semestre ponderado del estudiante: 5
        Valor del auxilio: 1,600,000 (20%)

Estudiante 2    Valor de la matrícula: $6’600,000
            Semestre ponderado del estudiante: 7
            Valor del auxilio: 1,980,000 (30%)

El valor de la matrícula promedio de los estudiantes de la Escuela con problemas económicos es $7’300,000
y el total de los auxilios que dará la AECI es de $3’580,000.2. 

Datos de entrada: n, matricula, semestre
Datos de salida: valor_auxilios, promedio_matriculas, total_auxilios
'''

def main():
    print("Cálculo del presupuesto de auxilios escolares.")
    n = int(input(("n = ")))
    cont = 1
    total_matriculas = 0
    total_auxilios = 0
    valor_auxilio = 0
    while cont <= n: # Valida la cantidad de datos a ingresar
        matricula = int(input("\nMatrícula = "))
        semestre = int(input("Semestre = "))
        if semestre >= 1 and semestre <= 5: # Condición 1
            valor_auxilio = matricula * ((4 * semestre) / 100)
            print("Valor del auxilio: ", valor_auxilio, "(", 4 * semestre, "%)")
        else:
            if semestre >= 6 and semestre <= 10: # Condición 2
                valor_auxilio = matricula * 0.3
                print("Valor del auxilio: ", valor_auxilio, "(30%)")
            else:
                print("El semestre", semestre, "ingresado no es válido.")
        total_auxilios = total_auxilios + valor_auxilio
        total_matriculas = total_matriculas + matricula
        cont = cont + 1
        
    print("\nEl valor de la matrícula promedio de los estudiantes de la Escuela con problemas económicos es $", total_matriculas / n, "y el total de los auxilios que dará la AECI es de $", total_auxilios)
    print("¡Ya puedes retomar a tus estudios universitarios!")
        
main()
