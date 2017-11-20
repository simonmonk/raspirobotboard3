# Attach: SR-04 Range finder, switch on SW1, and of course motors.

# The switch SW2 stops and starts the robot

from rrb3 import *
import time, random

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

# if you dont have a switch, change the value below to True
running = False

def turn_randomly():
    turn_time = random.randint(1, 3)
    if random.randint(1, 2) == 1:
        rr.left(turn_time, 0.5) # turn at half speed
    else:
        rr.right(turn_time, 0.5)
    rr.stop()

try:
    while True:
        distance = rr.get_distance()
        print(distance)
        if distance < 50 and running:
            turn_randomly()
        if running:
            rr.forward(0)
        if rr.sw2_closed():
            running = not running
        if not running:
            rr.stop()
        time.sleep(0.2)
finally:
    print("Exiting")
    rr.cleanup()
    
