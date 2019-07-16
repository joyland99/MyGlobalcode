#Libraries
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=4
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
led = LED(17)#yellow
led1 = LED(27)#red
led2 = LED(22)#green
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    led.on()
    sleep(2)
    GPIO.output(buzzer,GPIO.LOW)
    led.off()
    sleep(2)
     
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
  
    
    led1.on()
    sleep(2)
    led1.off()
    sleep(2)
    
    led2.on()
    sleep(5)
    led2.off()
    sleep(3)
  
    
    
    
    