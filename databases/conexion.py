from sqlite3 import Row, connect
from typing import Iterable

conexion = connect("databases/database.db")
conexion.row_factory = Row

def rowToDict(row: Row) -> dict:
    diccionario = {}
    for key in row.keys():
        diccionario[key] = row[key]

    return diccionario

def execute(consulta: str, parametros: Iterable = [], commit = False) -> list | bool:
    try:
        resultado = conexion.execute(consulta, parametros)
    except:
        return False
    else:
        if(not commit):
            return list(map(rowToDict, resultado.fetchall()))
        else: 
            conexion.commit()
            return bool(resultado.rowcount)