from re import split
from PyQt5.QtWidgets import QTableWidgetItem
from db.detalle import Registro_detalle

class Funciones_detalle():

    def mostrar_detalle(self):
        data = Registro_detalle.retornar_detalle(self)
        self.tabladetalle.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tabladetalle.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_detalle(self):
        ID = self.buscard.text()
        data = Registro_detalle.busca_detalle(ID)
        self.tabladetalle.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tabladetalle.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_detalle.ultimo_detalle(self)
        if len(self.refrescarid) != 0:
            self.iddetalle.setText(self.refrescarid[0][0])
            a = self.iddetalle.text()
            b = int(split('\D+', a)[1])
            c = b+1

            if c >=1 and c <= 9:
                d = "D000"+str(c)
                self.iddetalle.setText(d)
            if c >= 10 and c <= 99:
                d ="D00"+str(c)
                self.iddetalle.setText(d)
            elif c >= 100 and c <= 999:
                d ="D0"+str(c)
                self.iddetalle.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "D"+str(c)
                self.iddetalle.setText(d)

    def inserta_detalle(self):
        ID = self.iddetalle.text()
        idventa = self.idventad.text()
        descuento = self.descuentod.text()
        total = self.totald.text()

        Registro_detalle.insert_detalle(ID, idventa, descuento, total)

        self.iddetalle.clear()
        self.idventad.clear()
        self.descuentod.clear()
        self.totald.clear()

    def buscarm_detalles(self):
        id_detalle = self.buscard2.text()
        self.detalle = Registro_detalle.busca_detalle(id_detalle)
        if len(self.detalle) != 0:
            self.Id = self.detalle[0][0]
            self.iddetalle2.setText(self.detalle[0][0])
            self.idventad2.setText(self.detalle[0][1])
            self.descuentod2.setText(self.detalle[0][2])
            self.totald2.setText(str(self.detalle[0][3]))

    def modificar_detalles(self):
        if self.detalle != '':

            idM = self.iddetalle2.text()
            idventaM = self.idventad2.text()
            descuentoM = self.descuentod2.text()
            totalM = self.totald2.text()

            act = Registro_detalle.actualiza_detalle(idM, idventaM, descuentoM, totalM)

            if act == 1:
                self.iddetalle2.clear()
                self.idventad2.clear()
                self.descuentod2.clear()
                self.totald2.clear()

    def eliminar_detalles(self):
        select_row = self.tabladetalle.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_detalle.elimina_detalle(ID)
