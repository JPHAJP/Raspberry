from gpiozero import LED
from time import sleep

led = LED(17)  # Use the GPIO pin number, not the physical pin number
time=0.1
direction=1
try:
    while True:
        led.on()
        print("LED on")
        sleep(time)
        led.off()
        print("LED off")
        sleep(time)
        if time < 0.1:
            direction = 1
        elif time > 1:
            direction = -1
        time += 0.1*direction
        print(f'LED on for {time} seconds')

except KeyboardInterrupt:
    # If the user presses Ctrl+C, gracefully exit the loop
    print("\nExiting the program.")
finally:
    # Turn off the LED and clean up
    led.off()
    print("LED off")
