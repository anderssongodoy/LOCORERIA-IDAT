from .conexion import create_conection

class Registro_venta:

    def insert_venta(self, ID_venta, ID_pedido, ID_vendedor, Precio_unitario, Subtotal, Fecha_venta):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Venta (ID_venta, ID_pedido, ID_vendedor, Precio_unitario, Subtotal, Fecha_venta)
        VALUES('{}', '{}','{}', '{}','{}', '{}')""".format(ID_venta, ID_pedido, ID_vendedor, Precio_unitario, Subtotal, Fecha_venta)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_venta(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Venta"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_venta(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Venta WHERE ID_venta = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_venta(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Venta WHERE ID_venta = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_venta(self, ID_venta, ID_pedido, ID_vendedor, Precio_unitario, Subtotal, Fecha_venta):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Venta SET ID_pedido = '{}', ID_vendedor = '{}', Precio_unitario = '{}', Subtotal = '{}', Fecha_venta = '{}'
        WHERE ID_venta = '{}' '''.format(ID_pedido, ID_vendedor, Precio_unitario, Subtotal, Fecha_venta, ID_venta)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_venta(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_venta FROM Venta ORDER BY ID_venta DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a