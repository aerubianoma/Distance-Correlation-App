import sys
from UI_PY import *
from PyQt5.QtWidgets import QDialog
from all_class import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.distance_label.setText("presioname")
        self.calculate_buttom.clicked.connect(self.actualizar)  
    def actualizar(self):
        prueba = Distance_correlation()
        prueba.x = np.random.uniform(-1,1,100)
        prueba.y = np.random.uniform(-1,1,100)
        prueba.calculateDistanceCorrelation(100)
        self.distance_label.setText(str(prueba.distance_correlation))
        

