from .conexion import create_conection

class Registro_vendedor():

    def insert_vendedor(self, ID_vendedor, Nombre, Apellido_paterno, Apellido_materno, DNI, Email):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Vendedor (ID_vendedor, Nombre, Apellido_paterno, Apellido_materno, DNI, Email)
        VALUES('{}', '{}','{}', '{}','{}','{}')""".format(ID_vendedor, Nombre, Apellido_paterno, Apellido_materno, DNI, Email)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_vendedor(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Vendedor"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_vendedor(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Vendedor WHERE ID_vendedor = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_vendedor(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Vendedor WHERE ID_vendedor = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_vendedor(self, ID_vendedor, Nombre, Apellido_paterno, Apellido_materno, DNI, Email):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Vendedor SET  Nombre = '{}', Apellido_paterno = '{}', Apellido_materno = '{}', DNI = '{}', Email = '{}'
        WHERE ID_vendedor = '{}' '''.format(Nombre, Apellido_paterno, Apellido_materno, DNI, Email, ID_vendedor)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_vendedor(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_vendedor FROM Vendedor ORDER BY ID_vendedor DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a