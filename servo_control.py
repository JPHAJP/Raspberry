# from gpiozero import AngularServo
# from time import sleep
# servo = AngularServo(17, min_angle=-90, max_angle=90)
# while True:
#     servo.angle = -90
#     sleep(2)
#     servo.angle = 0
#     sleep(2)
#     servo.angle = 90
#     sleep(2)


# while True:
#     servo.min()
#     sleep(1)
#     servo.mid()
#     sleep(1)
#     servo.max()
#     sleep(1)

# from gpiozero import Servo
# from time import sleep

# servo = Servo(17)
# while True:
#     value = input("Enter a value between -1 and 1: ")
#     value = float(value)
#     servo.value = value
#     sleep(2)

#     # if value < -1 or value > 1:
#     #     print("Invalid input")
#     # else:
#     #     servo.value = value
#     #     sleep(2)

from gpiozero import Servo
from time import sleep
 
myGPIO=17
 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
 
while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)