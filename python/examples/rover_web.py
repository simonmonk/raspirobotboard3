from bottle import route, run, template, request
import rrb3 as rrb
import time

# Change these for your setup.
IP_ADDRESS = '192.168.1.13' # of your Pi
BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

# Configure the RRB
rr = rrb.RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

# Handler for the home page
@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        rr.forward()
    elif cmd == 'l':
        rr.left(0, 0.5) # turn at half speed
    elif cmd == 's':
        rr.stop()
    elif cmd == 'r':
        rr.right(0, 0.5)
    elif cmd == 'b':
        rr.reverse(0, 0.3) # reverse slowly
    return template('home.tpl')
        
# Start the webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:  
    rr.cleanup()
