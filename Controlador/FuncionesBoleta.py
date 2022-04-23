from re import split, sub
from PyQt5.QtWidgets import QTableWidgetItem
from db.venta import Registro_venta

class Funciones_boleta():

    def mostrar_venta(self):
        data = Registro_venta.retornar_venta(self)
        self.tablaventa.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablaventa.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_venta(self):
        ID = self.buscarvt.text()
        data = Registro_venta.busca_venta(ID)
        self.tablaventa.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablaventa.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_venta.ultimo_venta(self)
        if len(self.refrescarid) != 0:
            self.idventa.setText(self.refrescarid[0][0])
            a = self.idventa.text()
            b = int(split('\D+', a)[1])
            c = b+1

            if c >=1 and c <= 9:
                d = "Vt000"+str(c)
                self.idventa.setText(d)
            if c >= 10 and c <= 99:
                d ="Vt00"+str(c)
                self.idventa.setText(d)
            elif c >= 100 and c <= 999:
                d ="Vt0"+str(c)
                self.idventa.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "Vt"+str(c)
                self.idventa.setText(d)

    def inserta_venta(self):
        ID = self.idventa.text()
        idpedido = self.idpedidovt.text()
        idvendedor = self.idvendedorvt.text()
        preciounitario = self.preciounitariovt.text()
        subtotal = self.subtotalvt.text()
        fecha = self.fechavt.text()

        Registro_venta.insert_venta(ID, idpedido, idvendedor, preciounitario, subtotal, fecha)

        self.idventa.clear()
        self.idpedidovt.clear()
        self.idvendedorvt.clear()
        self.preciounitariovt.clear()
        self.subtotalvt.clear()
        self.fechavt.clear()

    def buscarm_ventas(self):
        id_venta = self.buscarvt2.text()
        self.venta = Registro_venta.busca_venta(id_venta)
        if len(self.venta) != 0:
            self.Id = self.venta[0][0]
            self.idventa2.setText(self.venta[0][0])
            self.idpedidovt2.setText(self.venta[0][1])
            self.idvendedorvt2.setText(self.venta[0][2])
            self.preciounitariovt2.setText(str(self.venta[0][3]))
            self.subtotalvt2.setText(str(self.venta[0][4]))
            self.fechavt2.setText(self.venta[0][5])

    def modificar_ventas(self):
        if self.venta != '':

            idM = self.idventa2.text()
            idpedidoM = self.idpedidovt2.text()
            idvendedorM = self.idvendedorvt2.text()
            preciounitarioM = self.preciounitariovt2.text()
            subtotalM = self.subtotalvt2.text()
            fechaM = self.fechavt2.text()

            act = Registro_venta.actualiza_venta(idM, idpedidoM, idvendedorM, preciounitarioM, subtotalM, fechaM)

            if act == 1:
                self.idventa2.clear()
                self.idpedidovt2.clear()
                self.idvendedorvt2.clear()
                self.preciounitariovt2.clear()
                self.subtotalvt2.clear()
                self.fechavt2.clear()

    def eliminar_ventas(self):
        select_row = self.tablaventa.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_venta.elimina_venta(ID)
