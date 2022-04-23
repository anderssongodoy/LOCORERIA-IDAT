from re import split
from this import d
from PyQt5.QtWidgets import QTableWidgetItem
from db.caja import Registro_caja

class Funciones_caja():

    def mostrar_caja(self):
        data = Registro_caja.retornar_caja(self)
        self.tablacaja.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablacaja.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_caja(self):
        ID = self.buscarcj.text()
        data = Registro_caja.busca_caja(ID)
        self.tablacaja.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablacaja.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_caja.ultimo_caja(self)
        if len(self.refrescarid) != 0:
            self.idcaja.setText(self.refrescarid[0][0])
            a = self.idcaja.text()
            b = int(split('\D+', a)[1])
            c = b+1

            if c >=1 and c <= 9:
                d = "Cj000"+str(c)
                self.idcaja.setText(d)
            if c >= 10 and c <= 99:
                d ="Cj00"+str(c)
                self.idcaja.setText(d)
            elif c >= 100 and c <= 999:
                d ="Cj0"+str(c)
                self.idcaja.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "Cj"+str(c)
                self.idcaja.setText(d)

    def inserta_caja(self):
        ID = self.idcaja.text()
        iddetalle = self.iddetallecj.text()
        ingreso = self.ingreso.text()
        egreso = self.egreso.text()
        diferencia = self.diferencia.text()

        Registro_caja.insert_caja(ID, iddetalle, ingreso, egreso, diferencia)

        self.idcaja.clear()
        self.iddetallecj.clear()
        self.ingreso.clear()
        self.egreso.clear()
        self.diferencia.clear()

    def buscarm_cajas(self):
        id_caja = self.buscarcj2.text()
        self.caja = Registro_caja.busca_caja(id_caja)
        if len(self.caja) != 0:
            self.Id = self.caja[0][0]
            self.idcaja2.setText(self.caja[0][0])
            self.iddetallecj2.setText(self.caja[0][1])
            self.ingreso2.setText(str(self.caja[0][2]))
            self.egreso2.setText(str(self.caja[0][3]))
            self.diferencia2.setText(str(self.caja[0][4]))

    def modificar_cajas(self):
        if self.caja != '':

            idM = self.idcaja2.text()
            iddetalleM = self.iddetallecj2.text()
            ingresoM = self.ingreso2.text()
            egresoM = self.egreso2.text()
            diferenciaM = self.diferencia2.text()

            act = Registro_caja.actualiza_caja(idM, iddetalleM, ingresoM, egresoM, diferenciaM)

            if act == 1:
                self.idcaja2.clear()
                self.iddetallecj2.clear()
                self.ingreso2.clear()
                self.egreso2.clear()
                self.diferencia2.clear()

    def eliminar_cajas(self):
        select_row = self.tablacaja.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_caja.elimina_caja(ID)
