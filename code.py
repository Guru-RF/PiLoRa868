import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
import config
import sys
import os
import binascii

sys.path.insert(0, os.getcwd() + "/lib")
import adafruit_rfm9x


print("Intializing µPico")

rf1 = DigitalInOut(board.D13)
rf1.direction = Direction.OUTPUT

rf1.value = True

rf2 = DigitalInOut(board.D19)
rf2.direction = Direction.OUTPUT

rf2.value = True
time.sleep(0.25)
rf2.value = False

# Lora Stuff
RADIO_FREQ_MHZ = 868.000
CS = DigitalInOut(board.D7)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000, agc=False,crc=True)
rfm9x.tx_power = 5

rfm9x.send(
                bytes("{}".format("<"), "UTF-8") + binascii.unhexlify("AA") + binascii.unhexlify("01") +
                bytes("{}".format('sw0/8'), "UTF-8")
            )
