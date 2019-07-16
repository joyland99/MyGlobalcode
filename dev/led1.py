import pyowm
from gpiozero import LED
from time import sleep
def Weather_Forecast():
    city = input("Enter Name of City with space :- ")
    country = input("Enter Name of Country :- ")
​
    led = LED(17)#yellow
    led1 = LED(18)#red
    led2 = LED(27)#green
    
   
            
​
    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place('city, country')
    w = observation.get_weather()
​
​
​
    winds = w.get_wind()
    humidities = w.get_humidity()
    tempreture = w.get_temperature()
    presh = w.get_pressure()
    clud = w.get_clouds()
    ran = w.get_rain()
    snoww = w.get_snow()
​
    print(" The weather information ")
    if winds['speed'] < 15:
        print( led2.on(),
               sleep(5),
               led2.off(),
               sleep(1))
        
    elif winds['speed'] > 15 and winds['speed'] < 21:
        print( led.on(),
               sleep(5),
               led.off(),
               sleep(1))
        
    else:
        print(led1.on()(),
              sleep(5),
              led1.off(),
              sleep(1))
    
    print("The wind result is :- ", winds['speed'])
   ​
​
​
​
​
​
Weather_Forecast()



