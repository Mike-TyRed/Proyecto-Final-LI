# -------------------------- IMPORTACIONES -----------------------
import getpass
from os import system
# --------------------------- ASIGNACIONES -----------------------
v_password = ('123', 'hola', 'Soy1humano?')
v_user = ('moy', 'aranza', 'miguel')
# ---------------------------- FUNCIONES ------------------------
# METODO DE ACCESO TIPO LOGIN


def acceso():

    while True:
        system("cls")  # LIMPIAR PANTALLA
        print("\n\tInicio de secion")
        user = str(input("\n\t\tUsuario: "))
        if user in v_user:
            password = getpass.getpass("\n\t\tContraseña: ")
            if password in v_password:
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
        system("cls")  # LIMPIAR PANTALLA
        print("\n\t< MENU >")
        print("\n\n\t1.- Portada ITT.")
        print("\n\t2.- Cadenas.")
        print("\n\t3.- Cuestionario.")
        print("\n\t4.- Pregunta sencilla con firma.")
        print("\n\t5.- Impresión de boleta")
        print("\n\t6.- Impresión de un cuadrado.")
        print("\n\t7.- Captura de 4 números.")
        print("\n\t8.- Sistema de unidades.")
        print("\n\t9.- Operaciones matemáticas. ")
        print("\n\t10.- Operaciones lógicas.")
        print("\n\t11.- Ejercicios 28/09/22.")
        print("\n\t12.- Corrección de codigo 4, 5 y 6.")
        print("\n\t13.- Tablas de multiplicar.")
        print("\n\t14.- Temas anteriores.")
        print("\n\t15.- Programa clave de acceso.")
        print("\n\t16.- Programa código de limpieza y usuario, contraseña ocultas.")
        print("\n\t17.- Funciones.")
        print("\n\t18.- Tipos de triángulos.")
        print("\n\t19.- Salir.")
        menu = int(input("\n\n\tOpcion: "))
        if menu == 1:

            PortadaITT()

        elif menu == 2:

            Cadenas()

        elif menu == 3:

            Cuestionario()

        elif menu == 4:

            PreguntaSencillaFirma()

        elif menu == 5:

            ImpresionBoleta()

        elif menu == 6:

            ImpresionCuadrado()

        elif menu == 7:

            Captura4Numeros()

        elif menu == 8:

            SistemaUnidades()

        elif menu == 9:

            OperacionesMatematicas()

        elif menu == 10:

            OperacionesLogicas()

        elif menu == 11:

            Ejercicios28()

        elif menu == 12:

            Correccion17()

        elif menu == 13:

            TablasMultiplicar()

        elif menu == 14:

            ProyectoIntegrador()

        elif menu == 15:

            ClaveAcceso()

        elif menu == 16:

            CodigoLimpieza()

        elif menu == 17:

            Funciones()

        elif menu == 18:

            TiposTriangulos()

        elif menu == 19:
            break

# METODOS DE EJERCICIOS

# 1.- Portada ITT.


def PortadaITT():
    system("cls")
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

# 2.- Cadenas.


def Cadenas():
    system("cls")
    print("Tecnologico de Tijuana")
    print("Lenguajes de interfaz")
    print("Gutierrez Sandoval Terrazas")
    print("Tomas Aquino")
    print("Ingenieria en Sistemas")
    print("Computacion ")
    print("DosBox ")

    print("")
    input("Presiona enter para continuar...")
    opc = 0

# 3.- Cuestionario.


def Cuestionario():
    system("cls")  # LIMPIAR PANTALLA
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

# 4.- Pregunta sencilla con firma.


def PreguntaSencillaFirma():
    system("cls")  # LIMPIAR PANTALLA
    ps = input("\n\tPregunta sencilla.\n\n\tCual es tu nombre? ")
    input(f"\n\tTu nombre es: {ps}\n\tEnter para continuar.")
    menu()

