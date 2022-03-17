from sqlite3 import Row, connect

conexion = connect("databases/database.db")
conexion.row_factory = Row
conexion.execute("PRAGMA foreign_keys = 1")

def execute(consulta: str, parametros: list = [], commit = False) -> list | bool:
    try:
        resultado = conexion.execute(consulta, parametros)
    except:
        return False
    else:
        if(not commit):
            return resultado.fetchall()
        else:
            conexion.commit()
            return bool(resultado.rowcount)