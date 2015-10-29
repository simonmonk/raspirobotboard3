# 09_robot_sequence.py
# Moves the robot to attempt a regular polygon shape

from rrb3 import *

rr = RRB3(9.0, 6.0)

motor_speed = 1.0
sides = 3
turn = 1.5

print("Press CTRL-c to quit the program")

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

