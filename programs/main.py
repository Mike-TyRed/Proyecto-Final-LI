#-------------------------- IMPORTACIONES -----------------------
import os
import sys
import getpass
from numpy import array
from numpy import* 
#--------------------------- ASIGNACIONES -----------------------
v_password = ( '123' , 'hola' , 'Soy1humano?')
v_user = ('moy' , 'aranza' , 'miguel')
#---------------------------- FUNCIONES ------------------------
# METODO DE ACCESO TIPO LOGIN
def acceso():
    
    while True:
        os.system ("clear")#LIMPIAR PANTALLA
        print("\n\tInicio de secion")
        user = str(input("\n\t\tUsuario: "))
        if user in v_user :
            password = getpass.getpass("\n\tContraseña: ")
            if password in v_password :
                print(f"\n\tBienvenido usuario {user} ...")
                break
            else:
                input("\n\tcontraseña incorrecta.\n\tEnter para continuar...")
        else:
            input("\n\tUsuario incorrecto.\n\tEnter para continuar...")
    input("\n\tEnter para continuar...")

# METODO DE MENU
def menu():
    
