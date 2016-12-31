# Use the arrow keys to direct the robot
# Many thanks to Matt Linton, Caroline Lucas and Dave Linton for contributing this code.
# This multi-threaded robot example allows you to move the rover using keyboard keys (over SSH).
# It also detects obstacles using the rangfinder and automatically back-up.


from multiprocessing import Process

from rrb3 import *
import sys
import tty
import termios

rr = RRB3(9.0, 6.0) # battery, motor
motor_speed = 0.4
half_speed = motor_speed/2
ahead = True

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

print("Use the arrow keys to move the robot")
print("Press CTRL-c TWICE to quit the program")

# These two functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# This will continuously measure distance to obstruction and react when nearer than 20cm
def loop_a():
    while 1:    
        distance = rr.get_distance()
        if distance < 20:
            print (distance)
            rr.reverse(2, motor_speed)
            print 'sensor'

Process(target=loop_a).start()

# This will control the movement of the robot and display on your screen
try: 
    while True:
        keyp = readkey()
        if keyp == UP:
            rr.forward(0, motor_speed) # if you don't specify duration it keeps going indefinitely
            ahead = True
            print 'forward'
        elif keyp == DOWN:
            rr.reverse(0, motor_speed)
            ahead = False
            print 'reverse'
        elif keyp == RIGHT:
            if ahead == True:
                rr.right(0.2, half_speed)
                rr.forward(0, half_speed)
            if ahead == False:
                rr.right(0.2, half_speed)
                rr.reverse(0, half_speed)
            print 'clockwise'
        elif keyp == LEFT:
            if ahead == True:
                rr.left(0.2, half_speed)
                rr.forward(0, half_speed)
            if ahead == False:
                rr.left(0.2, half_speed)
                rr.reverse(0, half_speed)
            print 'anti clockwise'
        elif keyp == ' ':
            rr.stop()
            print 'end stop'
        elif ord(keyp) == 3: # Press CTRL-c TWICE to quit the program
            print 'break'
            break

except KeyboardInterrupt:
    GPIO.cleanup()
