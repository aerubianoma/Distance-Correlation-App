import sys
from UI_PY import *
from PyQt5.QtWidgets import QDialog,QMessageBox,QWidget
from all_class import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        insertar = QtGui.QIcon('../otros archivos/insertar.svg')
        self.csv = False
        self.setupUi(self)
        self.calcular_aleatorio.clicked.connect(self.calcularAleatorio)
        self.calcular_archivo.clicked.connect(self.calcularArchivo)
        self.insertar_tabla.clicked.connect(self.getCSV)
        self.distance_number.setDigitCount(12)
        self.distance_number.setSmallDecimalPoint(True)
        self.insertar_tabla.setIcon(insertar)
        #PRUEBA

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()
    def calcularAleatorio(self):
        if self.tamano.text()=="":
            print("error")
            QMessageBox.about(self, "Error", "Porfavor ingrese el tamaño")
        else:
            muestra_aleatoria = Distance_correlation()
            muestra_aleatoria.x = np.random.uniform(-1,1,int(self.tamano.text()))
            muestra_aleatoria.y = np.random.uniform(-1,1,int(self.tamano.text()))
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
            print(muestra_archivo.x)
            muestra_archivo.calculateDistanceCorrelation(len(muestra_archivo.x))
            self.distance_number.display(muestra_archivo.distance_correlation)
        else:
            print("error")
            QMessageBox.about(self, "Error", "Archivo csv no cargado aún")

def iniciar():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
