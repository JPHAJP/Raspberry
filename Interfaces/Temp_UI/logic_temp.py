from temp_5 import *
from time import sleep

#pyuic6 -x .\ejemplo_2.ui -o ejemplo_2.py

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
        #My code
        self.input_data.setText("0")

        self.Max_slider.valueChanged.connect(self.change_value)
        self.Min_slider.valueChanged.connect(self.change_value)
        self.Set_button.clicked.connect(self.change_value)
        self.Reset_button.clicked.connect(self.reset_values)

        #self.set_values_color()
        #self.set_values_brighness()
        #self.dial_r.valueChanged.connect(self.choose_red)
    
    def reset_values(self):
        self.Max_slider.setValue(0)
        self.Min_slider.setValue(0)
        self.input_data.setText("0")
        self.data_label.setText("Historic:")
        #self.change_value()
 
    def change_value(self):
        self.min_label.setText(str(self.Min_slider.value()))
        self.max_label.setText(str(self.Max_slider.value()))
    
        elements = int(self.input_data.toPlainText())
        self.data_label.setText("Historic:")

    # def choose_green(self):
    #     green = self.dial_g.value()
    #     self.lcdNumber_g.display(green)
    #     self.choose_color()
        
    # def choose_blue(self):
    #     blue = self.dial_b.value()
    #     self.lcdNumber_b.display(blue)
    #     self.choose_color()
    
    # def choose_brighness(self):
    #     brighness = self.slider_br.value()
    #     self.lcdNumber_br.display(brighness)
    #     self.choose_color()

    # def choose_color(self):
    #     red = self.dial_r.value()
    #     green = self.dial_g.value()
    #     blue = self.dial_b.value()
    #     brighness = self.slider_br.value()
    #     red = int(red * (brighness / 100))
    #     green = int(green * (brighness / 100))
    #     blue = int(blue * (brighness / 100))
    #     self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue});")
    #     led.red = red/255
    #     led.green = green/255
    #     led.blue = blue/255

    #     if (brighness <= 50) or (red < 125 and green < 125 and blue < 125):
    #         self.label_r.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.label_g.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.label_b.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.label_tt.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.label_br.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.menubar.setStyleSheet("color: rgb(255, 255, 255)")
    #         self.menuReset.setStyleSheet("color: rgb(255, 255, 255)")
    #     else:
    #         self.label_r.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.label_g.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.label_b.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.label_tt.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.label_br.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.menubar.setStyleSheet("color: rgb(0, 0, 0)")
    #         self.menuReset.setStyleSheet("color: rgb(0, 0, 0)")
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()