import sys
sys.path.append("..")
from lib.lib import *
from UI_PY import *
from all_class import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        insertar = QtGui.QIcon('../otros_archivos/icono_insertar.svg')
        insertar2 = QtGui.QIcon('../otros_archivos/deshacer.png')
        insertar3 = QtGui.QIcon('../otros_archivos/hacer.png')
        self.csv = False
        self.x = []
        self.y = []
        self.undo = []
        self.label = ""
        self.setupUi(self)
        self._toggle = True
        self.arrays.setChecked(self._toggle)
        self.listas.setChecked(not self._toggle)
        self.arrays.clicked.connect(self.toggle)
        self.listas.clicked.connect(self.toggle)
        self.calcular_aleatorio.clicked.connect(self.calcularAleatorio)
        self.calcular_archivo.clicked.connect(self.calcularArchivo)
        self.insertar_tabla.clicked.connect(self.getCSV)
        self.deshacer.clicked.connect(self.undoActions)
        self.hacer.clicked.connect(self.doActions)
        self.distance_number.setDigitCount(12)
        self.distance_number.setSmallDecimalPoint(True)
        self.insertar_tabla.setIcon(insertar)
        self.deshacer.setIcon(insertar2)
        self.hacer.setIcon(insertar3)
        self.vbl = QVBoxLayout(self.grafica)
        #Se instancia el Lienzo con la grafica de Matplotlib
        self.qmc = Lienzo(self.grafica,self.x,self.y,self.label)
        # se instancia la barra de navegacion
        self.ntb = NavigationToolbar(self.qmc, self.grafica)
        #la barra de navegacion en el vbox
        self.vbl.addWidget(self.qmc)
        self.vbl.addWidget(self.ntb)
        self.graficar.clicked.connect(self.plot)
        self.pila = Stack()
        self.pila2 = Stack()
    def calcularAleatorio(self):
        if self.arrays.isChecked() == True:
            if self.tamano.text()=="":
                print("error")
                QMessageBox.about(self, "Error", "Porfavor ingrese el tamaño")
            else:
                muestra_aleatoria = Distance_correlation()
                muestra_aleatoria.x = np.random.uniform(-1,1,int(self.tamano.text()))
                muestra_aleatoria.y = np.random.uniform(-1,1,int(self.tamano.text()))
                self.x = muestra_aleatoria.x
                self.y = muestra_aleatoria.y
                muestra_aleatoria.calculateDistanceCorrelation(int(self.tamano.text()))
                self.distance_number.display(muestra_aleatoria.distance_correlation)
                self.label = "Muestra aleatoria de tamaño: "+str(self.tamano.text())
                self.tipo_entrada.setText(self.label)
                self.undo = [muestra_aleatoria.distance_correlation,self.label,"numero"]
                self.pila.push(self.undo)
        if self.listas.isChecked() == True:
            if self.tamano.text()=="":
                print("error")
                QMessageBox.about(self, "Error", "Porfavor ingrese el tamaño")
            else:
                self.x = []
                self.y = []
                muestra_aleatoria = Distance_correlation_list()
                for i in range(int(self.tamano.text())):
                    a = random.uniform(-1, 1)
                    b = random.uniform(-1, 1)
                    muestra_aleatoria.x.append(a)
                    muestra_aleatoria.y.append(b)
                    self.x.append(a)
                    self.y.append(b)
                muestra_aleatoria.calculateDistanceCorrelation(int(self.tamano.text()))
                self.distance_number.display(muestra_aleatoria.distance_correlation)
                self.label = "Muestra aleatoria de tamaño: "+str(self.tamano.text())
                self.tipo_entrada.setText(self.label)
                self.undo = [muestra_aleatoria.distance_correlation,self.label,"numero"]
                self.pila.push(self.undo)
                
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '../data')
        if filePath != "":
            print ("Dirección",filePath)
            self.df = pd.read_csv(str(filePath))
            self.csv = True
    def calcularArchivo(self):
        if self.arrays.isChecked() == True:
            if self.csv == True:
                locale.setlocale(locale.LC_ALL, '')
                muestra_archivo = Distance_correlation()
                muestra_archivo.x = np.zeros(len(self.df.index))
                muestra_archivo.y = np.zeros(len(self.df.index))
                for i in range(len(self.df.index)):
                    muestra_archivo.x[i] = locale.atof(self.df.loc[i]["x"])
                    muestra_archivo.y[i] = locale.atof(self.df.loc[i]["y"])
                self.x = muestra_archivo.x
                self.y = muestra_archivo.y
                muestra_archivo.calculateDistanceCorrelation(len(muestra_archivo.x))
                self.distance_number.display(muestra_archivo.distance_correlation)
                self.label = "Muestra aleatoria de archivo csv"
                self.tipo_entrada.setText(self.label)
                self.undo = [muestra_archivo.distance_correlation,self.label,"numero"]
                self.pila.push(self.undo)
            else:
                print("error")
                QMessageBox.about(self, "Error", "Archivo csv no cargado aún")
        if self.listas.isChecked() == True:
            if self.csv == True:
                self.x = []
                self.y = []
                muestra_archivo = Distance_correlation_list()
                for i in range(len(self.df.index)):
                    muestra_archivo.x.append(locale.atof(self.df.loc[i]["x"]))
                    muestra_archivo.y.append(locale.atof(self.df.loc[i]["y"]))
                    self.x.append(locale.atof(self.df.loc[i]["x"]))
                    self.y.append(locale.atof(self.df.loc[i]["y"]))
                muestra_archivo.calculateDistanceCorrelation(len(self.df.index))
                self.distance_number.display(muestra_archivo.distance_correlation)
                self.label="Muestra aleatoria de archivo csv"
                self.tipo_entrada.setText(self.label)
                self.undo = [muestra_archivo.distance_correlation,self.label,"numero"]
                self.pila.push(self.undo)
            else:
                print("error")
                QMessageBox.about(self, "Error", "Archivo csv no cargado aún")
    def plot(self):
        if self.arrays.isChecked() == True:
            if self.x != []: 
                self.qmc.setParent(None)
                self.ntb.setParent(None)
                #Se instancia el Lienzo con la grafica de Matplotlib
                self.qmc = Lienzo(self.grafica,self.x,self.y,self.label)
                # se instancia la barra de navegacion
                self.ntb = NavigationToolbar(self.qmc, self.grafica)
                #la barra de navegacion en el vbox
                self.vbl.addWidget(self.qmc)
                self.vbl.addWidget(self.ntb)
                self.pila.push([self.x,self.y,self.label,"grafica"])
                print("grafica mostrada al usuario")
            else:
                print("error")
                QMessageBox.about(self, "Error", "Primero debe calcular el coeficiente")
        if self.listas.isChecked() == True:
            if self.x != []: 
                self.qmc.setParent(None)
                self.ntb.setParent(None)
                #Se instancia el Lienzo con la grafica de Matplotlib
                self.qmc = Lienzo(self.grafica,self.x,self.y,self.label)
                # se instancia la barra de navegacion
                self.ntb = NavigationToolbar(self.qmc, self.grafica)
                #la barra de navegacion en el vbox
                self.vbl.addWidget(self.qmc)
                self.vbl.addWidget(self.ntb)
                print("grafica mostrada al usuario")
            else:
                print("error")
                QMessageBox.about(self, "Error", "Primero debe calcular el coeficiente")
    def toggle(self):
        self._toggle = not self._toggle
        self.arrays.setChecked(self._toggle)
        self.listas.setChecked(not self._toggle)
    def undoActions(self):
        if self.pila.empty()==False:            
            self.pila2.push(self.pila.pop())
            if self.pila.top()[-1] == "numero": 
                if self.pila.size()>=1:
                    actions = self.pila.top()
                    self.distance_number.display(actions[0])
                    self.tipo_entrada.setText(actions[1])
            if self.pila.top()[-1] == "grafica":
                if self.pila.size()>=1:
                    actions = self.pila.top()
                    self.qmc.setParent(None)
                    self.ntb.setParent(None)
                    #Se instancia el Lienzo con la grafica de Matplotlib
                    self.qmc = Lienzo(self.grafica,actions[0],actions[1],actions[2])
                    # se instancia la barra de navegacion
                    self.ntb = NavigationToolbar(self.qmc, self.grafica)
                    #la barra de navegacion en el vbox
                    self.vbl.addWidget(self.qmc)
                    self.vbl.addWidget(self.ntb)
    def doActions(self):
        if self.pila2.empty()==False:            
            self.pila2.pop()
            if self.pila2.top()[-1] == "numero": 
                if self.pila2.size()>=1:
                    actions = self.pila2.top()
                    self.distance_number.display(actions[0])
                    self.tipo_entrada.setText(actions[1])
            if self.pila2.top()[-1] == "grafica":
                if self.pila2.size()>=1:
                    actions = self.pila2.top()
                    self.qmc.setParent(None)
                    self.ntb.setParent(None)
                    #Se instancia el Lienzo con la grafica de Matplotlib
                    self.qmc = Lienzo(self.grafica,actions[0],actions[1],actions[2])
                    # se instancia la barra de navegacion
                    self.ntb = NavigationToolbar(self.qmc, self.grafica)
                    #la barra de navegacion en el vbox
                    self.vbl.addWidget(self.qmc)
                    self.vbl.addWidget(self.ntb)
        
class Lienzo(FigureCanvas):
    x = []
    y = []
    def __init__(self, parent,x,y,label):
        # Se instancia el objeto figure
        self.fig = Figure()
        #Se define la grafica en coordenadas polares
        self.axes = self.fig.add_subplot(1,1,1)
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
        self.axes.plot(self.x,self.y,"o",label=label)
        self.axes.set_title(label)
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
    
