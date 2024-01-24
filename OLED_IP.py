from time import sleep

# Import all board pins.
from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306

# Additional imports for getting IP address
import socket
import fcntl
import struct

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)
# Alternatively, you can change the I2C address of the device with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Function to get IP address
def get_ip(interface='wlan0'):
    try:
        # Get the IP address of the specified interface
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = socket.inet_ntoa(fcntl.ioctl(
            sock.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15].encode())
        )[20:24])

        return ip_address
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to display IP address on OLED
def display_ip():
    wlan_ip = get_ip()

    if wlan_ip:
        # Clear the display
        display.fill(0)

        # Display the IP address
        display.text("IP Address:", 0, 0, 1)
        display.text(wlan_ip, 0, 10, 1)

        # Update the OLED display
        display.show()
    else:
        print("Unable to retrieve and display IP address.")

# Display IP address on OLED
time=60
i=5
while i>0:
    time.sleep(time)
    display_ip()
    i-=1
    sleep(time)