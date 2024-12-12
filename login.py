from Frmlogin import *
from Menu import *
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #self.label_3.setText("Ricardo Luna Santos")
        self.btnEntrar.clicked.connect(self.validar)
        self.btnCancelar.clicked.connect(self.salir)

    def validar(self):
        usuario = self.txtUser.text()
        constrasena = self.txtPassword.text()
        if usuario=="admin" and constrasena == "1234":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Bienvenido al sistema")
            msgBox.setWindowTitle("Autorizado")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.openwindow()
                self.hide()
            else:
                self.close()
        else:
            QMessageBox.about(self, "Error", "Usuario o contraseña incorrectos")
            QMessageBox.setIcon(QMessageBox.Critical)
    
    def salir(self):
        self.close()

    def openwindow(self):
        openwindow = Menu(self)
        openwindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()