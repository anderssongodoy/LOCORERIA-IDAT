from .conexion import create_conection

class Registro_cliente():

    def insert_cliente(self, ID_cliente, Nombre, Apellido_paterno, Apellido_materno, DNI, Email):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Cliente (ID_vendedor, Nombre, Apellido_paterno, Apellido_materno, DNI, Email)
        VALUES('{}', '{}','{}', '{}','{}','{}')""".format(ID_cliente, Nombre, Apellido_paterno, Apellido_materno, DNI, Email)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_cliente(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Cliente"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_cliente(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Cliente WHERE ID_cliente = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_cliente(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Cliente WHERE ID_cliente = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_cliente(self, ID_cliente, Nombre, Apellido_paterno, Apellido_materno, DNI, Email):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Cliente SET  Nombre = '{}', Apellido_paterno = '{}', Apellido_materno = '{}', DNI = '{}', Email = '{}'
        WHERE ID_cliente = '{}' '''.format(Nombre, Apellido_paterno, Apellido_materno, DNI, Email, ID_cliente)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_cliente(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_cliente FROM Cliente ORDER BY ID_cliente DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a