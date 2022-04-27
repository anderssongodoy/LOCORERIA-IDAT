import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from Controlador.FuncionesProducto import Funciones_producto
from Controlador.FuncionesVendedor import Funciones_vendedor
from Controlador.FuncionesCliente import Funciones_cliente
from Controlador.FuncionesPedido import Funciones_pedido
from Controlador.FuncionesVenta import Funciones_venta
from Controlador.FuncionesDetalle import Funciones_detalle
from Controlador.FuncionesCaja import Funciones_caja
from Controlador.FuncionesBoleta import Funciones_boleta



class VentanaMenu(QMainWindow):
    def __init__(self, parent=None, _id=None):
        super(VentanaMenu,self).__init__(parent)
        loadUi("UI/menu.ui", self)
        # ocultar la barra de titulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Sistema de Ventas")
        self.setIcon()
        # control de la barra de titulo
        self.restaurar.clicked.connect(self.control_restaurar)
        self.maximizar.clicked.connect(self.control_maximizar)
        self.minimizar.clicked.connect(self.control_minimizar)
        self.cerrar.clicked.connect(lambda: self.close())
        #self.restaurar.hide()

        # sizegrip ( redimensionar )
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
        self.superior.mouseMoveEvent = self.mover_ventana

        #acceder a las paginas
        self.inicio.clicked.connect(self.pagina1)
        self.vendedor.clicked.connect(self.pagina2)
        self.producto.clicked.connect(self.pagina3)
        self.cliente.clicked.connect(self.pagina4)
        self.pedido.clicked.connect(self.pagina5)
        self.vender.clicked.connect(self.pagina6)
        self.detalle.clicked.connect(self.pagina7)
        self.caja.clicked.connect(self.pagina8)
        
        self.vendedorb.clicked.connect(self.pagina2)
        self.productob.clicked.connect(self.pagina3)
        self.clienteb.clicked.connect(self.pagina4)
        self.reporteb.clicked.connect(self.pagina5)
        self.venderb.clicked.connect(self.pagina6)
        self.detalleb.clicked.connect(self.pagina7)
        self.cajab.clicked.connect(self.pagina8)

        # mover menu
        #self.menu.clicked.connect(self.contraer_menu)
        self.menu.clicked.connect(lambda: self.slideLeftMenu())

        # funciones producto
        self.agregarbtn.clicked.connect(self.insert_productos)
        self.actualizarbtn.clicked.connect(self.m_productos)
        self.buscarbtn2.clicked.connect(self.buscarm_productos)
        self.buscarbtn.clicked.connect(self.buscar_producto)
        self.guardarbtn.clicked.connect(self.modificar_producto)
        self.eliminarbtn.clicked.connect(self.eliminar_producto)
        self.refrescarp.clicked.connect(self.refrescar_idp)

        #funciones vendedor
        self.agregarvbtn.clicked.connect(self.insert_vendedor)
        self.actualizarvbtn.clicked.connect(self.m_vendedor)
        self.buscarvbtn2.clicked.connect(self.buscarm_vendedor)
        self.buscarvbtn.clicked.connect(self.buscar_vendedor)
        self.guardarvbtn.clicked.connect(self.modificar_vendedor)
        self.eliminarvbtn.clicked.connect(self.eliminar_vendedor)
        self.refrescarv.clicked.connect(self.refrescar_idv)

        #funciones cliente
        self.registrarcbtn.clicked.connect(self.insert_cliente)
        self.actualizarcbtn.clicked.connect(self.m_cliente)
        self.buscarbtnc2.clicked.connect(self.buscarm_cliente)
        self.buscarcbtn.clicked.connect(self.buscar_cliente)
        self.guardarcbtn.clicked.connect(self.modificar_cliente)
        self.eliminarcbtn.clicked.connect(self.eliminar_cliente)
        self.refrescarc.clicked.connect(self.refrescar_idc)

        #funciones pedido
        self.registrarpdbtn.clicked.connect(self.insert_pedido)
        self.actualizarpdbtn.clicked.connect(self.m_pedido)
        self.buscarpdbtn2.clicked.connect(self.buscarm_pedido)
        self.buscarpdbtn.clicked.connect(self.buscar_pedido)
        self.guardarpdbtn.clicked.connect(self.modificar_pedido)
        self.eliminarpdbtn.clicked.connect(self.eliminar_pedido)
        self.refrescarpd.clicked.connect(self.refrescar_idpd)

        #funciones venta
        self.registrarvtbtn.clicked.connect(self.insert_venta)
        self.actualizarvtbtn.clicked.connect(self.m_venta)
        self.buscarvtbtn2.clicked.connect(self.buscarm_venta)
        self.buscarvtbtn.clicked.connect(self.buscar_venta)
        self.guardarvtbtn2.clicked.connect(self.modificar_venta)
        self.eliminarvt.clicked.connect(self.eliminar_venta)
        self.refrescarvtbtn.clicked.connect(self.refrescar_idvt)

        #funciones detalle
        self.registrardbtn.clicked.connect(self.insert_detalle)
        self.actualizardbtn.clicked.connect(self.m_detalle)
        self.buscardbtn2.clicked.connect(self.buscarm_detalle)
        self.buscardbtn.clicked.connect(self.buscar_detalle)
        self.guardardbtn2.clicked.connect(self.modificar_detalle)
        self.eliminardbtn.clicked.connect(self.eliminar_detalle)
        self.refrescard.clicked.connect(self.refrescar_idd)

        #funciones caja
        self.registrarcjbtn.clicked.connect(self.insert_caja)
        self.actualizarcjbtn.clicked.connect(self.m_caja)
        self.buscarcjbtn2.clicked.connect(self.buscarm_caja)
        self.buscarcjbtn.clicked.connect(self.buscar_caja)
        self.guardarcjbtn.clicked.connect(self.modificar_caja)
        self.eliminarcjbtn.clicked.connect(self.eliminar_caja)
        self.refrescarcj.clicked.connect(self.refrescar_idcj)

        #funciones boleta