# 5.- Impresión de boleta.


def ImpresionBoleta():
    system("cls")
    var1 = input("Nombre de tu escuela: ")
    var2 = input("Nombre del alumno: ")
    var3 = input("Grupo y grado: ")
    var4 = input("Inserta materia 1: ")
    cal11 = int(input("Calificacion unidad 1: "))
    cal12 = int(input("Calificacion unidad 2: "))
    cal13 = int(input("Calificacion unidad 3: "))
    var5 = input("Inserta materia 2: ")
    cal21 = int(input("Calificacion unidad 1: "))
    cal22 = int(input("Calificacion unidad 2: "))
    cal23 = int(input("Calificacion unidad 3: "))
    var6 = input("Inserta materia 3: ")
    cal31 = int(input("Calificacion unidad 1: "))
    cal32 = int(input("Calificacion unidad 2: "))
    cal33 = int(input("Calificacion unidad 3: "))
    var7 = input("Inserta materia 4: ")
    cal41 = int(input("Calificacion unidad 1: "))
    cal42 = int(input("Calificacion unidad 2: "))
    cal43 = int(input("Calificacion unidad 3: "))

    prom1 = ((cal11 + cal12 + cal13) / 3)
    prom2 = ((cal21 + cal22 + cal23) / 3)
    prom3 = ((cal31 + cal32 + cal33) / 3)
    prom4 = ((cal41 + cal42 + cal43) / 3)

    promfinal = ((prom1 + prom2 + prom3 + prom4) / 4)

    print("""o


        """)

    print(f"{var1}              {var2}                      {var3}    ")
    print("_______________________________________________________________________________________")
    print("Nombre de la escuela                   Nombre del alumno                  Grado y grupo")
    print("")
    print("=======================================================================================")
    print("Materia                  Calificacion 1    Calificacion 2    Calificacion 3    Promedio")
    print(
        f"Materia 1:{var4}             {cal11}                   {cal12}                  {cal13}             {prom1}")
    print(
        f"Materia 2:{var5}         {cal21}                 {cal22}                {cal23}              {prom2}")
    print(
        f"Materia 3:{var6}            {cal31}                 {cal32}                 {cal33}              {prom3}")
    print(
        f"Materia 4:{var7}             {cal41}                 {cal42}                 {cal43}              {prom4}")
    print("=======================================================================================")
    print(f"Promedio final: {promfinal}")

    print("""


        """)

    print("")
    input("Presiona enter para continuar...")
    opc = 0

# 6.- IMPRESION CUADRADO


def ImpresionCuadrado():
    system("cls")
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
    print("")
    input("Presiona enter para continuar...")
    menu()

# 7.- CAPTURA 4 NUMEROS


def Captura4Numeros():
    system("cls")
    n1 = input("Ingresa primer numero: ")
    n2 = input("Ingresa segundo numero: ")
    n3 = input("Ingresa tercer numero: ")
    n4 = input("Ingresa cuarto numero: ")

    print("Primer numero: " + n1)
    print("Segundo numero: " + n2)
    print("Tercer numero: " + n3)
    print("Cuarto numero: " + n4)

    print("")
    input("Presiona enter para continuar...")
    menu()

# 8.- SISTEMA DE UNIDADES


def SistemaUnidades():
    system("cls")
    x = int(input("Ingresa un número: "))
    print("\n\tUnidades: " + str(x * 1))
    print("Decenas: " + str(x * 10))
    print("Centenas: " + str(x * 100))
    print("Millares: " + str(x * 1000))
    print("Decenas de millar: " + str(x * 10000))
    print("Centenas de millar: " + str(x * 100000))
    print("Millones: " + str(x * 1000000))

    print("")
    input("Presiona enter para continuar...")
    menu()

# 9.- OPERACIONES MATEMATICAS


