from temp_5 import *
from time import sleep
import random
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

#pyuic6 -x .\ejemplo_2.ui -o ejemplo_2.py

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
        #My code
        self.data_list=[]

        #Firebase
        cred = credentials.Certificate("Interfaces\Temp_UI\serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

        db=firestore.client()
        self.clima_ref=db.collection('clima')
        self.actual_ref=db.collection('actuales').document('zsvSEgB2aB1LqNPMdFC0')

        #Interface
        self.input_data.setText("0")
        self.data_label.setText("Historic:")

        self.Max_slider.valueChanged.connect(self.change_value)
        self.Min_slider.valueChanged.connect(self.change_value)
        self.Set_button.clicked.connect(self.set_data)
        self.Historic_button.clicked.connect(self.historic_data)
        self.Last_button.clicked.connect(self.last_data)
        self.Reset_button.clicked.connect(self.reset_values)
        self.comboBox.currentIndexChanged.connect(self.selection_change)
        self.clean_button.clicked.connect(self.List_data.clear)


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
        if self.Max_slider.value() < self.Min_slider.value():
            self.Max_slider.setValue(self.Min_slider.value())
        self.min_label.setText(str(self.Min_slider.value()))
        self.max_label.setText(str(self.Max_slider.value()))
    
    def set_data(self):
        try:
            elements = int(self.input_data.toPlainText())
        except:
            elements = 0
        self.data_gen(elements)
        if elements == 0:
            print("No data")
            self.List_data.addItem("No data")
        else:
            try:
                self.db_create()
                self.db_update_last()
            except:
                print("No connection")
        self.data_label.setText("Historic:")

    def db_create(self):
        for i in range(len(self.data)):
            self.clima_ref.document().set({
                'temp':self.data[i][0],
                'hum':self.data[i][1],
                'pres':self.data[i][2],
                'datetime':self.data[i][3]
            })
        print("Data added")

    def db_update_last(self):
        self.actual_ref.update({
            'temp':self.data[-1][0],
            'hum':self.data[-1][1],
            'pres':self.data[-1][2],
            'datetime':self.data[-1][3],
            'led':True
        })
        print(f"Last updated {self.data[-1]}")

    def last_data(self):
        self.data_label.setText("Last:")
        #show last data
        #Firebase
        data = self.actual_ref.get().to_dict()
        print(f"Last data: {data}")
        self.List_data.addItem(f"{data['temp']}°C, {data['hum']}%, {data['pres']}kPa, {data['datetime']}")



        # global data
        # if len(data) > 0:
        #     self.List_data.addItem(f"{data[-1][0]}°C, {data[-1][1]}%, {data[-1][2]}kPa, {data[-1][3]}")
        # else:
        #     self.List_data.addItem("No data")
    
    def historic_data(self):
        self.data_label.setText("Historic:")
        filtered_data = []
        if self.comboBox.currentText() == "Temperature":
            j=0
        elif self.comboBox.currentText() == "Humidity":
            
            j=1
        elif self.comboBox.currentText() == "Pressure":
            j=2
        else:
            j=0

        data=self.clima_ref.get()
        for doc in data:
            if doc.to_dict()[self.comboBox.currentText().lower()] >= self.Min_slider.value() and doc.to_dict()[self.comboBox.currentText().lower()] <= self.Max_slider.value():
                filtered_data.append(doc.to_dict())
        if filtered_data == []:
            self.List_data.addItem("No data")
        else:
            for i in range(len(filtered_data)):
                self.List_data.addItem(f"{filtered_data[i]['temp']}°C, {filtered_data[i]['hum']}%, {filtered_data[i]['pres']}kPa, {filtered_data[i]['datetime']}")

        # for i in range(len(self.data)):
        #     if self.data[i][j] >= self.Min_slider.value() and self.data[i][j] <= self.Max_slider.value():
        #         filtered_data.append(self.data[i])
        # if filtered_data == []:
        #     self.List_data.addItem("No data")
        # else:
        #     for i in range(len(filtered_data)):
        #         self.List_data.addItem(f"{filtered_data[i][0]}°C, {filtered_data[i][1]}%, {filtered_data[i][2]}kPa, {filtered_data[i][3]}")

    def data_gen(self, elements):
        for _ in range(elements):
            t=self.sensor_data_gen(-10,40)
            h=self.sensor_data_gen(20,80)
            p=self.sensor_data_gen(99,103)
            date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data.append([t,h,p,date])
        print(f"Data generated: {self.data}")
    
    def sensor_data_gen(self,max,min):
        return round(random.uniform(max,min),2)
        #aprox en puebla 16°C, 60%, 100kPa

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()