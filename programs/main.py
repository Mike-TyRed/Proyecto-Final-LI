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
        menu = int(input("\n\t< MENU >\n\n\t1. Programa Menú.\n\t2. Programa de comparación lógica utilizando variables.\n\t3. Operaciones matemáticas.\n\t4. Sistema de unidades.\n\t5. Impresión de un Cuadrado.\n\t6. Pregunta sencilla con firma.\n\t7. Cuestionario.\n\t8.Cadenas."))
        if menu == 1:

            return 

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

# METODO PREGUNTA SENCILLA FIRMACuestionario8.	Cadenas
def PreguntaSencillaFirma():
    return

# METODO CUESTIONARIO
def Cuestionario():
    return

# METODO CADENAS
def Cadenas():
    return

#----------------------------- LLAMADAS ------------------------

acceso()
