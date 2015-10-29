# 04_movement.py
# Uses the ultrasonic rangefinder to detect movement

from rrb3 import *
import time

threshold = 10

rr = RRB3()
reference = rr.get_distance()
rr.set_led1(0)
rr.set_led2(0)

print("alarm activated")
print("Press CTRL-c to quit the program")

while True:
    time.sleep(0.3)
    reading = rr.get_distance()
    difference = abs(reading - reference)   
    if difference > threshold:
        print("Movement detected")
        for a in range(5):        
            rr.set_led1(1)
            rr.set_led2(1)
            time.sleep(0.3)
            
            rr.set_led1(0)
            rr.set_led2(0)           
            time.sleep(0.3)
    reference = reading
