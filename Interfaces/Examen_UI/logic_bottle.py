from bottle_analyzer import *
from time import sleep
import random
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

#pyuic5 -x .\ejemplo_2.ui -o ejemplo_2.py

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
        #My code
        self.data=[]

        #Firebase
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred)

        db=firestore.client()
        self.bottle_ref=db.collection('Bottle')

        #Interface
        self.input_data.setText("0")
        self.Max_slider.valueChanged.connect(self.change_value)
        self.Min_slider.valueChanged.connect(self.change_value)
        self.Set_button.clicked.connect(self.set_data)
        self.Last_button.clicked.connect(self.analizar)
        self.Reset_button.clicked.connect(self.reset_values)
        self.ClearDB_button.clicked.connect(self.db_clear)
           
    def reset_values(self):
        self.Max_slider.setValue(0)
        self.Min_slider.setValue(0)
        self.input_data.setText("0")
        #clean data
        #clean qlistwidget List_Data
        self.List_data.clear()
        self.listWidget.clear()
 
    def change_value(self):
        if self.Max_slider.value() < self.Min_slider.value():
            self.Max_slider.setValue(self.Min_slider.value())
        self.min_label.setText(str(self.Min_slider.value()))
        self.max_label.setText(str(self.Max_slider.value()))
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
            self.listWidget.addItem("No data")
        else:
            try:
                self.db_create()
            except:
                print("No connection")

    def db_create(self):
        for i in range(len(self.data)):
            self.bottle_ref.document().set({
                'Dato':self.data[i][0],
                'datetime':self.data[i][1]
            })
        print("Data added")
   
    def db_clear(self):
        db=firestore.client()
        docs = db.collection('Bottle').stream()

        # Delete each document
        for doc in docs:
            doc.reference.delete()
        print("Database cleaned")

    def analizar(self):
        self.List_data.clear()
        self.listWidget.clear()
        filtered_data_good = []
        filtered_data_wrong = []
        data=self.bottle_ref.order_by('datetime').get()
        for doc in data:
            if doc.to_dict()['Dato'] > self.Min_slider.value() and doc.to_dict()['Dato'] < self.Max_slider.value():
                filtered_data_good.append(doc.to_dict())
            else:
                filtered_data_wrong.append(doc.to_dict())
        
        
        if filtered_data_good == []:
            self.listWidget.addItem("No data")
        else:
            for i in range(len(filtered_data_good)):
                self.listWidget.addItem(f"Bottle at {filtered_data_good[i]['Dato']}%, {filtered_data_good[i]['datetime']}")

        if filtered_data_wrong == []:
            self.List_data.addItem("No data")
        else:
            for i in range(len(filtered_data_wrong)):
                self.List_data.addItem(f"Bottle at {filtered_data_wrong[i]['Dato']}%, {filtered_data_wrong[i]['datetime']}")

    def data_gen(self, elements):
        self.data=[]
        for i in range(elements):
            Datos=self.sensor_data_gen(40,100)
            Date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data.append([Datos,Date])
        print(f"Data generated: {self.data}")
    
    def sensor_data_gen(self,max,min):
        return round(random.uniform(max,min),2)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()