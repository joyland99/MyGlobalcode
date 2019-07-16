from gpiozero import LED,Button
from signal import pause
import time
led=LED(18)
led=LED(27)
button=Button(2)


button.when_pressed=led.on
button.when_released=led.off

pause()

    