def OperacionesMatematicas():
    system("cls")
    print("""
    1.Sumar 2 variables, réstale un valor  y al resultado sumarla otra valor.
    2.-Sumar 3 variables y al obtener el  resultado sumarle un cuarto valor.
    3.-Realizar 2 operaciones donde se combinen operaciones matemáticas básicas.
    """)

    opc = int(input("Selecciona operacion a realizar: "))

    if (opc == 1):
        n1 = int(input("Ingresa primer numero: "))
        n2 = int(input("Ingresa segundo numero: "))
        n3 = int(input("Ingresa tercer numero: "))
        n4 = int(input("Ingresa cuarto numero: "))

        resultado = n1 + n2 - n3 + n4

        print("El resultado es:")
        print(resultado)

    if (opc == 2):
        n1 = int(input("Ingresa primer numero: "))
        n2 = int(input("Ingresa segundo numero: "))
        n3 = int(input("Ingresa tercer numero: "))
        n4 = int(input("Ingresa cuarto numero: "))

        resultado = n1 + n2 + n3 + n4

        print("El resultado es:")
        print(resultado)

    if (opc == 2):
        n1 = int(input("Ingresa primer numero: "))
        n2 = int(input("Ingresa segundo numero: "))
        n3 = int(input("Ingresa tercer numero: "))
        n4 = int(input("Ingresa cuarto numero: "))

        resultado = (n1 * n2) + (n3 - n4)

        print("El resultado es:")
        print(resultado)

    print("")
    input("Presiona enter para continuar...")
    menu()


# 10.- OPERACIONES LOGICAS

def OperacionesLogicas():
    system("cls")
    n1 = int(input("Ingresa numero 1: "))
    n2 = int(input("Ingresa numero 2: "))

    if (n1 < n2):
        print("Primer numero es menor")

    if (n1 > n2):
        print("Primer numero es mayor")

    if (n1 == n2):
        print("Los numeros son iguales")

    print("")
    input("Presiona enter para continuar...")
    menu()


# 12.- EJECCION 28/09/22


def Ejercicios28():
    system("cls")
    print("""¡Morir es nada cuando por la patria se muere!
    José María Morelos y Pavón
    
    La madrugada del 16 de septiembre de 1810, El cura Don Miguel Hidalgo y Costilla convocó al pueblo de Dolores Hidalgo, a través del repique de las campanas de su iglesia, a levantarse en armas en contra del dominio de los españoles.
    El periodo de nuestra historia conocido como la Guerra de Independencia empieza (estrictamente hablando) la madrugada del 16 de septiembre de 1810, cuando el padre Miguel Hidalgo da el llamado ‘Grito de Dolores’ y termina el 27 de septiembre de 1821 (11 años después) con la entrada triunfal del Ejército Trigarante, encabezado por Agustín de Iturbide y Vicente Guerrero, a una jubilosa Ciudad de México. El objetivo principal de este movimiento (armado y social) era liberar a nuestro territorio del yugo español y que, en cada rincón de la Colonia se olvidase por completo el concepto de virreinato.
    """)

    # 2.-Realiza una suma, resta, multiplicación y división con números diferentes cada uno y utiliza valores  con decimales para la suma.

    print("Ingresa un número en decimal: ")
    num1 = float(input())
    print("Ingresa otro número en decimal: ")
    num2 = float(input())
    print("El resultado es: " + str(num1 + num2))

    print("")

    print("Ingresa un número: ")
    num1 = int(input())
    print("Ingresa otro número: ")
    num2 = float(input())
    print("El resultado es: " + str(num1 - num2))

    print("")

    print("Ingresa un número: ")
    num1 = int(input())
    print("Ingresa otro número: ")
    num2 = int(input())
    print("El resultado es: " + str(num1 * num2))

    print("")

    print("Ingresa un número: ")
    num1 = int(input())
    print("Ingresa otro número: ")
    num2 = int(input())
    print("El resultado es: " + str(num1 / num2))

    print("")
    input("Presiona enter para continuar...")
    menu()

    # 3.-Realiza 6 preguntas y concatenaras las respuestas en una un párrafo e imprímelo.

    print("Cual es tu nombre? ")
    nombre = input()
    print("Cual es tu edad? ")
    edad = input()
    print("Cual es tu color favorito? ")
    color = input()
    print("Cual es tu comida favorita? ")
    comida = input()
    print("Cual es tu deporte favorito? ")
    deporte = input()
    print("Cual es tu animal favorito? ")
    animal = input()

    Cuestionario = """¿Cómo te llamas? {nombre}
    ¿Cuántos años tienes? {edad}
    ¿Cuál es tu comida favorita? {comida}
    ¿Cuál es tu color favorito? {color} 
    ¿Cuál es tu deporte favorito? {deporte}
    ¿Cuál es tu animal favorito? {animal}""".format(nombre=nombre, edad=edad, comida=comida, color=color, deporte=deporte, animal=animal)
    print(Cuestionario)

    print("")
    input("Presiona enter para continuar...")
    menu()

    menu()

