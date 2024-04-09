from mainui import *
#pyuic5 -x .\ejemplo_2.ui -o ejemplo_2.py

# class Ui_GroupBox(Ui_GroupBox):
#     pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)

        #UICODE
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()