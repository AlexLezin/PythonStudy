import RPi.GPIO as IO

import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

data_pin = 7 
latch_pin = 11 
clock_pin = 12 

IO.setup(data_pin, IO.OUT)
IO.setup(latch_pin, IO.OUT)
IO.setup(clock_pin, IO.OUT)

def lightUp(ledNum: int) -> int:
        print(ledNum)
        
s = input('Gimme somesthing!')
lightUp(s)
        
'''
while 1:                               # execute loop forever
    for y in range(8):            # loop for counting up 8 times
        IO.output(data_pin, 1)            # pull up the data pin for every bit.
        time.sleep(0.1)            # wait for 100ms
        IO.output(clock_pin, 1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(data_pin, 0)            # clear the DATA pin
        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(latch_pin, 0)            # pull down the SHIFT pin

    for y in range(8):            # loop for counting up 8 times
        IO.output(data_pin, 0)            # clear the DATA pin, to send 0
        time.sleep(0.1)            # wait for 100ms
        IO.output(clock_pin, 1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(data_pin, 0)            # keep the DATA bit low to keep the countdown
        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(latch_pin, 0)
'''
