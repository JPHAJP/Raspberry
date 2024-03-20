from ColorPicker_5 import *
#from gpiozero import RGBLED

from time import sleep

#add adafruit neopixel library
#sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
#sudo python3 -m pip install --force-reinstall adafruit-blinka
#sudo pip3 install adafruit-circuitpython-neopixel
#sudo pip3 install rpi_ws281x
#from neopixel import NeoPixel
#import board

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
#pixel_pin = board.D18


#led = RGBLED(red=17, green=27, blue=22)  # Use the GPIO pin number, not the physical pin number 

#pyuic6 -x .\ejemplo_2.ui -o ejemplo_2.py

#led=RGBLED(17,27,22)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args, **kwargs)
        self.setupUi(self)
        #My code
        self.dial_r.setMinimum(0)
        self.dial_r.setMaximum(255)
        self.dial_g.setMinimum(0)
        self.dial_g.setMaximum(255)
        self.dial_b.setMinimum(0)
        self.dial_b.setMaximum(255)
        self.slider_br.setMinimum(0)
        self.slider_br.setMaximum(100)

        self.set_values_color()
        self.set_values_brighness()
        
        self.dial_r.valueChanged.connect(self.choose_red)
        self.dial_g.valueChanged.connect(self.choose_green)
        self.dial_b.valueChanged.connect(self.choose_blue)
        self.slider_br.valueChanged.connect(self.choose_brighness)
        self.Colo_R.triggered.connect(self.set_values_color)
        self.Brightness_R.triggered.connect(self.set_values_brighness)

    def set_values_color(self):
        self.dial_r.setValue(0)
        self.lcdNumber_R.display(0)
        self.dial_g.setValue(0)
        self.lcdNumber_g.display(0)
        self.dial_b.setValue(0)
        self.lcdNumber_b.display(0)
        self.choose_color()
    
    def set_values_brighness(self):
        self.slider_br.setValue(0)
        self.lcdNumber_br.display(0)
        self.choose_color()
   
    def choose_red(self):
        red = self.dial_r.value()
        self.lcdNumber_R.display(red)
        self.choose_color()

    def choose_green(self):
        green = self.dial_g.value()
        self.lcdNumber_g.display(green)
        self.choose_color()
        
    def choose_blue(self):
        blue = self.dial_b.value()
        self.lcdNumber_b.display(blue)
        self.choose_color()
    
    def choose_brighness(self):
        brighness = self.slider_br.value()
        self.lcdNumber_br.display(brighness)
        self.choose_color()

    def choose_color(self):
        red = self.dial_r.value()
        green = self.dial_g.value()
        blue = self.dial_b.value()
        brighness = self.slider_br.value()
        red = int(red * (brighness / 100))
        green = int(green * (brighness / 100))
        blue = int(blue * (brighness / 100))
        #led.value=(red/255,green/255,blue/255)
        #print(f"RGB: {red}, {green}, {blue}")

        self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue});")
        #led.red = red/255
        #led.green = green/255
        #led.blue = blue/255

        if (brighness <= 50) or (red < 125 and green < 125 and blue < 125):
            self.label_r.setStyleSheet("color: rgb(255, 255, 255)")
            self.label_g.setStyleSheet("color: rgb(255, 255, 255)")
            self.label_b.setStyleSheet("color: rgb(255, 255, 255)")
            self.label_tt.setStyleSheet("color: rgb(255, 255, 255)")
            self.label_br.setStyleSheet("color: rgb(255, 255, 255)")
            self.menubar.setStyleSheet("color: rgb(255, 255, 255)")
            self.menuReset.setStyleSheet("color: rgb(255, 255, 255)")
        else:
            self.label_r.setStyleSheet("color: rgb(0, 0, 0)")
            self.label_g.setStyleSheet("color: rgb(0, 0, 0)")
            self.label_b.setStyleSheet("color: rgb(0, 0, 0)")
            self.label_tt.setStyleSheet("color: rgb(0, 0, 0)")
            self.label_br.setStyleSheet("color: rgb(0, 0, 0)")
            self.menubar.setStyleSheet("color: rgb(0, 0, 0)")
            self.menuReset.setStyleSheet("color: rgb(0, 0, 0)")
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Window = MainWindow()
    Window.show()
    app.exec()