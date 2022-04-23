from re import split
from PyQt5.QtWidgets import QTableWidgetItem
from db.clientes import Registro_cliente

class Funciones_cliente():

    def mostrar_cliente(self):
        data = Registro_cliente.retornar_cliente(self)
        self.tablacliente.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablacliente.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def buscara_cliente(self):
        ID = self.buscarc.text()
        data = Registro_cliente.busca_cliente(ID)
        self.tablacliente.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tablacliente.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def refrescar_id(self):
        self.refrescarid = Registro_cliente.ultimo_cliente(self)
        if len(self.refrescarid) != 0:
            self.idcliente.setText(self.refrescarid[0][0])
            a = self.idcliente.text()
            b = int(split('\D+', a)[1])
            c = b+1
            
            if c >=1 and c <= 9:
                d = "Cl00"+str(c)
                self.idcliente.setText(d)
            if c >= 10 and c <= 99:
                d ="Cl0"+str(c)
                self.idcliente.setText(d)
            elif c >= 100 and c <= 999:
                d ="Cl"+str(c)
                self.idcliente.setText(d)

    def inserta_cliente(self):
        ID = self.idcliente.text()
        nombre = self.nombrec.text()
        apellidopaterno = self.apellidopaternoc.text()
        apellidomaterno = self.apellidomaternoc.text()
        dni = self.dnic.text()
        email = self.emailc.text()

        self.clientedatos.insert_cliente(ID, nombre, apellidopaterno, apellidomaterno, dni, email)

        self.idcliente.clear()
        self.nombrec.clear()
        self.apellidopaternoc.clear()
        self.apellidomaternoc.clear()
        self.dnic.clear()
        self.emailc.clear()

    def buscarm_clientes(self):
        id_cliente = self.buscarc2.text()
        self.cliente = Registro_cliente.busca_cliente(id_cliente)
        if len(self.cliente) != 0:
            self.Id = self.cliente[0][0]
            self.idcliente2.setText(self.cliente[0][0])
            self.nombrec2.setText(self.cliente[0][1])
            self.apellidopaternoc2.setText(self.cliente[0][2])
            self.apellidomaternoc2.setText(self.cliente[0][3])
            self.dnic2.setText(str(self.cliente[0][4]))
            self.emailc2.setText(self.cliente[0][5])

    def modificar_clientes(self):
        if self.cliente != '':

            idM = self.idcliente2.text()
            nombreM = self.nombrec2.text()
            apellidopaternoM = self.apellidopaternoc2.text()
            apellidomaternoM = self.apellidomaternoc2.text()
            dniM = self.dnic2.text()
            emailM = self.emailc2.text()

            act = self.clientedatos.actualiza_cliente(idM, nombreM, apellidopaternoM, apellidomaternoM, dniM, emailM)

            if act == 1:
                self.idcliente2.clear()
                self.nombrec2.clear()
                self.apellidopaternoc2.clear()
                self.apellidomaternoc2.clear()
                self.dnic2.clear()
                self.emailc2.clear()

    def eliminar_clientes(self):
        select_row = self.tablacliente.selectedItems()
        if select_row:
            ID = select_row[0].text()

            Registro_cliente.elimina_cliente(ID)
