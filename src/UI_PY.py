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
        MainWindow.resize(731, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calcular_aleatorio = QtWidgets.QPushButton(self.centralwidget)
        self.calcular_aleatorio.setGeometry(QtCore.QRect(10, 30, 211, 31))
        self.calcular_aleatorio.setObjectName("calcular_aleatorio")
        self.distance_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.distance_number.setGeometry(QtCore.QRect(360, 130, 211, 31))
        self.distance_number.setProperty("value", 0.0)
        self.distance_number.setObjectName("distance_number")
        self.insertar_tabla = QtWidgets.QPushButton(self.centralwidget)
        self.insertar_tabla.setGeometry(QtCore.QRect(230, 70, 31, 31))
        self.insertar_tabla.setText("")
        self.insertar_tabla.setObjectName("insertar_tabla")
        self.tamano = QtWidgets.QLineEdit(self.centralwidget)
        self.tamano.setGeometry(QtCore.QRect(230, 30, 111, 31))
        self.tamano.setObjectName("tamano")
        self.calcular_archivo = QtWidgets.QPushButton(self.centralwidget)
        self.calcular_archivo.setGeometry(QtCore.QRect(10, 70, 211, 31))
        self.calcular_archivo.setObjectName("calcular_archivo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 0, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 100, 231, 31))
        self.label_3.setObjectName("label_3")
        self.graficar = QtWidgets.QPushButton(self.centralwidget)
        self.graficar.setGeometry(QtCore.QRect(10, 110, 211, 31))
        self.graficar.setObjectName("graficar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 111, 21))
        self.label_4.setObjectName("label_4")
        self.grafica = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafica.setGeometry(QtCore.QRect(30, 180, 671, 361))
        self.grafica.setObjectName("grafica")
        self.arrays = QtWidgets.QCheckBox(self.centralwidget)
        self.arrays.setGeometry(QtCore.QRect(230, 130, 101, 31))
        self.arrays.setObjectName("arrays")
        self.listas = QtWidgets.QCheckBox(self.centralwidget)
        self.listas.setGeometry(QtCore.QRect(230, 110, 101, 31))
        self.listas.setObjectName("listas")
        self.deshacer = QtWidgets.QPushButton(self.centralwidget)
        self.deshacer.setGeometry(QtCore.QRect(360, 70, 31, 31))
        self.deshacer.setText("")
        self.deshacer.setObjectName("deshacer")
        self.tipo_entrada = QtWidgets.QLabel(self.centralwidget)
        self.tipo_entrada.setGeometry(QtCore.QRect(360, 160, 251, 21))
        self.tipo_entrada.setObjectName("tipo_entrada")
        self.hacer = QtWidgets.QPushButton(self.centralwidget)
        self.hacer.setGeometry(QtCore.QRect(400, 70, 31, 31))
        self.hacer.setText("")
        self.hacer.setObjectName("hacer")
        self.ingresar_funcion = QtWidgets.QLineEdit(self.centralwidget)
        self.ingresar_funcion.setGeometry(QtCore.QRect(380, 30, 201, 31))
        self.ingresar_funcion.setObjectName("ingresar_funcion")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 0, 221, 31))
        self.label_5.setObjectName("label_5")
        self.extremo_izquierdo = QtWidgets.QLineEdit(self.centralwidget)
        self.extremo_izquierdo.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.extremo_izquierdo.setObjectName("extremo_izquierdo")
        self.extremo_derecho = QtWidgets.QLineEdit(self.centralwidget)
        self.extremo_derecho.setGeometry(QtCore.QRect(620, 30, 31, 31))
        self.extremo_derecho.setObjectName("extremo_derecho")
        self.salto = QtWidgets.QLineEdit(self.centralwidget)
        self.salto.setGeometry(QtCore.QRect(650, 30, 31, 31))
        self.salto.setObjectName("salto")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 10, 47, 13))
        self.label_6.setObjectName("label_6")
        self.encolar = QtWidgets.QPushButton(self.centralwidget)
        self.encolar.setGeometry(QtCore.QRect(550, 70, 31, 31))
        self.encolar.setText("")
        self.encolar.setObjectName("encolar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 30, 61, 31))
        self.label_7.setObjectName("label_7")
        self.prioridad = QtWidgets.QLineEdit(self.centralwidget)
        self.prioridad.setGeometry(QtCore.QRect(490, 70, 51, 31))
        self.prioridad.setObjectName("prioridad")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 60, 81, 41))
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 0, 20, 181))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(350, 100, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.calcular = QtWidgets.QPushButton(self.centralwidget)
        self.calcular.setGeometry(QtCore.QRect(690, 30, 31, 31))
        self.calcular.setText("")
        self.calcular.setObjectName("calcular")
        self.desencolar = QtWidgets.QPushButton(self.centralwidget)
        self.desencolar.setGeometry(QtCore.QRect(590, 70, 31, 31))
        self.desencolar.setText("")
        self.desencolar.setObjectName("desencolar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Distance_correlation"))
        self.calcular_aleatorio.setText(_translate("MainWindow", "Muestras aleatorias"))
        self.calcular_archivo.setText(_translate("MainWindow", "Archivo csv"))
        self.label.setText(_translate("MainWindow", "Calcular la correlacion de la distancia con:"))
        self.label_2.setText(_translate("MainWindow", "Tamaño de la muestra:"))
        self.label_3.setText(_translate("MainWindow", "La correlacion de la distancia es:"))
        self.graficar.setText(_translate("MainWindow", "Graficar datos"))
        self.label_4.setText(_translate("MainWindow", "Grafica:"))
        self.arrays.setText(_translate("MainWindow", "Modo arrays"))
        self.listas.setText(_translate("MainWindow", "Modo listas"))
        self.tipo_entrada.setText(_translate("MainWindow", "No se registra entrada aún"))
        self.label_5.setText(_translate("MainWindow", "Ingresar funcion por pantalla:"))
        self.label_6.setText(_translate("MainWindow", "Dominio:"))
        self.label_7.setText(_translate("MainWindow", "y = "))
        self.label_8.setText(_translate("MainWindow", "Prioridad:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        MainWindow.setWindowIcon(QtGui.QIcon('../otros_archivos/distance.jpg'))

