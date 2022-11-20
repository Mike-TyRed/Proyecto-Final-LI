#-------------------------- IMPORTACIONES -----------------------
import getpass
from os import system
#--------------------------- ASIGNACIONES -----------------------
v_password = ( '123' , 'hola' , 'Soy1humano?')
v_user = ('moy' , 'aranza' , 'miguel')
#---------------------------- FUNCIONES ------------------------
# METODO DE ACCESO TIPO LOGIN
def acceso():
    
    while True:
        system ("cls")#LIMPIAR PANTALLA
        print("\n\tInicio de secion")
        user = str(input("\n\t\tUsuario: "))
        if user in v_user :
            password = getpass.getpass("\n\t\tContraseña: ")
            if password in v_password :
                print(f"\n\tBienvenido usuario {user} ...")
                break
            else:
                input("\n\tcontraseña incorrecta.\n\tEnter para continuar...")
        else:
            input("\n\tUsuario incorrecto.\n\tEnter para continuar...")
    input("\n\tEnter para continuar...")
    menu()

# METODO DE MENU
def menu():
    while True:
        system ("cls")#LIMPIAR PANTALLAm
        menu = int(input("\n\t< MENU >\n\n\t1. Portada ITT.\n\t2. Programa de comparación lógica utilizando variables.\n\t3. Operaciones matemáticas.\n\t4. Sistema de unidades.\n\t5. Impresión de un Cuadrado.\n\t6. Pregunta sencilla con firma.\n\t7. Cuestionario.\n\t8.Cadenas. \n\t9. Dibujar cuadrado. \n\t10. Sistema de unidades. \n\t11. Salir..."))
        if menu == 1:

            return PortadaITT()

        elif menu == 2:

            return
        
        elif menu == 3:

            return

        elif menu == 4:

            return

        elif menu == 5:

            return

        elif menu == 6:

            return PreguntaSencillaFirma()

        elif menu == 7:

            return Cuestionario()

        elif menu == 8:

            return Cadenas()

        elif menu == 9:

            return Cuadrado()

        elif menu == 10:
                
            return SistemaUnidades()

        elif menu == 11:
            break

# METODO PREGUNTA SENCILLA FIRMACuestionario8.	Cadenas
def PreguntaSencillaFirma():
    return

# METODO CUESTIONARIO
def Cuestionario():
    return

# METODO CADENAS
def Cadenas():
    return

# METODO PORTADA ITT
def PortadaITT():
    system ("cls")
    print("""
                   TECNOLOGICO NACIONAL DE MEXICO
                  INSTITUTO TECNOLOGICO DE TIJUANA
                      SUBDIRECCION ACADEMICA
               DEPARTAMENTO DE SISTEMAS Y COMPUTACION
               INGENIERIA EN SISTEMAS COMPUTACIONALES
               
                    AGOSTO - DICIEMBRE 2022
                    
                            MAESTRO
                     CAÑEZ VALLE RODRIGO
                     
                            MATERIA
                     LENGUAJE DE INTERFAZ
                     
                            ALUMNO(S)
                      GUTIERREZ MORA ARANZA
                    SANDOVAL VALTIERRA MOISES
                   TERRAZAS ROJO MIGUEL ARTURO""")
    input("\n\tEnter para continuar...")
    menu()

def Cuadrado():
    system ("cls")
    print("""    -------------------------------------
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    -------------------------------------""")
    input("\n\tEnter para continuar...")
    menu()

# METODO SISTEMA DE UNIDADES
def SistemaUnidades():
    system ("cls")
    x = int(input("Ingresa un número: "))
    print("\n\tUnidades: " + str(x * 1))
    print("Decenas: " + str(x * 10))
    print("Centenas: " + str(x * 100))
    print("Millares: " + str(x * 1000))
    print("Decenas de millar: " + str(x * 10000))
    print("Centenas de millar: " + str(x * 100000))
    print("Millones: " + str(x * 1000000))
    input("\n\tEnter para continuar...")
    menu()

#----------------------------- LLAMADAS ------------------------
acceso()
