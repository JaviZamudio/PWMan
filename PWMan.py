from getpass import getpass
from os import system
import databases.DbFunctions as dbf
import cryptocode as cripto

# Inicio del programa

# Pedir la contraseña maestra
# Comprobar que el hash de la contraseña sea igual al hash guardado
# Guardar la contraseña maestra para desencriptar todo

# Acceder a la base de datos y al loop principal
# Dar el Menú de opciones

def titulo():
    system("cls")
    print("\n\t - - - - PWDMan - - - - \n")

def encriptar(texto: str):
    return cripto.encrypt(texto, contrasenaMaestra)
    
def desEncriptar(texto: str):
    return cripto.decrypt(texto, contrasenaMaestra)

hashContrasenaMaestra = hash("javi123")
contrasenaMaestra = ""

def login():
    while True:
        titulo()
        contrasenaMaestra = getpass("Escibre la contraseña maestra: ")

        if hash(contrasenaMaestra) != hashContrasenaMaestra:
            input("\nEsa contraseña es incorrecta, intenta otra vez . . .")
        else:
            break

    main()
            
def main():
    while True:
        allSitiosScreen()

def allSitiosScreen():
    titulo()

    #mostrar todos los sitios
    sitios = dbf.getAllSitios()

    print("0) Agregar Sitio")
    for sitio in sitios:
        print(f"{sitio['idSitio']}) {desEncriptar(sitio['nombre'])}")
    print("-1) Salir")
    opcion = int(input("Opcion: "))

    if(opcion == -1):
        exit()
    elif(opcion == 0):
        addSitioWindow()
    else:
        if(dbf.getSitio(opcion)):
            sitioScreen(opcion)
        else:
            input("\nEsa no es una opcion valida . . .")

def sitioScreen(idSitio: int):
    titulo()
    sitio = dbf.getSitio(idSitio)[0]
    cuentas = dbf.getTodasCuentas()

    print(f" - - Cuentas de {desEncriptar(sitio['nombre'])}:\n")

    for cuenta in cuentas:
        print(f"Nombre de Usuario: {desEncriptar(cuenta['nombreUsuario'])}")
        print(f"Correo: {desEncriptar(cuenta['correo'])}")
        print(f"Contraseña: {desEncriptar(cuenta['contrasena'])}")
        print(f"-----------------------------\n")

    print("0) Agregar Cuenta")
    print("-1) Regresar")
    opcion = int(input("Opcion: "))

    if(opcion == -1):
        allSitiosScreen()
    elif(opcion == 0):
        addCuentaWindow(idSitio)

def addSitioWindow():
    titulo()
    print("\tAgregar Sitio")
    nombre = input("Nombre del sitio: ")

    if dbf.addSitio(encriptar(nombre)):
        input("\nSitio agregado correctamente . . .")
    else:
        input("\nEse sitio ya existe . . .")

def addCuentaWindow(idSitio):
    titulo()
    print("\tAgregar Cuenta")
    nombreUsuario = input("Nombre de usuario: ")
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    if dbf.addCuenta(encriptar(nombreUsuario), encriptar(correo), encriptar(contrasena), idSitio):
        input("\nCuenta agregada correctamente . . .")
        sitioScreen(idSitio)
    else:
        input("\nOcurrio un error . . .")

login()