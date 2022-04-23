import sys
from PyQt5.QtWidgets import QApplication
from Vista.principal import VentanaLogin

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = VentanaLogin()
    window.show()
    sys.exit(app.exec_())
