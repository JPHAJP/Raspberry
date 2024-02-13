#https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
from gpiozero import Servo
from time import sleep
 
myGPIO=17 
myCorrection=0.3
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

while True:
    value = input("Enter a value between -1 and 1: ")
    value = float(value)
    if value < -1 or value > 1:
        print("Invalid input")
    else:
        servo.value = value
        sleep(1)