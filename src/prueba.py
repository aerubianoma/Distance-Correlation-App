import sys
from Prueba_UI_PY import *
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
        prueba.x = np.random.uniform(-1,1,10000)
        prueba.y = np.random.uniform(-1,1,10000)
        prueba.calculateDistanceCorrelation(10000)
        self.distance_label.setText(str(prueba.distance_correlation))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()