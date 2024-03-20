from temp_5 import *
from time import sleep
import random
from datetime import datetime

global data
data = []
#pyuic6 -x .\ejemplo_2.ui -o ejemplo_2.py

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
        #My code
        self.input_data.setText("0")
        self.data_label.setText("Historic:")

        self.Max_slider.valueChanged.connect(self.change_value)
        self.Min_slider.valueChanged.connect(self.change_value)
        self.Set_button.clicked.connect(self.set_data)
        self.Historic_button.clicked.connect(self.historic_data)
        self.Last_button.clicked.connect(self.last_data)
        self.Reset_button.clicked.connect(self.reset_values)
        self.comboBox.currentIndexChanged.connect(self.selection_change)

    def selection_change(self):
        if self.comboBox.currentText() == "Temperature":
            self.Max_slider.setMaximum(40)
            self.Max_slider.setMinimum(-10)
            self.Min_slider.setMaximum(40)
            self.Min_slider.setMinimum(-10)
            self.Max_slider.setValue(0)
            self.Min_slider.setValue(0)
        elif self.comboBox.currentText() == "Humidity":
            self.Max_slider.setMaximum(80)
            self.Max_slider.setMinimum(20)
            self.Min_slider.setMaximum(80)
            self.Min_slider.setMinimum(20)
            self.Max_slider.setValue(30)
            self.Min_slider.setValue(30)
        elif self.comboBox.currentText() == "Pressure":
            self.Max_slider.setMaximum(103)
            self.Max_slider.setMinimum(99)
            self.Min_slider.setMaximum(103)
            self.Min_slider.setMinimum(99)
            self.Max_slider.setValue(100)
            self.Min_slider.setValue(100)
           
    def reset_values(self):
        self.comboBox.setCurrentIndex(0)
        self.Max_slider.setValue(0)
        self.Min_slider.setValue(0)
        self.input_data.setText("0")
        self.data_label.setText("Historic:")
        #clean data
        #clean qlistwidget List_Data
        self.List_data.clear()
 
    def change_value(self):
        self.min_label.setText(str(self.Min_slider.value()))
        self.max_label.setText(str(self.Max_slider.value()))
    
    def set_data(self):
        try:
            elements = int(self.input_data.toPlainText())
        except:
            elements = 0
        self.data_gen(elements)
        self.data_label.setText("Historic:")

    def last_data(self):
        self.data_label.setText("Last:")
        #show last data
        global data
        if len(data) > 0:
            self.List_data.addItem(f"{data[-1][0]}°C, {data[-1][1]}%, {data[-1][2]}kPa, {data[-1][3]}")
        else:
            self.List_data.addItem("No data")
    
    def historic_data(self):
        self.data_label.setText("Historic:")
        global data
        for i in range(len(data)):
            self.List_data.addItem(f"{data[i][0]}°C, {data[i][1]}%, {data[i][2]}kPa, {data[i][3]}")

    def data_gen(self, elements):
        global data
        for _ in range(elements):
            t=self.sensor_temp()
            h=self.sensor_humedad()
            p=self.sensor_presion()
            date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data.append([t,h,p,date])
            sleep(0.1)
    def sensor_temp(self):
        return round(random.uniform(-10,40),2)
        #aprox en puebla 16°C
    def sensor_humedad(self):
        return round(random.uniform(40,80),2)
        #aprox en puebla 60%
    def sensor_presion(self):
        return round(random.uniform(99,103),2)

            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()