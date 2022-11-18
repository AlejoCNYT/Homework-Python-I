'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación, Grupo 1 (AYPR-1)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Fecha: 8 de Junio de 2022
Lenguaje: Python 3.10.5

EJ2.3 De acuerdo con el Ministerio de Salud, una persona está en una de estas etapas según su edad:

     Primera infancia [0-5 años]
     Infancia (5 - 11 años]
     Adolescencia (11-18 años]
     Juventud [14 - 26 años]
     Adultez (26 - 60 años)
     Vejez [60 años y más)
    
Pedir una edad y decir en qué etapa está la persona.

A algunas personas les molesta que los llamen viejos y a otros que les digan adolescentes en lugar
de jóvenes. Por tanto, si la persona tiene 60 años o más, se le dirá que está en la edad de plata.
Adicionalmente, primará joven sobre adolescente.

Datos de entrada: edad
Datos de salida: etapa
'''

def etapa_salud():
    print("Indique su edad y le diré a qué etapa pertenece.")
    edad = int(input("Diga su edad: "))
    if edad >= 60:
        print("Usted se encuentra en la edad de plata ¡Felicidades!.")
    else:
        if edad > 26 and edad < 60:
            print("¡Ya eres todo un adulto!")
        else:
            if edad >= 14 and edad <= 26:
                print("Usted es un(a) jóven.")
            else:
                if edad > 11 and edad <= 18:
                    print("Usted es, apenas, un adolescente.")
                else:
                    if edad > 5 and edad <= 11:
                        print("No hables con extraños, pequeñ@ infante.")
                    else:
                        if edad >= 0 and edad <= 5:
                            print("Su bebé está en la etapa de primera infancia.")
                        else:
                            print("¡Alerta de seguridad: un no humano ha entrado en la máquina!")
    print("Gracias por visitarnos. Vuelva pronto.")

etapa_salud()
                
