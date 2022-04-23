from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import sqlite3
from Vista.circulo import VentanaBarra


class VentanaLogin(QMainWindow):
    def __init__(self):
        super(VentanaLogin,self).__init__()
        loadUi("UI/login.ui", self)
        
        # ocultar la barra de titulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # control de la barra de titulos
        self.minimizar.clicked.connect(self.control_minimizar)
        self.cerrar.clicked.connect(lambda: self.close())
        
        # sizegrip ( redimensionar )
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        # mover ventana
        self.barra.mouseMoveEvent = self.mover_ventana

        # login
        self.logearse.clicked.connect(self.loginfunction)

    # LOGIN
    
    def loginfunction(self, value):
        user = self.usuario.text()
        password = self.contra.text()
        
        verificacion = [(user,password)]
        if len(user) == 0 or len(password) == 0 :
            htmlText = """<p>Porfavor <br/>ingresar<br/>los datos</p><p><br/></p>"""
            
            self.error.setText(htmlText)
            
        else :
            
            conn = sqlite3.connect("licoreria.db")
            cur = conn.cursor()
            query = "SELECT * FROM logins WHERE username = ? AND password = ? "
            cur.execute(query, (user,password))
            result_pass = cur.fetchall()
            if result_pass == verificacion :
                self.barra = VentanaBarra()
                self.barra.show()
                self.close()
                
            else :
                htmlText = """<p>Datos<br/>Incorrectos</p>"""
                self.error.setText(htmlText)

    # MINIMIZAR
    def control_minimizar(self):
        self.showMinimized()

    # MOVER VENTANA
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
    
    #SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)



#Login.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#Login.setAttribute(QtCore.Qt.WA_TranslucentBackground)