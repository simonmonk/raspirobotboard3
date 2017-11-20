# Attach: SR-04 Range finder

from rrb3 import *
import time, random

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

try:
    while True:
        distance = rr.get_distance()
        print(distance)
        time.sleep(0.2)
finally:
    print("Exiting")
    rr.cleanup()
    
