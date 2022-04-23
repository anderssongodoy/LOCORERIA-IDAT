from .conexion import create_conection

class Registro_caja:

    def insert_caja(self, ID_caja, ID_detalle, Ingreso, Egreso, Diferencia):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Caja (ID_caja, ID_detalle, Ingreso, Egreso, Diferencia)
        VALUES('{}', '{}','{}', '{}')""".format(ID_caja, ID_detalle, Ingreso, Egreso, Diferencia)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_caja(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Caja"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_caja(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Caja WHERE ID_caja = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_caja(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Caja WHERE ID_caja = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_caja(self, ID_caja, ID_detalle, Ingreso, Egreso, Diferencia):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Caja SET ID_detalle= '{}', Ingreso = '{}', Egreso = '{}', Diferencia = '{}'
        WHERE ID_caja = '{}' '''.format(ID_detalle, Ingreso, Egreso, Diferencia, ID_caja)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_caja(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_caja FROM Caja ORDER BY ID_caja DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a