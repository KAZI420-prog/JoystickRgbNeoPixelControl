import machine
from machine import Pin
import time
import math
import neopixel
hPin=27
vPin=26
hJoy= machine.ADC(hPin)
vJoy= machine.ADC(vPin)
pixPin=0
pixSize=8 #adjust pixel string size here
pix=neopixel.NeoPixel(Pin(pixPin),pixSize)

def getRGB(deg):
    m=1/60
    if deg>=0 and deg<60:
        R=1
        G=0
        B=m*deg
    if deg>=60 and deg<120:
        R=1-m*(deg-60)
        G=0
        B=1
    if deg>=120 and deg<180:
        R=0
        G=m*(deg-120)
        B=1
    if deg>=180 and deg<240:
        R=0
        G=1
        B=1-m*(deg-180)
    if deg>=240 and deg<300:
        R=m*(deg-240)
        G=1
        B=0
    if deg>=300 and deg<360:
        R=1
        G=1-m*(deg-300)
        B=0
    myColor=(int(R*40),int(G*40),int(B*40))#adjust brightness here
    return myColor
while True:
    hVal=hJoy.read_u16()
    vVal=vJoy.read_u16()
    
    hCal=int(-.00306*hVal+100.766)
    vCal=int(.00306*vVal-100.766)
    
    deg=math.atan2(vCal,hCal)*360/2/math.pi
    if hCal==0:
        hCal=1
    if deg<0:
        deg=deg+360
    
    mag=math.sqrt(hCal**2+vCal**2)
    if mag<=4:
        hCal=0
        vCal=0
        deg=0
    
    color=getRGB(int(deg))
    pix.fill(color)
    pix.write()
    time.sleep(.1)
    print(deg)
    time.sleep_ms(200)