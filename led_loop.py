# from gpiozero import LED
# from time import sleep

# # Create an LED object for GPIO pin 11
# led = LED(17)  # Use the GPIO pin number, not the physical pin number
# try:
#     while True:
#         # Turn on the LED
#         led.on()
#         print("LED on")
#         # Wait for a few seconds
#         sleep(1)
#         # Turn off the LED
#         led.off()
#         print("LED off")
#         # Wait for a few seconds
#         sleep(1)
# except KeyboardInterrupt:
#     # If the user presses Ctrl+C, gracefully exit the loop
#     print("\nExiting the program.")
# finally:
#     # Turn off the LED and clean up
#     led.off()
#     print("LED off")

#------------------------------------#

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
