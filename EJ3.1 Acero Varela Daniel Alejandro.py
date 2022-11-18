'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 10 de Junio de 2022
Lenguaje: Python 3.10.5

Ejercicio 3.1

Colombia es uno de los países en los que se ha manifestado últimamente una gran preocupación por la ingesta de
dulces y bebidas azucaradas, debido a su repercusión negativa en la salud y a la incidencia directa en los índices
de obesidad.

Con base en el Índice de Masa Corporal (IMC) se puede saber si una persona está baja de peso, tiene peso normal,
tiene sobrepeso o está obesa.

IMC = peso (en kilogramos) / estatura (en metros) elevada al cuadrado

      IMC            Estado de la persona
    < 18.5              Baja de peso
  [18.5,25.0)          Peso saludable
 [25.0, 30.0)            Sobrepeso
     ≥ 30.0              Obesidad

Permitir que una persona sepa si su peso es saludable o si está baja de peso, en sobrepeso u obesa, de acuerdo con
su IMC. Hay que calcular el IMC, decirle en qué estado se encuentra y por qué.

Datos de entrada: Peso y Estatura.
Datos de salida: IMC y Estado de la persona.
'''
def IMC():
    print("Calculo su IMC y le digo su estado de salud, en un instante.")
    print("Utilice el punto para los decimales.")
    peso = float(input("Escriba su peso en kilogramos: "))
    estatura = float(input("Escriba su estatura en metros: "))

    if estatura <= 0 and peso <= 0:
        print("La estatura", int(estatura), "m, ingresada, y el peso", int(peso), "kg, ingresado, no son válidos. Intente de nuevo.")    
    else:    
        if estatura <= 0:
            print("La estatura", int(estatura), "m, ingresada, no es válida. Intente de nuevo.")
        else:
            if peso <= 0 and estatura > 0:
                print("El peso", int(peso), "kg, ingresado, no es válido. Intente de nuevo.")
            else:
    
                IMC = peso / (estatura ** 2)
                IMC = round(IMC, 3)
    
                if IMC < 18.5:
                    print("\nSu IMC es", IMC, "kg / m^2, aproximádamente.")
                    print("Usted es una persona baja de peso.")
                else:
                    if IMC >= 18.5 and IMC < 25:
                        print("\nSu IMC es", IMC, "kg / m^2, aproximádamente.")
                        print("Su peso es saludable.")
                    else:
                        if IMC >= 25.0 and IMC < 30.0:
                            print("\nSu IMC es", IMC, "kg / m^2, aproximádamente.")
                            print("Usted tiene sobrepeso.")
                        else:
                            print("\nSu IMC es", IMC, "kg / m^2, aproximádamente.")
                            print("Usted tiene obesidad.")
                print("\nRecuerde mantener hábitos de vida saludables. Adiós.")

IMC()
