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
        system ("cls")#LIMPIAR PANTALLA
        print("\n\t< MENU >")
        print("\n\n\t1. Portada ITT.")
        print("\n\t2. Cadenas.")
        print("\n\t3. Cuestionario.")
        print("\n\t4. Pregunta sencilla firma.")
        print("\n\t5. Impresión de un Cuadrado.")
        print("\n\t6. Pregunta sencilla con firma.")
        print("\n\t7. .")
        print("\n\t8.Cadenas. ")
        print("\n\t9. Dibujar cuadrado. ")
        print("\n\t10. Sistema de unidades.")
        print("\n\t11. Salir...")
        menu = int(input("\n\n\tOpcion: "))
        if menu == 1:

            return PortadaITT()

        elif menu == 2:

            Cadenas()
        
        elif menu == 3:

            Cuestionario()

        elif menu == 4:

            return PreguntaSencillaFirma()

        elif menu == 5:

            return
            
        elif menu == 6:

            return 

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
    system("cls")#LIMPIAR PANTALLA
    ps = input("\n\tPregunta sencilla.\n\n\tCual es tu nombre? ")
    input(f"\n\tTu nombre es: {ps}\n\tEnter para continuar.")
    menu()

# METODO CUESTIONARIO
def Cuestionario():
    system("cls")#LIMPIAR PANTALLA
    print("\n\tCuestionario")
    p1 = input("\n\tCual es tu nombre?")
    p2 = input("\n\tCual es tu edad?")
    p3 = input("\n\tCual es tu carrera?")
    p4 = input("\n\tCual es tu ciudad de origen?")
    p5 = input("\n\tCual es tu nacionalidad?")
    p6 = input("\n\tCual es tu comida favorita?")
    p7 = input("\n\tCual es tu canción favorita?")
    p8 = input("\n\tCual es tu sexo?")
    p9 = input("\n\tEres ingeniero?")
    p10 = input("\n\tEres estudiante?")
    print(f"\n\tTus respuestas fueron...    \n\n\tTu nombre es {p1}.    \n\tTu edad es {p2}.    \n\tTu carrera es {p3}.    \n\tTu ciudad de origen es {p4}.    \n\tTu nacionalidad es {p5}.    \n\tTu comida favorita es {p6}.    \n\tTu cancion favorita es {p7}.    \n\tTu sexo es {p8}.    \n\tTu {p9} eres un ingeniero.  \n\tTu {p10} eres un estudiante.")
    input("\n\n\tEnter para continuar.")
    menu()

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
