from gpiozero import Servo
from time import sleep
 
myGPIO=17
 
myCorrection=0.55
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
        sleep(2)
# while True:
#     servo.mid()
#     print("mid")
#     sleep(1)
#     servo.min()
#     print("min")
#     sleep(1)
#     servo.mid()
#     print("mid")
#     sleep(1)
#     servo.max()
#     print("max")
#     sleep(1)