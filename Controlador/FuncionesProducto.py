from re import split
from PyQt5.QtWidgets import QTableWidgetItem
from db.productos import Registro_productos

class Funciones_producto():

    def mostrar_productos(self):
        data = Registro_productos.retornar_productos(self)
        self.tablaproducto.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablaproducto.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscar_productos(self):
        ID = self.buscar.text()
        data = Registro_productos.busca_producto(ID)
        self.tablaproducto.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablaproducto.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_productos.ultimo_producto(self)
        if len(self.refrescarid) != 0:
            self.idproducto.setText(self.refrescarid[0][0])
            a = self.idproducto.text()
            b = int(split('\D+', a)[1])
            c = b+1
            if c >= 10 and c <= 99:
                d ="P00"+str(c)
                self.idproducto.setText(d)
            elif c >= 100 and c <= 999:
                d ="P0"+str(c)
                self.idproducto.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "P"+str(c)
                self.idproducto.setText(d)

    def inserta_productos(self):
        ID = self.idproducto.text()
        nombre = self.nombrep.text()
        descripcion = self.descripcionp.text()
        categoria = self.categoriap.text()
        PV = self.ventap.text()
        PC = self.comprap.text()
        Utilidad = self.utilidadp.text()
        Stock = self.stockp.text()
        Existencia = self.existenciap.text()

        Registro_productos.insert_producto(self, ID, nombre, descripcion, categoria, PV, PC, Utilidad, Stock, Existencia)

        self.idproducto.clear()
        self.nombrep.clear()
        self.descripcionp.clear()
        self.categoriap.clear()
        self.ventap.clear()
        self.comprap.clear()
        self.utilidadp.clear()
        self.stockp.clear()
        self.existenciap.clear()

    def buscarm_producto(self):
        id_producto = self.buscar2.text()
        self.producto = Registro_productos.busca_producto(id_producto)
        if len(self.producto) != 0:
            self.Id = self.producto[0][0]
            self.idproducto2.setText(self.producto[0][0])
            self.nombrep2.setText(self.producto[0][1])
            self.descripcionp2.setText(self.producto[0][2])
            self.categoriap2.setText(self.producto[0][3])
            self.ventap2.setText(str(self.producto[0][4]))
            self.comprap2.setText(str(self.producto[0][5]))
            self.utilidadp2.setText(str(self.producto[0][6]))
            self.stockp2.setText(str(self.producto[0][7]))
            self.existenciap2.setText(str(self.producto[0][8]))

    def modificar_productos(self):
        if self.producto != '':
            idM = self.idproducto2.text()
            nombreM = self.nombrep2.text()
            descripcionM = self.descripcionp2.text()
            categoriaM = self.categoriap2.text()
            PVM = self.ventap2.text()
            PCM = self.comprap2.text()
            stockM = self.stockp2.text()
            utilidadM = self.utilidadp2.text()
            existenciaM = self.existenciap2.text()

            act = Registro_productos.actualiza_productos(idM, nombreM, descripcionM, categoriaM, PVM, PCM, stockM, utilidadM, existenciaM)

            if act == 1:
                self.idproducto2.clear()
                self.nombrep2.clear()
                self.descripcionp2.clear()
                self.categoriap2.clear()
                self.ventap2.clear()
                self.comprap2.clear()
                self.utilidadp2.clear()
                self.stockp2.clear()
                self.existenciap2.clear()

    def eliminar_productos(self):
        select_row = self.tablaproducto.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_productos.elimina_productos(ID)
