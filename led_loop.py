# import RPi.GPIO as GPIO
# from time import sleep

# # Set the GPIO mode to BCM (Broadcom SOC channel)
# # Set the GPIO mode to BOARD (physical pin numbering)
# GPIO.setmode(GPIO.BOARD)

# # Set up GPIO pin 11 as an output
# led_pin = 11
# GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
# while True:
#     try:
#         # Turn on the LED
#         GPIO.output(led_pin, GPIO.HIGH)
#         print("LED on")
#         # Wait for a few seconds (you can adjust the duration)
#         sleep(5)

#     finally:
#         # Turn off the LED and clean up GPIO settings
#         GPIO.output(led_pin, GPIO.LOW)
#         print("LED off")
#         GPIO.cleanup()

# import gpiod
# import time
# LED_PIN = 17
# chip = gpiod.Chip('gpiochip4')
# led_line = chip.get_line(LED_PIN)
# led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
# try:
#    while True:
#        led_line.set_value(1)
#        time.sleep(1)
#        led_line.set_value(0)
#        time.sleep(1)
# finally:
#    led_line.release()

from gpiozero import LED
from time import sleep

# Create an LED object for GPIO pin 11
led = LED(17)  # Use the GPIO pin number, not the physical pin number
try:
    while True:
        # Turn on the LED
        led.on()
        print("LED on")
        # Wait for a few seconds
        sleep(1)
        # Turn off the LED
        led.off()
        print("LED off")
        # Wait for a few seconds
        sleep(1)
except KeyboardInterrupt:
    # If the user presses Ctrl+C, gracefully exit the loop
    print("\nExiting the program.")
finally:
    # Turn off the LED and clean up
    led.off()
    print("LED off")