#        self.registrarpdbtn.clicked.connect(self.insert_boleta)
#        self.actualizarpdbtn.clicked.connect(self.m_boleta)
#        self.buscarpdbtn2.clicked.connect(self.buscarm_boleta)
#        self.buscarpdbtn.clicked.connect(self.buscar_boleta)
#        self.guardarpdbtn.clicked.connect(self.modificar_boleta)
#        self.eliminarpdbtn.clicked.connect(self.eliminar_boleta)
#        self.refrescarpd.clicked.connect(self.refrescar_idb)



# ===========================================
# ===========================================
#          DISEÑO DE LA VENTANA MENU
# ===========================================
# ===========================================

    # REDIMENSIONAR
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # MINIMIZAR
    def control_minimizar(self):
        self.showMinimized()

    # RESTAURAR
    def control_restaurar(self):
        self.showNormal()
        self.restaurar.hide()
        self.maximizar.show()

    def control_maximizar(self):
        self.showMaximized()
        self.maximizar.hide()
        self.restaurar.show()

    # MOVER VENTANA
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

    # PAGINAS
    def pagina1(self):
        self.stackedWidget.setCurrentWidget(self.pagina_inicio)
        #self.paginas_animaciones()

    def pagina2(self):
        self.stackedWidget.setCurrentWidget(self.pagina_vendedor)
        #self.paginas_animaciones()

    def pagina3(self):
        self.stackedWidget.setCurrentWidget(self.pagina_producto)
        #self.paginas_animaciones()

    def pagina4(self):
        self.stackedWidget.setCurrentWidget(self.pagina_cliente)
        #self.paginas_animaciones()

    def pagina5(self):
        self.stackedWidget.setCurrentWidget(self.pagina_pedido)
        #self.paginas_animaciones()

    def pagina6(self):
        self.stackedWidget.setCurrentWidget(self.pagina_venta)

    def pagina7(self):
        self.stackedWidget.setCurrentWidget(self.pagina_detalle)
        #self.paginas_animaciones()

    def pagina8(self):
        self.stackedWidget.setCurrentWidget(self.pagina_caja)

    def slideLeftMenu(self):
            # Get current left menu width
        width = self.izquierda.width()

        # If minimized
        if width == 10:
            # Expand menu
            newWidth = 150
        # If maximized
        else:
            # Restore menu
            newWidth = 10

        # Animate the transition
        self.animation = QPropertyAnimation(self.izquierda, b"minimumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    # ICONO DE WINDOWS
    def setIcon(self):
        appIcon = QIcon("IMAGES/vino.png")
        self.setWindowIcon(appIcon)
# ============================================

#=============================================
#=============================================
# FUNCIONES DE PRODUCTO
#=============================================
#=============================================
    # AGREGAR PRODUCTO
    def m_productos(self):
        Funciones_producto.mostrar_productos(self)
    def buscar_producto(self):
        Funciones_producto.buscarm_productos(self)
    def refrescar_idp(self):
        Funciones_producto.refrescar_id(self)
    def insert_productos(self):
        Funciones_producto.inserta_productos(self)
    def buscarm_productos(self):
        Funciones_producto.buscarm_producto(self)
    def modificar_producto(self):
        Funciones_producto.modificar_productos(self)
    def eliminar_producto(self):
        Funciones_producto.eliminar_productos(self)
# ================================================
# ================================================
# ================================================


# ================================================
# FUNCIONES VENDEDOR
# ================================================

    # AGREGAR VENDEDOR
    def m_vendedor(self):
        Funciones_vendedor.mostrar_vendedor(self)
    def buscar_vendedor(self):
        Funciones_vendedor.buscara_vendedor(self)
    def refrescar_idv(self):
        Funciones_vendedor.refrescar_id(self)
    def insert_vendedor(self):
        Funciones_vendedor.inserta_vendedor(self)
    def buscarm_vendedor(self):
        Funciones_vendedor.buscarmf_vendedor(self)
    def modificar_vendedor(self):
        Funciones_vendedor.modificara_vendedor(self)
    def eliminar_vendedor(self):
        Funciones_vendedor.eliminara_vendedor(self)
# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES CLIENTE

# ================================================

    # AGREGAR CLIENTE
    def m_cliente(self):
        Funciones_cliente.mostrar_cliente(self)
    def buscar_cliente(self):
        Funciones_cliente.buscara_cliente(self)
    def refrescar_idc(self):
        Funciones_cliente.refrescar_id(self)
    def insert_cliente(self):
        Funciones_cliente.inserta_cliente(self)
    def buscarm_cliente(self):
        Funciones_cliente.buscarm_clientes(self)
    def modificar_cliente(self):
        Funciones_cliente.modificar_clientes(self)
    def eliminar_cliente(self):
        Funciones_cliente.eliminar_clientes(self)

# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES PEDIDO

# ================================================

    # AGREGAR PEDIDO
    def m_pedido(self):
        Funciones_pedido.mostrar_pedido(self)
    def buscar_pedido(self):
        Funciones_pedido.buscara_pedido(self)
    def refrescar_idpd(self):
        Funciones_pedido.refrescar_id(self)
    def insert_pedido(self):
        Funciones_pedido.inserta_pedido(self)
    def buscarm_pedido(self):
        Funciones_pedido.buscarm_pedidos(self)
    def modificar_pedido(self):
        Funciones_pedido.modificar_pedidos(self)
    def eliminar_pedido(self):
        Funciones_pedido.eliminar_pedidos(self)

# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES VENTA

# ================================================

    # AGREGAR VENTA
    def m_venta(self):
        Funciones_venta.mostrar_venta(self)
    def buscar_venta(self):
        Funciones_venta.buscara_venta(self)
    def refrescar_idvt(self):
        Funciones_venta.refrescar_id(self)
    def insert_venta(self):
        Funciones_venta.inserta_venta(self)
    def buscarm_venta(self):
        Funciones_venta.buscarm_ventas(self)
    def modificar_venta(self):
        Funciones_venta.modificar_ventas(self)
    def eliminar_venta(self):
        Funciones_venta.eliminar_ventas(self)

# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES DETALLE

# ================================================

    # AGREGAR DETALLE
    def m_detalle(self):
        Funciones_detalle.mostrar_detalle(self)
    def buscar_detalle(self):
        Funciones_detalle.buscara_detalle(self)
    def refrescar_idd(self):
        Funciones_detalle.refrescar_id(self)
    def insert_detalle(self):
        Funciones_detalle.inserta_detalle(self)
    def buscarm_detalle(self):
        Funciones_detalle.buscarm_detalles(self)
    def modificar_detalle(self):
        Funciones_detalle.modificar_detalles(self)
    def eliminar_detalle(self):
        Funciones_detalle.eliminar_detalles(self)

# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES CAJA

# ================================================

    # AGREGAR CAJA
    def m_caja(self):
        Funciones_caja.mostrar_caja(self)
    def buscar_caja(self):
        Funciones_caja.buscara_caja(self)
    def refrescar_idcj(self):
        Funciones_caja.refrescar_id(self)
    def insert_caja(self):
        Funciones_caja.inserta_caja(self)
    def buscarm_caja(self):
        Funciones_caja.buscarm_cajas(self)
    def modificar_caja(self):
        Funciones_caja.modificar_cajas(self)
    def eliminar_caja(self):
        Funciones_caja.eliminar_cajas(self)

# ================================================
# ================================================
# ================================================
# ================================================

# FUNCIONES BOLETA

# ================================================

    # AGREGAR BOLETA
#    def m_boleta(self):
#        Funciones_boleta.mostrar_boleta(self)
#    def buscar_boleta(self):
#        Funciones_boleta.buscara_boleta(self)
#    def refrescar_idb(self):
#        Funciones_boleta.refrescar_id(self)
#    def insert_boleta(self):
#        Funciones_boleta.inserta_boleta(self)
#    def buscarm_boleta(self):
#        Funciones_boleta.buscarm_boletas(self)
#    def modificar_boleta(self):
#        Funciones_boleta.modificar_boletas(self)
#    def eliminar_boleta(self):
#       Funciones_boleta.eliminar_boletas(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    menu = VentanaMenu()
    menu.show()
    sys.exit(app.exec_())
