import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode to BCM (Broadcom SOC channel)
# Set the GPIO mode to BOARD (physical pin numbering)
GPIO.setmode(GPIO.BOARD)

# Set up GPIO pin 11 as an output
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
while True:
    try:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED on")
        # Wait for a few seconds (you can adjust the duration)
        sleep(5)

    finally:
        # Turn off the LED and clean up GPIO settings
        GPIO.output(led_pin, GPIO.LOW)
        print("LED off")
        GPIO.cleanup()