from re import split
from PyQt5.QtWidgets import QTableWidgetItem
from db.pedido import Registro_pedido

class Funciones_pedido():

    def mostrar_pedido(self):
        data = Registro_pedido.retornar_pedido(self)
        self.tablapedido.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablapedido.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_pedido(self):
        ID = self.buscarpd.text()
        data = Registro_pedido.busca_pedido(ID)
        self.tablapedido.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablapedido.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_pedido.ultimo_pedido(self)
        if len(self.refrescarid) != 0:
            self.idpedido.setText(self.refrescarid[0][0])
            a = self.idpedido.text()
            b = int(split('\D+', a)[1])
            c = b+1

            if c >=1 and c <= 9:
                d = "Pd000"+str(c)
                self.idpedido.setText(d)
            if c >= 10 and c <= 99:
                d ="Pd00"+str(c)
                self.idpedido.setText(d)
            elif c >= 100 and c <= 999:
                d ="Pd0"+str(c)
                self.idpedido.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "Pd"+str(c)
                self.idpedido.setText(d)

    def inserta_pedido(self):
        ID = self.idpedido.text()
        idcliente = self.idclientepd.text()
        idproducto = self.idproductopd.text()
        cantidad = self.cantidadpd.text()
        fechapedido = self.fechapd.text()

        self.pedidodatos.insert_pedido(ID, idcliente, idproducto, cantidad, fechapedido)

        self.idpedido.clear()
        self.idclientepd.clear()
        self.idproductopd.clear()
        self.cantidadpd.clear()
        self.fechapd.clear()

    def buscarm_pedidos(self):
        id_pedido = self.buscarpd2.text()
        self.pedido = Registro_pedido.busca_pedido(id_pedido)
        if len(self.pedido) != 0:
            self.Id = self.pedido[0][0]
            self.idpedido2.setText(self.pedido[0][0])
            self.idclientepd2.setText(self.pedido[0][1])
            self.idproductopd2.setText(self.pedido[0][2])
            self.cantidadpd2.setText(str(self.pedido[0][3]))
            self.fechapd2.setText(str(self.pedido[0][4]))

    def modificar_pedidos(self):
        if self.pedido != '':

            idM = self.idpedido2.text()
            idclienteM = self.idclientepd2.text()
            idproductoM = self.idproductopd2.text()
            cantidadM = self.cantidadpd2.text()
            fechaM = self.fechapd2.text()

            act = self.pedidodatos.actualiza_pedido(idM, idclienteM, idproductoM, cantidadM, fechaM)

            if act == 1:
                self.idpedido2.clear()
                self.idclientepd2.clear()
                self.idproductopd2.clear()
                self.cantidadpd2.clear()
                self.fechapd2.clear()

    def eliminar_pedidos(self):
        select_row = self.tablapedido.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_pedido.elimina_pedido(ID)
