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

from gpiozero import Servo
from time import sleep

servo = Servo(17)
value = input("Enter a value between -1 and 1: ")

if value < -1 or value > 1:
    print("Invalid input")
else:
    servo.value = value
    sleep(2)