from sqlite3 import connect

conexion = connect("databases/database.db")

def execute(consulta: str, ):
    cursor = conexion.cursor()

    nombreSitio = input("dime el nombre del sitio: ")
    cursor.execute("Select * from Sitios where upper(nombre) = ?", [nombreSitio.upper()])

    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

execute()