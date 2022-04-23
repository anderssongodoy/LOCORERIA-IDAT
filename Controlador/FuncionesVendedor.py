from re import split
from PyQt5.QtWidgets import QTableWidgetItem
from db.vendedor import Registro_vendedor

class Funciones_vendedor():

    def mostrar_vendedor(self):
        data = Registro_vendedor.retornar_vendedor(self)
        self.tablavendedor.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablavendedor.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_vendedor(self):
        ID = self.buscarv.text()
        data = Registro_vendedor.busca_vendedor(ID)
        self.tablavendedor.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablavendedor.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_vendedor.ultimo_vendedor(self)
        if len(self.refrescarid) != 0:
            self.idvendedor.setText(self.refrescarid[0][0])
            a = self.idvendedor.text()
            b = int(split('\D+', a)[1])
            print (b)
            c = b+1
            print (c)
            if c >=1 and c <= 9:
                d = "V000"+str(c)
                self.idvendedor.setText(d)
            elif c >= 10 and c <= 99:
                d ="V00"+str(c)
                self.idvendedor.setText(d)
            elif c >= 100 and c <= 999:
                d ="V0"+str(c)
                self.idvendedor.setText(d)
            elif c >= 1000 and c <= 9999:
                d = "V"+str(c)
                self.idvendedor.setText(d)

    def inserta_vendedor(self):
        ID = self.idvendedor.text()
        nombre = self.nombrev.text()
        apellidopaterno = self.apellidopaternov.text()
        apellidomaterno = self.apellidomaternov.text()
        dni = self.dniv.text()
        email = self.emailv.text()

        Registro_vendedor.insert_vendedor(self, ID, nombre, apellidopaterno, apellidomaterno, dni, email)

        self.idvendedor.clear()
        self.nombrev.clear()
        self.apellidopaternov.clear()
        self.apellidomaternov.clear()
        self.dniv.clear()
        self.emailv.clear()

    def buscarmf_vendedor(self):
        id_vendedor = self.buscarv2.text()
        self.vendedor = Registro_vendedor.busca_vendedor(id_vendedor)
        if len(self.vendedor) != 0:
            self.Id = self.vendedor[0][0]
            self.idvendedor2.setText(self.vendedor[0][0])
            self.nombrev2.setText(self.vendedor[0][1])
            self.apellidopaternov2.setText(self.vendedor[0][2])
            self.apellidomaternov2.setText(self.vendedor[0][3])
            self.dniv2.setText(str(self.vendedor[0][4]))
            self.emailv2.setText(self.vendedor[0][5])

    def modificara_vendedor(self):
        if self.vendedor != '':

            idM = self.idvendedor2.text()
            nombreM = self.nombrev2.text()
            apellidopaternoM = self.apellidopaternov2.text()
            apellidomaternoM = self.apellidomaternov2.text()
            dniM = self.dniv2.text()
            emailM = self.emailv2.text()

            act = Registro_vendedor.actualiza_vendedor(self, idM, nombreM, apellidopaternoM, apellidomaternoM, dniM, emailM)

            if act == 1:
                self.idvendedor2.clear()
                self.nombrev2.clear()
                self.apellidopaternov2.clear()
                self.apellidomaternov2.clear()
                self.dniv2.clear()
                self.emailv2.clear()

    def eliminara_vendedor(self):
        select_row = self.tablavendedor.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_vendedor.elimina_vendedor(ID)