# 04_distance.py
# Uses the ultrasonic rangefinder to measure distance

from rrb3 import *
import time

rr = RRB3()

print("Press CTRL-c to quit the program")

while True:
    dist = rr.get_distance()
    print(dist)
    time.sleep(0.5)