# 13.- CICLOS WHILE Y FOR


def Correccion17():
    i = 1
    while i <= 3:
        print(i)
        i += 1
    print("Programa terminado")

    i = 1
    while i <= 50:
        print(i)
        i = 3 * i + 1
    print("Programa terminado")

    numero = int(input("Escriba un número positivo: "))
    while numero < 0:
        print("¡Ha escrito un número negativo! Inténtelo de nuevo")
        numero = int(input("Escriba un número positivo: "))
    print("Gracias por su colaboración")

    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1

    print("")
    i = int(input("Ingrese un número: "))
    if i > 0:
        while i > 0:
            print(i, end=" ")
            i -= 1
    else:
        print("")
        print("No se aceptan numeros negativos")

    print("Comienzo")
    for i in [0, 1, 2]:
        print("Hola ", end="")
    print()
    print("Final")

    print("Comienzo")
    for i in []:
        print("Hola ", end="")
    print()
    print("Final")

    print("Comienzo")
    for i in [1, 1, 1]:
        print("Hola ", end="")
    print()
    print("Final")

    print("Comienzo")
    for _ in [0, 1, 2]:
        print("Hola ", end="")
    print()
    print("Final")

    print("Comienzo")
    for i in [3, 4, 5]:
        print(f"Hola. Ahora i vale {i} y su cuadrado {i ** 2}")
    print("Final")

    print("Comienzo")
    for i in ["Alba", "Benito", 27]:
        print(f"Hola. Ahora i vale {i}")
    print("Final")

    print("Comienzo")
    for numero in [0, 1, 2, 3]:
        print(f"{numero} * {numero} = {numero ** 2}")
    print("Final")

    i = 10
    print(f"El bucle no ha comenzado. Ahora i vale {i}")

    for i in [0, 1, 2, 3, 4]:
        print(f"{i} * {i} = {i ** 2}")
    print(f"El bucle ha terminado. Ahora i vale {i}")

    for i in [0, 1, 2]:
        print(f"{i} * {i} = {i ** 2}")
    print()
    for i in [0, 1, 2, 3]:
        print(f"{i} * {i} * {i} = {i ** 3}")

    for i in "AMIGO":
        print(f"Dame una {i}")
    print("¡AMIGO!")

    print("Comienzo")
    for i in range(10):
        print("Hola ", end="")
    print()
    print("Final")

    veces = int(input("¿Cuántas veces quiere que le salude? "))
    for i in range(veces):
        print("Hola ", end="")
    print()
    print("Adiós")

    print("")
    input("Presiona enter para continuar...")
    menu()

# 14.- TABLA DE MULTIPLICAR


