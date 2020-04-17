import sys
from UI_PY import *
from PyQt5.QtWidgets import QDialog,QMessageBox,QWidget,QVBoxLayout,QSizePolicy
from all_class import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        insertar = QtGui.QIcon('../otros archivos/insertar.svg')
        self.csv = False
        self.x = []
        self.y = []
        self.setupUi(self)
        self.calcular_aleatorio.clicked.connect(self.calcularAleatorio)
        self.calcular_archivo.clicked.connect(self.calcularArchivo)
        self.insertar_tabla.clicked.connect(self.getCSV)
        self.distance_number.setDigitCount(12)
        self.distance_number.setSmallDecimalPoint(True)
        self.insertar_tabla.setIcon(insertar)
        self.vbl = QVBoxLayout(self.grafica)
        #Se instancia el Lienzo con la grafica de Matplotlib
        self.qmc = Lienzo(self.grafica,self.x,self.y)
        # se instancia la barra de navegacion
        self.ntb = NavigationToolbar(self.qmc, self.grafica)
        #la barra de navegacion en el vbox
        self.vbl.addWidget(self.qmc)
        self.vbl.addWidget(self.ntb)
        self.graficar.clicked.connect(self.plot)
    def calcularAleatorio(self):
        if self.tamano.text()=="":
            print("error")
            QMessageBox.about(self, "Error", "Porfavor ingrese el tamaño")
        else:
            muestra_aleatoria = Distance_correlation()
            muestra_aleatoria.x = np.random.uniform(-1,1,int(self.tamano.text()))
            muestra_aleatoria.y = np.random.uniform(-1,1,int(self.tamano.text()))
            self.x = muestra_aleatoria.x
            self.y = muestra_aleatoria.y
            print(self.x)
            muestra_aleatoria.calculateDistanceCorrelation(int(self.tamano.text()))
            self.distance_number.display(muestra_aleatoria.distance_correlation)
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '../data')
        if filePath != "":
            print ("Dirección",filePath)
            self.df = pd.read_csv(str(filePath))
            self.csv = True
    def calcularArchivo(self):
        #AUN NO FUNCIONA BIEN LO DE LEER CSV
        if self.csv == True:
            muestra_archivo = Distance_correlation()
            muestra_archivo.x = self.df["x"]
            muestra_archivo.y = self.df["y"]
            self.x = muestra_archivo.x
            self.y = muestra_archivo.y
            print(muestra_archivo.x)
            muestra_archivo.calculateDistanceCorrelation(len(muestra_archivo.x))
            self.distance_number.display(muestra_archivo.distance_correlation)
        else:
            print("error")
            QMessageBox.about(self, "Error", "Archivo csv no cargado aún")
    def plot(self):
        if self.x != []: 
            self.qmc.setParent(None)
            self.ntb.setParent(None)
            #Se instancia el Lienzo con la grafica de Matplotlib
            self.qmc = Lienzo(self.grafica,self.x,self.y)
            # se instancia la barra de navegacion
            self.ntb = NavigationToolbar(self.qmc, self.grafica)
            #la barra de navegacion en el vbox
            self.vbl.addWidget(self.qmc)
            self.vbl.addWidget(self.ntb)
            print("grafica mostrada al usuario")
        else:
            print("error")
            QMessageBox.about(self, "Error", "Primero debe calcular el coeficiente")
class Lienzo(FigureCanvas):
    x = []
    y = []
    def __init__(self, parent,x,y):
        # Se instancia el objeto figure
        self.fig = Figure()
        #Se define la grafica en coordenadas polares
        self.axes = self.fig.add_subplot()
        #Se define el rango de 0 a 20 con saltos de 0.01
        self.x = x
        #Se calcula los valores de la funcion.
        self.y = y
        #Se define el eje X como logaritmico y se pasan los valores de x y y.
        """self.axes.semilogx(x, y);"""
        #Se define el limite del eje X
        """self.axes.set_xlim([0, 20]);"""
        #Se define una grilla
        self.axes.grid(True)
        #Se crea una etiqueta en el eje Y
        """self.axes.set_ylabel("log")"""
        self.axes.plot(self.x,self.y,"o")
        # se inicializa FigureCanvas
        FigureCanvas.__init__(self, self.fig)
        # se define el widget padre
        self.setParent(parent)
        # se define el widget como expandible
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        # se notifica al sistema de la actualizacion
        #de la politica
        FigureCanvas.updateGeometry(self)
    def plot(self):
        self.axes.plot(x,y)

def iniciar():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
