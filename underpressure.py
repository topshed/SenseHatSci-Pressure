import logging # makes it easy to log data to file
from sense_hat import SenseHat
from datetime import datetime
from time import sleep

# Set up the logfile name based on date/time
logfile = "pressure-"+str(datetime.now().strftime("%Y%m%d-%H%M"))+".csv"
# Logging settings and format for csv
logging.basicConfig(filename=logfile, level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d, %H:%M:%S,')

sh = SenseHat() #Initialise SenseHAT
p_old = 0 # previous reading
b = [0,0,0] # All LEDs off
c = [255,0,0] # Red
d=  [0,255,0] # Green
arrow = []
up_arrow = [ # Up arrow
    b,b,b,c,c,b,b,b,
    b,b,c,c,c,c,b,b,
    b,c,c,c,c,c,c,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b]

down_arrow = [ # Down arrow
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,d,d,d,d,d,d,b,
    b,b,d,d,d,d,b,b,
    b,b,b,d,d,b,b,b]

while True: # main loop
   show_arrow = False
   p = sh.get_pressure() # Take pressure reading
   logging.info(str(p)) # Log value to file
   if p > p_old: # If pressure has increased...
       col = [255,0,0] # Set to Red
       if (p - p_old) >= 1: # If change > 1mB
           show_arrow = True
           arrow = up_arrow
   else: # If pressure has decreased...
       col = [0,255,0] # set to green
       if (p_old - p) >= 1:
           show_arrow = True
           arrow = down_arrow
   sh.show_message(str(round(p,2)),text_colour=col)
   if show_arrow:
   	sh.set_pixels(arrow) # Draw arrow on LEDs
   	sleep(0.5)
   p_old = p # Set previous value