def TablasMultiplicar():
    system("cls")
    Lista = {1, 2, 3, 4, 5, 7, 8, 9, 10}

    for x in Lista:
        print(f"3 x {x} = {3*x}")

    print(" ")

    table = int(input("¿Que tabla de multiplicar desea? "))
    Lista = {1, 2, 3, 4, 5, 7, 8, 9, 10}

    for x in Lista:
        print(f"{table} x {x} = {table*x}")

    print("")
    input("Presiona enter para continuar...")
    menu()

# 15.- Proyecto integrador de temas anteriores de python


def ProyectoIntegrador():
    system("cls")

    name = input("¿Cómo te llamas? ")
    print("Bienvenido al sistema", name)
    print("")
    while True:
        system("cls")
        print("""
        =================Menu=================
        |Calcular area y perimetro de: |
        | 1 Cuadrado |
        | 2 Rectangulo |
        | 3 Triangulo |
        |4. Contar letras de una cadena |
        |5. Arreglo de 10 registros |
        |6. Atinar un numero random |
        |7. Imprimir una lista de 5 registros|
        |8. Salir |
        =====================================""")
        opcion = input("¿Qué opción deseas? ")
        if opcion == "8":
            print("Saliendo...")
            break
        # Cuadrado
        if opcion == "1":
            print("Calculando area y perimetro de un cuadrado")
            l = float(input("Introduce el valor de un lado: "))
            print("El area es: ", l*l)
            print("El perimetro es: ", 4*l)
        # Rectangulo

        elif opcion == "2":
            print("Calculando area y perimetro de un rectangulo")
            b = float(input("Introduce el valor de la base: "))
            h = float(input("Introduce el valor de la altura: "))
            print("El area es: ", b*h)
            print("El perimetro es: ", 2*(b+h))
        # Triangulo
        elif opcion == "3":
            print("Calculando area y perimetro de un triangulo")
            b = float(input("Introduce el valor de la base: "))
            h = float(input("Introduce el valor de la altura: "))
            print("El area es: ", b*h/2)
            print("El perimetro es: ", 2*(b+h))
        # Contar letras de una cadena
        elif opcion == "4":
            print("Contando letras de una cadena")
            cadena = input("Introduce una cadena: ")
            print("La cadena tiene", len(cadena), "letras")
        # Imprimir un arreglo de 10 registros
        elif opcion == "5":
            print("Imprimiendo un arreglo de 10 registros")
            r = []
            for i in range(1, 11):
                registro = input("Introduce un registro: ")
                posicion = input("Introduce la posicion: ")
                r.insert(int(posicion), registro)
                print("")
                input("Presiona enter para continuar...")
                menu()
        # Atinar un registro de un arreglo
        elif opcion == "6":
            print("Atinando un registro de un arreglo")
            comparacion = input("Ingresa un registro: ")
            for i in r:
                if comparacion == i:
                    print("Registro encontrado")
                    break

            else:
                print("registro no encontrado")
                break
        # Imprimir una lista de 5 registros
        elif opcion == "7":
            print("Imprimiendo una lista de 5 registros")
            lista = []
            print("Comienzo")
            for i in range(5):
                lista.append(input("Introduce un nombre: "))
                print("Hola. Ahora" + i + "vale" + lista[i])
                print("Final")
                break
        else:
            print("Opción incorrecta")
        print("")
        input("Presiona enter para continuar...")

# 16.- Programa claves de acceso


def ClaveAcceso():
    system("cls")
    pas = "interfaz123"
    ans = True
    while ans == True:
        password = input("Ingrese una contraseña: ")
        print("")
        if (len(password) <= 8):
            print("La contraseña es demasiado corta")

        if (len(password) >= 8) and (password != pas):
            print("La contraseña es suficientemente larga, pero es incorrecta")

        if password == pas:
            print("Contraseña correcta")
            break
    print("")
    print("Bienvenido usuario")

    print("")
    input("Presiona enter para continuar...")
    menu()

# 17.- Programa de calculadora


