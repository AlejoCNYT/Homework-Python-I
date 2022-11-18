'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejercicios 1.
1.5. Calcular y escribir el área promedio de tres trapecios cualesquiera. Los datos de los trapecios se solicitarán al usuario.

Entrada: bases mayores, bases menores y altura de tres trapecios.
Salida: promedio de las areas de tres trapecios ingresados por el usuario.
'''
def prom3Trap():
    print("En este programa se calcula el promedio de las tres áreas de los trapecios ingresados por el usuario...")
    print("Para el primer trapecio ingrese...")
    b1 = float(input("La base menor: "))
    B1 = float(input("La base mayor: "))
    h1 = float(input("La altura: "))
    area1 = ((B1 + b1)/2) * h1
    print("El área del trapecio 1, de altura", h1, "base menor", b1, "y base mayor", B1, "es:", round(area1, 5))
    print("Para el segundo trapecio ingrese...")
    b2 = float(input("La base menor: "))
    B2 = float(input("La base mayor: "))
    h2 = float(input("La altura: "))
    area2 = ((B2 + b2)/2) * h2
    print("El área del trapecio 2, de altura", h2, "base menor", b2, "y base mayor", B2, "es:", round(area2, 5))
    print("Para el tercer trapecio ingrese...")
    b3 = float(input("La base menor: "))
    B3 = float(input("La base mayor: "))
    h3 = float(input("La altura: "))
    area3 = ((B3 + b3)/2) * h3
    print("El área del trapecio 3, de altura", h3, "base menor", b3, "y base mayor", B3, "es:", round(area3, 5))
    prom = round((area1 + area2 + area3)/3, 5)
    print("El promedio del área de los tres trapecios anteriores es de", prom)
    print("¡Vuelva pronto!")

prom3Trap()
    
