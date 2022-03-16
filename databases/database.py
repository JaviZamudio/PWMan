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
    filas = conexion.execute(consulta, parametros)

    if(not commit):
        filas = filas.fetchall()
        resultado = []
        for fila in filas:
            resultado.append(rowToDict(fila))
        return resultado
    else: 
        conexion.commit()
        return bool(filas.rowcount)

sitios = execute("select * from sitios where idSitio")
for sitio in sitios:
    print(sitio)