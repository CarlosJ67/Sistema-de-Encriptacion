# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmMenu(object):
    def setupUi(self, FrmMenu):
        FrmMenu.setObjectName("FrmMenu")
        FrmMenu.resize(1093, 710)
        self.centralwidget = QtWidgets.QWidget(FrmMenu)
        self.centralwidget.setObjectName("centralwidget")
        FrmMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 21))
        self.menubar.setObjectName("menubar")
        self.menuEncriptar = QtWidgets.QMenu(self.menubar)
        self.menuEncriptar.setObjectName("menuEncriptar")
        self.menuDesencriptar = QtWidgets.QMenu(self.menubar)
        self.menuDesencriptar.setObjectName("menuDesencriptar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        FrmMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmMenu)
        self.statusbar.setObjectName("statusbar")
        FrmMenu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEncriptar.menuAction())
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())

        self.retranslateUi(FrmMenu)
        QtCore.QMetaObject.connectSlotsByName(FrmMenu)

    def retranslateUi(self, FrmMenu):
        _translate = QtCore.QCoreApplication.translate
        FrmMenu.setWindowTitle(_translate("FrmMenu", "MainWindow"))
        self.menuEncriptar.setTitle(_translate("FrmMenu", "Encriptar"))
        self.menuDesencriptar.setTitle(_translate("FrmMenu", "Desencriptar"))
        self.menuAyuda.setTitle(_translate("FrmMenu", "Ayuda"))
        self.menuSalir.setTitle(_translate("FrmMenu", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmMenu = QtWidgets.QMainWindow()
    ui = Ui_FrmMenu()
    ui.setupUi(FrmMenu)
    FrmMenu.show()
    sys.exit(app.exec_())
