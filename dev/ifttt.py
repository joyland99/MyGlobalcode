import requests

url1="https://maker.ifttt.com/trigger/messanger/with/key/2Kud4E0CUmxZX3JAbrzbl"
name="joyland"
message="Hello there,like your laptop,its cool "
r = requests.get(url1,{"value1":name,"value2":message})
c= r.status_code
print(c)