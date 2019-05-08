import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16,GPIO.OUT)

pinIn = 12
pinOut = 16

def tryPin(pin):
    return bool(GPIO.input(pin))

def blinkPin(pin, pause):
    GPIO.output(pin, True)
    time.sleep(int(pause))
    GPIO.output(pin, False)
    time.sleep(int(pause))

def lightPin(pin):
    GPIO.output(pin, True)

try:
    while True:
        if tryPin(pinIn):
            lightPin(pinOut)
        else:
            blinkPin(pinOut, 1)

finally:
    GPIO.cleanup()


