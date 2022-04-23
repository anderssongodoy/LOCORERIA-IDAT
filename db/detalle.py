from .conexion import create_conection

class Registro_detalle:

    def insert_detalle(self, ID_detalle, ID_venta, Descuento, Total):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Detalle (ID_detalle, ID_venta, Descuento, Total)
        VALUES('{}', '{}','{}', '{}')""".format(ID_detalle, ID_venta, Descuento, Total)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_detalle(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Detalle"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_detalle(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Detalle WHERE ID_detalle = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_detalle(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Detalle WHERE ID_detalle = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_detalle(self, ID_detalle, ID_venta, Descuento, Total):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Detalle SET ID_venta = '{}', Descuento = '{}', Total = '{}'
        WHERE ID_detalle = '{}' '''.format(ID_venta, Descuento, Total, ID_detalle)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_detalle(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_detalle FROM Detalle ORDER BY ID_detalle DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a