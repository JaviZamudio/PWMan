import databases.conexion as con

# - - - - SITIOS - - - -
def getAllSitios() -> list:
    consulta = """
        SELECT *
        FROM sitios
    """

    return con.execute(consulta)
    #retorna una lista con todos los dict

def getSitio(idSitio: int) -> list:
    consulta = """
        SELECT *
        FROM sitios
        WHERE IdSitio = ?
    """

    return con.execute(consulta, [idSitio])
    #retorna una lista con un o ningun dict

def addSitio(nombre) -> bool:
    consulta = """
        INSERT INTO sitios (Nombre)
        VALUES (?)
    """

    return con.execute(consulta, [nombre], True)
    #retorna true (todo bien) o false (El nombre del sitio ya existe)

def deleteSitio(idSitio) -> bool:
    consulta = """
        DELETE FROM sitios
        WHERE IdSitio = ?
    """

    return con.execute(consulta, [idSitio], True)
    #retorna true (se eliminó un sitio y sus cuentas) false (si no se eliminó nada)

# - - - - CUENTAS - - - -
def getTodasCuentas() -> list:
    consulta = """
        SELECT *
        FROM cuentas
    """

    return con.execute(consulta)


def getCuenta(idCuenta: int) -> list:
    consulta = """
        SELECT *
        FROM cuentas
        WHERE idCuenta = ?
    """

    return con.execute(consulta, [idCuenta])
    #retorna una lista con un o ningun dict

def addCuenta(nombreUsuario, correo, contrasena, idSitio) -> bool:
    consulta = """
        INSERT INTO cuentas (nombreUsuario, correo, contrasena, idsitio)
        VALUES (?, ?, ?, ?)
    """

    return con.execute(consulta, [nombreUsuario, correo, contrasena, idSitio], True)
    #retorna true (todo bien) o false (no existe ese IdSitio)

def deleteCuenta(idCuenta) -> bool:
    consulta = """
        DELETE FROM cuentas
        WHERE idCuenta = ?
    """

    return con.execute(consulta, [idCuenta], True)
    #retorna true (se eliminó un Cuenta) false (si no se eliminó nada)