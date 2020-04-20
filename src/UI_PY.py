# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calcular_aleatorio = QtWidgets.QPushButton(self.centralwidget)
        self.calcular_aleatorio.setGeometry(QtCore.QRect(70, 30, 211, 31))
        self.calcular_aleatorio.setObjectName("calcular_aleatorio")
        self.distance_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.distance_number.setGeometry(QtCore.QRect(460, 30, 211, 31))
        self.distance_number.setProperty("value", 0.0)
        self.distance_number.setObjectName("distance_number")
        self.insertar_tabla = QtWidgets.QPushButton(self.centralwidget)
        self.insertar_tabla.setGeometry(QtCore.QRect(10, 40, 51, 51))
        self.insertar_tabla.setText("")
        self.insertar_tabla.setObjectName("insertar_tabla")
        self.tamano = QtWidgets.QLineEdit(self.centralwidget)
        self.tamano.setGeometry(QtCore.QRect(290, 30, 151, 31))
        self.tamano.setObjectName("tamano")
        self.calcular_archivo = QtWidgets.QPushButton(self.centralwidget)
        self.calcular_archivo.setGeometry(QtCore.QRect(70, 70, 211, 31))
        self.calcular_archivo.setObjectName("calcular_archivo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 0, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 4, 231, 31))
        self.label_3.setObjectName("label_3")
        self.graficar = QtWidgets.QPushButton(self.centralwidget)
        self.graficar.setGeometry(QtCore.QRect(70, 110, 211, 31))
        self.graficar.setObjectName("graficar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 111, 21))
        self.label_4.setObjectName("label_4")
        self.grafica = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafica.setGeometry(QtCore.QRect(30, 170, 671, 401))
        self.grafica.setObjectName("grafica")
        self.arrays = QtWidgets.QCheckBox(self.centralwidget)
        self.arrays.setGeometry(QtCore.QRect(290, 70, 101, 31))
        self.arrays.setObjectName("arrays")
        self.listas = QtWidgets.QCheckBox(self.centralwidget)
        self.listas.setGeometry(QtCore.QRect(290, 110, 101, 31))
        self.listas.setObjectName("listas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.calcular_aleatorio.clicked.connect(self.distance_number.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcular_aleatorio.setText(_translate("MainWindow", "Muestras aleatorias"))
        self.calcular_archivo.setText(_translate("MainWindow", "Archivo csv"))
        self.label.setText(_translate("MainWindow", "Calcular la correlacion de la distancia con:"))
        self.label_2.setText(_translate("MainWindow", "Tamaño de la muestra:"))
        self.label_3.setText(_translate("MainWindow", "La correlacion de la distancia es:"))
        self.graficar.setText(_translate("MainWindow", "Graficar datos"))
        self.label_4.setText(_translate("MainWindow", "Grafica:"))
        self.arrays.setText(_translate("MainWindow", "Modo arrays"))
        self.listas.setText(_translate("MainWindow", "Modo listas"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

