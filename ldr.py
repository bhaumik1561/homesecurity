from gpiozero import LightSensor,LED
from time import sleep
led=LED(23)                                             
ldr= LightSensor(4)
while True:
    sleep(0.1)
    if ldr.value < 0.5:
        led.on()
        
    else:
        led.off()