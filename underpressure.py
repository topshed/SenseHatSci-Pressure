import logging
from sense_hat import SenseHat
from time import sleep
logging.basicConfig(filename='testlog.log', level=logging.DEBUG,
    format='%(asctime)s %(message)s')
sh = SenseHat()
p_old = 0
b = [0,0,0]
c = [255,0,0]
d=  [0,255,0]
arrow = []
up_arrow = [
    b,b,b,c,c,b,b,b,
    b,b,c,c,c,c,b,b,
    b,c,c,c,c,c,c,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b,
    b,b,c,c,c,c,b,b]
down_arrow = [
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    b,d,d,d,d,d,d,b,
    b,b,d,d,d,d,b,b,
    b,b,b,d,d,b,b,b]

while True:
   show_arrow = False
   p = sh.get_pressure()
   logging.info(str(p))
   if p > p_old:
       col = [255,0,0]
       if (p - p_old) >= 1:
           show_arrow = True
           arrow = up_arrow
   else:
       col = [0,255,0]
       if (p_old - p) >= 1:
           show_arrow = True
           arrow = down_arrow
   sh.show_message(str(round(p,2)),text_colour=col)
   if show_arrow:
   	sh.set_pixels(arrow)
   sleep(0.5)
   p_old = p
