from .conexion import create_conection

class Registro_productos():

    def insert_producto(self, ID_producto, Nombre, Descripcion, ID_categoria, Precio_venta, Precio_compra, Utilidad, Stock, Existencia):
        conn = create_conection()
        cur = conn.cursor()
        sql="""INSERT INTO Producto (ID_producto, Nombre, Descripcion, ID_categoria, Precio_venta, Precio_compra, Utilidad, Stock, Existencia)
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}')""".format(ID_producto, Nombre, Descripcion, ID_categoria, Precio_venta, Precio_compra, Utilidad, Stock, Existencia)
        cur.execute(sql)
        conn.commit()
        cur.close()

    def retornar_productos(self):
        conn = create_conection()
        cursor = conn.cursor()
        sql = "SELECT * FROM Producto"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT * FROM Producto WHERE ID_producto = (\'"+ID+"\')"
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_productos(ID):
        conn = create_conection()
        cur = conn.cursor()
        sql="SELECT * FROM Producto WHERE ID_producto = (\'"+ID+"\')"
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def actualiza_productos(self, ID_producto, Nombre, Descripcion, ID_categoria, Precio_venta, Precio_compra, Utilidad, Stock, Existencia):
        conn = create_conection()
        cur = conn.cursor()
        sql ='''UPDATE Producto SET  Nombre = '{}', Descripcion = '{}', ID_categoria = '{}', Precio_venta = '{}', Precio_compra = '{}', Utilidad = '{}', Stock = '{}', Existencia = '{}'
        WHERE ID_producto = '{}' '''.format(Nombre, Descripcion, ID_categoria, Precio_venta, Precio_compra, Utilidad, Stock, Existencia, ID_producto)
        cur.execute(sql)
        a = cur.rowcount
        conn.commit()
        cur.close()
        return a

    def ultimo_producto(self):
        conn = create_conection()
        cur = conn.cursor()
        sql = "SELECT ID_producto FROM Producto ORDER BY ID_producto DESC LIMIT 1"
        cur.execute(sql)
        a = cur.fetchall()
        return a
