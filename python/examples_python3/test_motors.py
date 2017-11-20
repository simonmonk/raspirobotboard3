from rrb3 import *
from random import randint

rr = RRB3(8, 6)

i = 0

while True:
    speedl = randint(0, 100) / 100.0
    speedr = randint(0, 100) / 100.0
    dl = randint(0, 1)
    dr = randint(0, 1)
    rr.set_motors(speedl, dl, speedr, dr)
    time.sleep(3)
    i += 1
    print(i)
