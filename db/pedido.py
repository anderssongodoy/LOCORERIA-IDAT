from .conexion import create_conection

class Registro_pedido:

    def insert_pedido(self, ID_pedido, ID_cliente, ID_producto, Cantidad, Fecha_pedido):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Pedido (ID_pedido, ID_cliente, ID_producto, Cantidad, Fecha_pedido)
        VALUES('{}', '{}','{}', '{}','{}')""".format(ID_pedido, ID_cliente, ID_producto, Cantidad, Fecha_pedido)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_pedido(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Pedido"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_pedido(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Pedido WHERE ID_pedido = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_pedido(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql= "DELETE FROM Pedido WHERE ID_pedido = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_pedido(self, ID_pedido, ID_cliente, ID_producto, Cantidad, Fecha_pedido):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Cliente SET  ID_cliente = '{}', ID_producto = '{}', Cantidad = '{}', Fecha_pedido = '{}'
        WHERE ID_cliente = '{}' '''.format(ID_cliente, ID_producto, Cantidad, Fecha_pedido, ID_pedido)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_pedido(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_pedido FROM Pedido ORDER BY ID_pedido DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a