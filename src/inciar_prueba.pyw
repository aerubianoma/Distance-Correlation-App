import sys
from Prueba_UI_PY import *
from PyQt5.QtWidgets import QDialog

class MiFormulario(QtWidgets.QDialog):
  def __init__(self, parent=None):
    QtWidgets.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   myapp = MiFormulario()
   myapp.show()
   sys.exit(app.exec_())

