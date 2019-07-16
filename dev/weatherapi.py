import pyowm

a=input("enter city followed by a comma and the country")

apiKey='bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place(a)
w = observation.get_weather()

w.get_wind()
w.get_humidity()
w.get_temperature()

print(a)
print("wind: ",w.get_wind())
print("HUMIDITY: ",w.get_humidity())
print("temp:",w.get_temperature())
print("")



b=input("enter city followed by a comma and the country")

apiKey='bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place(b)
d = observation.get_weather()

d.get_wind()
d.get_humidity()
d.get_temperature()


print(b)
print("wind: ",d.get_wind())
print("HUMIDITY: ",d.get_humidity())
print("temp:",d.get_temperature(['temp']))
print("")






c=input("enter city followed by a comma and the country")

apiKey='bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place(c)
k = observation.get_weather()

k.get_wind()
k.get_humidity()
k.get_temperature()


print(c)
print("wind: ",k.get_wind())
print("HUMIDITY: ",k.get_humidity())
print("temp:",k.get_temperature(['temp']))



while True:
    if (w.get_temperature(['temp_max']) > d.get_temperature(['temp_max']) and w.get_temperature(['temp_max']) > m.temperature(['temp_max'])):
        print(a +" has the highest temp")
    elif (d.get_temperature(['temp']) > w.get_temperature(['temp_max']) and d.get_temperature(['temp_max']) > m.temperature(['temp_max'])):
        print(b +" has the highest temp")
    elif (m.get_temperature(['temp_max']) > w.get_temperature(['temp_max']) and m.get_temperature(['temp_max']) > d.temperature(['temp_max'])):
        print(c +" has the highest temp")