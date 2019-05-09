import RPi.GPIO as IO
import time
import sys

IO.setwarnings(False)
IO.setmode(IO.BOARD)

data_pin = 7 
latch_pin = 11 
clock_pin = 12 

IO.setup(data_pin, IO.OUT)
IO.setup(latch_pin, IO.OUT)
IO.setup(clock_pin, IO.OUT)

def askForAction():
        ans1 = input("What do you want to do? (Up/Down) ")
        if ans1 == "Up":
                ans2 = int(input("Which one? (1-8) "))
                lightUp(ans2)
        elif ans1 == "Down":
                ans2 = int(input("Which one? (1-8) "))
                lightDown(ans2)
        elif ans1 == "Clear":
                clearAll()
        elif ans1 == "Pattern":
                lightPattern([0, 0, 1, 0, 0, 1, 0, 0])
        else:
                print("Invalid input")
                sys.exit()

def lightPattern(pattern: [int]):
        for i in pattern:
                if i == 1:
                        IO.output(data_pin, 1)
                       #time.sleep(0.1)
                        IO.output(clock_pin, 1)            # pull CLOCK pin high
                       #time.sleep(0.1)
                        IO.output(data_pin, 0)            # clear the DATA pin
                        #time.sleep(0.1)
                        IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
                       # time.sleep(0.1)
                        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
                        #time.sleep(0.1)
                        IO.output(latch_pin, 0) 
                elif i == 0:
                        IO.output(data_pin, 0)
                        #time.sleep(0.1)
                        IO.output(clock_pin, 1)            # pull CLOCK pin high
                        #time.sleep(0.1)
                        IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
                        #time.sleep(0.1)
                        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
                        #time.sleep(0.1)
                        IO.output(latch_pin, 0) 
                        

def lightUp(ledNum: int):
        IO.output(data_pin, 1)            # pull up the data pin for every bit.
        for i in range(ledNum):
                IO.output(clock_pin, 1)            # pull CLOCK pin high
                time.sleep(0.1)
                IO.output(data_pin, 0)            # clear the DATA pin
                time.sleep(0.1)
                IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
                time.sleep(0.1)
        time.sleep(0.1)
        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(latch_pin, 0)            # pull down the SHIFT pin
        
def lightDown(ledNum: int):
        IO.output(data_pin, 0)            # clear the DATA pin, to send 0
        for i in range(ledNum):
                IO.output(clock_pin, 1)            # pull CLOCK pin high
                IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
                IO.output(data_pin, 0)            # clear the DATA pin
       
        IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        IO.output(latch_pin, 0)            # pull down the SHIFT pin
   

def clearAll():
        for i in range(8):
                IO.output(data_pin, 0)            # clear the DATA pin, to send 0
                time.sleep(0.1)            # wait for 100ms
                IO.output(clock_pin, 1)            # pull CLOCK pin high
                time.sleep(0.1)
                IO.output(clock_pin, 0)            # pull CLOCK pin down, to send a rising edge
                IO.output(data_pin, 0)            # keep the DATA bit low to keep the countdown
                IO.output(latch_pin, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
                time.sleep(0.1)
                IO.output(latch_pin, 0)

while True:
        askForAction()

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
