import socket, cv2, pickle, struct, imutils, time, firebase_admin, qrcode, os, serial
from mainui import *
from datetime import datetime
from firebase_admin import credentials, firestore
#import numpy as np
#from ultralytics import YOLO
from PyQt5.QtCore import QTimer, QObject, pyqtSignal, QThread, pyqtSlot
from PyQt5.QtGui import QPainter, QPen, QColor, QImage, QPixmap
#from PyQt5.QtWidgets import QLabel


#pyuic5 -x .\ejemplo_2.ui -o ejemplo_2.py

# class Ui_GroupBox(Ui_GroupBox):
#     pass

global estado_pantalla
class CameraThread(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, estado_pantalla):
        super().__init__()
    
    def run(self):
        #host_ip = '172.18.141.91'      #rasp
        host_ip = '172.18.59.33'       #jplaptop
        # try:
        #     client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #     port = 9999
        #     client_socket.connect((host_ip,port)) # a tuple
        #     data = b""
        #     payload_size = struct.calcsize("Q")
        # except:
        #     print('Error en la conexiónn al servidor no se puede iniciar la cámara')
        #     pass
        
        
        # while True:
        #     try:
        #         while len(data) < payload_size:
        #             packet = client_socket.recv(4*1024) # 4K
        #             if not packet: break
        #             data+=packet
        #         packed_msg_size = data[:payload_size]
        #         data = data[payload_size:]
        #         msg_size = struct.unpack("Q",packed_msg_size)[0]
                
        #         while len(data) < msg_size:
        #             data += client_socket.recv(4*1024)
        #         frame_data = data[:msg_size]
        #         data  = data[msg_size:]
        #         frame = pickle.loads(frame_data)
        #     except:
        #         print('Error en la conexión al servidor')
        #         pass

            #-----------------------------------#
        #cap = cv2.VideoCapture(0)
        #model = YOLO(r'best.pt')
        # while True:
        #     prev_time = time.time()
        #     time_elapsed = time.time() - prev_time
        #     if time_elapsed > 1./5:
        #     #     rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     #     #results = model(rgbImage, conf=0.6)
        #     #     #rgbImage = results[0].plot()
        #     #     h, w, ch = rgbImage.shape
        #     #     bytesPerLine = ch * w
        #     #     convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
        #     #     p = convertToQtFormat.scaled(410, 320)
        #     #     self.changePixmap.emit(p)
        #         print('hola')
        #         prev_time = time.time()
        #     print('adios')
        #     status=self.cam_ref.get().to_dict('status')
        #     print(status)
        #     if status:
        #         data = self.cam_ref.get().to_dict()
        #         print(data)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
    #UICODE
        #QR
        self.qr_file_path = os.path.join("Interfaces","ProyectoUI","resources", "qr.png")
        print(self.qr_file_path)
        
        #Firebase
        cred = credentials.Certificate('Interfaces\ProyectoUI\pan-orama-back.json')
        firebase_admin.initialize_app(cred)
        db=firestore.client()
        self.panes_ref=db.collection('panes')
        self.cam_ref=db.collection('cam').document('tultntOMopOIwT9B12Yz')
        self.ordenes_ref=db.collection('ordenes')
        self.totales_ref=db.collection('totales').document('Bdak4QvaeHgGgvgcaq6O')
        self.last_ref=db.collection('last').document('7h9DXtyHl9Ewi5zHL9wy')

    #-----------UPDATE----------------#
        self.reset()
        self.precios_update()

        self.stackedWidget.setCurrentIndex(0)
        self.order_num=self.last_ref.get().to_dict()['order']
        self.update_order(0)   

        #Parámetros del modelo:
        #self.cam_num = 0
        #self.pre_model = r'AAA.pt'
        self.flag = False
        self.activate = False
        #self.camera = cv2.VideoCapture(0)
        #self.model = YOLO(r'best.pt')

        #Parámetros de la interfaz:
        #self.label = QtWidgets.QLabel(self)
        #self.label.setGeometry(50, 50, 700, 540)
        #self.pushButton.clicked.connect(self.close_popup)

        self.th = CameraThread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()

    #-----------PANTALLAS----------------#
    #Pantalla 0 Inicio
        self.empezar_button.clicked.connect(lambda: self.cambiar_pantalla(1))

    #Pantalla 1 Cam
        self.revisar_button.clicked.connect(lambda: self.cambiar_pantalla(2))

    #Pantalla 2 Cart
        self.generar_button.clicked.connect(lambda: self.cambiar_pantalla(3))
        self.generar_button.clicked.connect(self.create_order_db)
        self.editar_button.clicked.connect(lambda: self.cambiar_pantalla(4))
        self.minus_button0.clicked.connect(lambda: self.restar(0))
        self.plus_button0.clicked.connect(lambda: self.sumar(0))
        self.minus_button1.clicked.connect(lambda: self.restar(1))
        self.plus_button1.clicked.connect(lambda: self.sumar(1))
        self.minus_button2.clicked.connect(lambda: self.restar(2))
        self.plus_button2.clicked.connect(lambda: self.sumar(2))
        self.minus_button3.clicked.connect(lambda: self.restar(3))
        self.plus_button3.clicked.connect(lambda: self.sumar(3))
        self.minus_button4.clicked.connect(lambda: self.restar(4))
        self.plus_button4.clicked.connect(lambda: self.sumar(4))
        self.minus_button5.clicked.connect(lambda: self.restar(5))
        self.plus_button5.clicked.connect(lambda: self.sumar(5))
        self.minus_button6.clicked.connect(lambda: self.restar(6))
        self.plus_button6.clicked.connect(lambda: self.sumar(6))
        self.minus_button7.clicked.connect(lambda: self.restar(7))
        self.plus_button7.clicked.connect(lambda: self.sumar(7))
        self.minus_button8.clicked.connect(lambda: self.restar(8))
        self.plus_button8.clicked.connect(lambda: self.sumar(8))
        self.minus_button9.clicked.connect(lambda: self.restar(9))
        self.plus_button9.clicked.connect(lambda: self.sumar(9))
        self.minus_button10.clicked.connect(lambda: self.restar(10))
        self.plus_button10.clicked.connect(lambda: self.sumar(10))
        #self.trash_button_ejemplo.clicked.connect(self.eliminar)
        
    #Pantalla 3 Ticket
        self.terminar_button.clicked.connect(self.get_new_order)
        self.terminar_button.clicked.connect(lambda: self.cambiar_pantalla(0))
        self.terminar_button.clicked.connect(self.reset)
        

    #Pantalla 4 Auth
        self.ingresar_button.clicked.connect(self.autenticar)
        self.regresar_button.clicked.connect(lambda: self.cambiar_pantalla(2))
        #Button array
        self.button_num_0.clicked.connect(lambda: self.button_pushed(0))
        self.button_num_1.clicked.connect(lambda: self.button_pushed(1))
        self.button_num_2.clicked.connect(lambda: self.button_pushed(2))
        self.button_num_3.clicked.connect(lambda: self.button_pushed(3))
        self.button_num_4.clicked.connect(lambda: self.button_pushed(4))
        self.button_num_5.clicked.connect(lambda: self.button_pushed(5))
        self.button_num_6.clicked.connect(lambda: self.button_pushed(6))
        self.button_num_7.clicked.connect(lambda: self.button_pushed(7))
        self.button_num_8.clicked.connect(lambda: self.button_pushed(8))
        self.button_num_9.clicked.connect(lambda: self.button_pushed(9))
        self.button_delete.clicked.connect(lambda: self.button_pushed(10))

    #Pantalla 5 Productos
        self.bolillo_button_add.clicked.connect     (lambda: self.productos(0))
        self.telera_button_add.clicked.connect      (lambda: self.productos(1))
        self.torta_button_add.clicked.connect       (lambda: self.productos(2))
        self.concha_button_add.clicked.connect      (lambda: self.productos(3))
        self.dona_button_add.clicked.connect        (lambda: self.productos(4))
        self.mantecada_button_add.clicked.connect   (lambda: self.productos(5))
        self.pinguino_button_add.clicked.connect    (lambda: self.productos(6))
        self.oreja_button_add.clicked.connect       (lambda: self.productos(7))
        self.reja_button_add.clicked.connect        (lambda: self.productos(8))
        self.rebanda_button_add.clicked.connect     (lambda: self.productos(9))
        self.cuernito_button_add.clicked.connect    (lambda: self.productos(10))
    

    #-----------FUNCTIONS----------------#

    def update_time(self,num):
        time_labels = [self.time_label_0, self.time_label_1, self.time_label_2, self.time_label_3, self.time_label_4]
        #time
        if num != 5:
            current_label = time_labels[num]
            current_label.setText(datetime.now().strftime("%H:%M %d-%m-%Y"))
        #orders
        
    def update_order(self,num):
        order_labels = [self.order_label_0, self.order_label_1, self.order_label_2, self.order_label_3]
        if num != 4 and num != 5:
            self.current_order = order_labels[num]
            self.current_order.setText(f'Orden: #{str(self.order_num)}')
        self.last_ref.update({'order':self.order_num})
        self.last_ref.update({'fecha':datetime.now().strftime("%H:%M %d-%m-%Y")})

    def get_new_order(self):
        #print('New order')
        if self.order_num[-8:] != datetime.now().strftime("%d%m%Y"):
            #print('New day')
            order = '1'+datetime.now().strftime("%d%m%Y")
        else:
            #print('Same day')
            order = int(self.order_num[:-8])
            order += 1
            order = str(order)+(datetime.now().strftime("%d%m%Y"))
        self.order_num = order
        #print(self.order_num)

    def cambiar_pantalla(self,num):
        global estado_pantalla
        estado_pantalla = num
        if num == 4 and self.admin==True:
            self.stackedWidget.setCurrentIndex(5)
        elif num == 3 and self.admin==True:
            self.admin = False
            self.stackedWidget.setCurrentIndex(num)
            self.editar_button.setText('Editar')
        elif num == 1:
            self.precios_update()
            self.cam_ref.update({'status':True})
            #self.mostrar_camara()
            self.stackedWidget.setCurrentIndex(num)
        else:
            self.cam_ref.update({'status':False})
            self.stackedWidget.setCurrentIndex(num)
            #self.camera.release()
        self.update_time(num)
        self.update_order(num)
        self.update_total_oder()
        #print(f'Pantalla {num}')
    
    def button_pushed(self, num):
        if num == 10:
            self.pss = self.pss[:-1]
        else:
            self.pss+=str(num)
        self.pass_label.setText('*'*len(self.pss))

    def autenticar(self):
        if self.pss == '1234':
            self.cambiar_pantalla(2)
            self.pss = ''
            self.pass_label.setText('')
            self.sudo()
        else:
            self.pss = ''
            self.pass_label.setText('Error')

    def sudo(self):
        self.editar_button.setText('Agregar')
        self.admin = True
        self.asistencia_requerida = 1
        #print(self.editar_button.text())

    def sumar(self, num):
        if self.admin == True:
            label = getattr(self,f'qty_label{num}')
            label.setText(str(int(label.text())+1))
        self.update_total_oder()

    def restar(self,num):
        if self.admin == True:
            label = getattr(self,f'qty_label{num}')
            if int(label.text()) > 0:
                label.setText(str(int(label.text())-1))
        self.update_total_oder()

    def update_total_oder(self):
        total_art = 0
        for i in range(11):
            label = getattr(self,f'qty_label{i}')
            total_art += int(label.text())
        self.articulos_label.setText(str(total_art))
        self.articulos_label_2.setText(str(total_art))

        total_price = 0
        for i in range(11):
            label = getattr(self,f'qty_label{i}')
            precio_label = getattr(self,f'precio_label{i}')
            total_price += int(label.text())*float(precio_label.text()[1:])
        self.total_label.setText(f'${total_price}')
        self.total_label_2.setText(f'${total_price}')

    def precios_update(self):
        #obtener precios de firebase y mostrarlos en sus labels
        self.precios = {}
        panes_docs = self.panes_ref.get()
        for doc in panes_docs:
            dato_pan = doc.to_dict()
            tipo_pan = dato_pan['Pan']
            precio_pan = dato_pan['Precio']
            self.precios[tipo_pan]=precio_pan
        #print(self.precios)
        #guardar precios en labels con diccionario de precios
        for i in range(11):
            precio_label = getattr(self,f'precio_label{i}')
            articulo_label = getattr(self,f'articulo_label{i}')

            tipo_pan = articulo_label.text()

            if tipo_pan in self.precios:
                precio_label.setText(f'${self.precios[tipo_pan]}')
            else:
                precio_label.setText('$0')
    
    def productos(self,num):
        print(f'Producto {num}')
        self.cambiar_pantalla(2)

    def reset(self):
        for i in range(11):
                label = getattr(self,f'qty_label{i}')
                label.setText('0')
                label_art = getattr(self,f'articulo_label{i}')
                art=label_art.text()
                if art == 'Pingüino':
                    art = 'Pinguino'
                self.cam_ref.update({art:0})
        self.update_total_oder()
        self.employee_code = 3987
        self.pss = ''
        self.pass_label.setText('')
        self.admin = False
        self.asistencia_requerida = 0

    def create_order_db(self):
        order_art = {}
        order_art['orden'] = int(self.order_num)
        order_art['venta'] = float(self.total_label.text()[1:])
        order_art['art'] = int(self.articulos_label.text())
        order_art['asistencia'] = self.asistencia_requerida
        for i in range(11):
            label = getattr(self,f'qty_label{i}')
            label_precio = getattr(self,f'precio_label{i}')
            if int(label.text()) > 0:
                articulo_label = getattr(self,f'articulo_label{i}')
                order_art[articulo_label.text()] = (int(label.text()),float(label_precio.text()[1:]))
        totales=self.totales_ref.get().to_dict()
        #print(totales)
        totales['ventas']+=1
        totales['ingresos']+=order_art['venta']
        totales['escaneos']+=order_art['art']
        totales['asistencia']+=order_art['asistencia']
        totales['d_ventas']+=1
        totales['d_ingresos']+=order_art['venta']
        totales['d_escaneos']+=order_art['art']
        totales['d_asistencia']+=order_art['asistencia']
        #print(totales)
        self.totales_ref.update(totales)
        #print(order_art)
        self.ordenes_ref.add(order_art)

        qr_data = str(order_art)
        qr = qrcode.make(qr_data, box_size=7.9)
        qr.save(self.qr_file_path)

        self.QR_code.setPixmap(QPixmap(self.qr_file_path))

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.cam.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()