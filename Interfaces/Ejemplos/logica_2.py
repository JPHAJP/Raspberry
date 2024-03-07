from ejemplo_2 import *
#pyuic6 -x .\ejemplo_2.ui -o ejemplo_2.py


# class Ui_GroupBox(Ui_GroupBox):
#     pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)

        #mio
        self.Aum.clicked.connect(self.Aumentar)
        self.Dim.clicked.connect(self.Disminuir)
        self.lcdNumber.display(0)

    def Aumentar(self):
        try:
            valor = self.lcdNumber.intValue()
            self.label.setText(f"El valor es: {valor + 1}")
            self.lcdNumber.display(valor + 1)
        except:
            self.label.setText("El valor es demasiado grande")
    
    def Disminuir(self):
        valor = self.lcdNumber.intValue()
        self.label.setText(f"El valor es: {valor - 1}")
        self.lcdNumber.display(valor - 1)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()