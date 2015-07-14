#Python 2

import rrb3 as rrb
import time
#import ex_8x8_pixels

rr = rrb.RRB3(6, 3)

def confirm(question):
    answer = raw_input(question)

def test_leds():
    rr.set_led1(0)
    rr.set_led2(0)
    confirm("Are LED1 and LED2 both OFF?")
    
    rr.set_led1(1)
    rr.set_led2(0)
    confirm("Is LED1 ON and LED2 OFF?")
    
    rr.set_led1(1)
    rr.set_led2(1)
    confirm("Are LED1 and LED2 both ON?")
    
    rr.set_led1(0)
    rr.set_led2(0)
    confirm("Are LED1 and LED2 both OFF?")
    

def test_oc():
    rr.set_oc1(0)
    rr.set_oc2(0)
    confirm("OC1 and OC2 OFF?")
    
    rr.set_oc1(1)
    rr.set_oc2(0)
    confirm("OC1 ON?")

    rr.set_oc1(0)
    rr.set_oc2(1)
    confirm("OC2 ON?")
    
    rr.set_oc1(0)
    rr.set_oc2(0)
    confirm("OC1 and OC2 OFF?")
    
def test_switches():
    print("Remove header jumpers from [SW1] and [SW2]")
    while rr.sw1_closed() or rr.sw2_closed():
        pass
    print("PASS: [SW1] and [SW2] open")
    
    print("Fit header jumpers over [SW1] only")
    while not rr.sw1_closed() or rr.sw2_closed():
        pass
    print("PASS: [SW1] closed")
    
    print("Fit header jumpers over [SW2] only")
    while rr.sw1_closed() or not rr.sw2_closed():
        pass
    print("PASS: [SW2] closed")


def test_motors():
    rr.set_motors(0, 0, 0, 0)
    confirm("Are Both motors stopped?")
    
    rr.set_motors(1, 0, 1, 0)
    confirm("Are Both motors going forwards?")

    rr.set_motors(0.5, 0, 0.5, 0)
    confirm("Are both motors going forwards at half speed?")
    
    rr.set_motors(1, 1, 1, 1)
    confirm("Are both motors going backwards?")
    
    rr.set_motors(0, 0, 0, 0)
    confirm("Are the motors off now?")

def test_ranger():
    print("Make sure there is nothing infront of the rangefinder for 30cm")
    print("Approximate distance should be displayed.")
    print("Put your hand less than 10cm from rangefinder to finish test.")
    d = rr.get_distance()
    while d > 10:
        print(d)
        time.sleep(1)
        d = rr.get_distance()
    print("PASS")

def testI2C():
    confirm("Watch the LED Matrix. Press Return when ready.")
    ex_8x8_pixels.display_pattern()
    confirm("Did the display draw a line at a time?")

test_leds()
test_oc()
test_switches()
test_motors()
test_ranger()
#testI2C()