def CodigoLimpieza():
    system("cls")
    ans = True
    while ans:
        contra = ('123', 'hola', 'Soy1humano?')
        usr = input("Ingresa tu usuario: ")
        print(" ")
        passw = getpass.getpass("Tu contraseña: ")
        print(" ")
        if passw in contra:
            print(f"Bienvenido {usr}")
            ans = False
        else:
            print("Error")

    print("")
    input("Presiona enter para continuar...")
    menu()

# 18.- FUNCIONES


def Funciones():
    system("cls")

    def respuestas1():
        print(f"Respuesta 1: {p1}")
        print(f"Respuesta 2: {p2}")
        print(f"Respuesta 3: {p3}")
        print(f"Respuesta 4: {p4}")

    def respuestas2():
        print(f"Respuesta 5: {p5}")
        print(f"Respuesta 6: {p6}")
        print(f"Respuesta 7: {p7}")
        print(f"Respuesta 8: {p8}")

    p1 = input("¿Cómo te llamas? ")
    p2 = input("¿Cuántos años tienes? ")
    p3 = input("Color favorito: ")
    p4 = input("¿Perros o gatos? ")

    system('cls')

    respuestas1()
    print("")
    input("Presiona enter para continuar...")

    system('cls')

    opcion = int(input("¿Cuántos recorridos deseas? "))
    x = 0
    while x < opcion:
        p1 = input("¿Cómo te llamas? ")
        p2 = input("¿Cuántos años tienes? ")
        p3 = input("Color favorito: ")
        p4 = input("¿Perros o gatos? ")
        print("")
        respuestas1()
        x += 1

    print("")
    input("Presiona enter para continuar...")

    system('cls')

    p5 = input("¿Qué estudias? ")
    p6 = input("¿Tienes PC o laptop? ")
    p7 = input("Comida favorita: ")
    p8 = input("Bebida favorita: ")

    system('cls')

    respuestas1()
    respuestas2()

    print("")
    input("Presiona enter para continuar...")
    menu()


# 19.- Tipos de triangulos
def TiposTriangulos():
    system("cls")

    def cantidad_vocales(cadena):
        cant = 0
        cant1 = 0
        for x in range(len(cadena)):
            if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u":
                cant = cant+1
        print("Cantidad de vocales de la palabra", cadena, "es", cant)
        for x in range(len(cadena)):
            if cadena[x] != "":
                cant1 = cant1+1
        print("Cantidad de letras de la palabra", cadena, "es", cant1)

    # Bloque principal
    cantidad_vocales("administracion")
    cantidad_vocales("hola mundo")
    cantidad_vocales("ana")

    # Crear funcion donde tiene 4 palabaras y va a contar todas las vocales de las frases y su total

    cantidad_vocales("Amigo ven te invito una copa")
    cantidad_vocales("ya no tomo gracias")
    cantidad_vocales("no tomas bien te invito un café")
    cantidad_vocales("bueno")

    # Introducir los lados de un triángulo y encontrar qué tipo de triángulo es

    input("Presione enter para continuar...")
    system('cls')

    def triangulo(ladoA, ladoB, ladoC):
        if ladoA == ladoB & ladoB == ladoC:
            print("todos los lados son iguales, es un Triangulo Equilatero.")

        elif ladoA == ladoB & ladoA != ladoC | ladoA != ladoB & ladoA == ladoC | ladoB == ladoC & ladoA != ladoC:
            print("solo dos lados son iguales, es un Triangulo Isóseles.")
        else:
            print("todos lo lados son distintos, es un Triangulo Escaleno.")

    ladoA = int(input("Ingresa un lado: "))
    ladoB = int(input("Ingresa otro lado: "))
    ladoC = int(input("Ingresa otro lado: "))

    triangulo(ladoA, ladoB, ladoC)

    print("")
    input("Presiona enter para continuar...")
    menu()


# ----------------------------- LLAMADAS ------------------------
acceso()
