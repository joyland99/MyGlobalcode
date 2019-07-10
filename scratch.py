import math
pi = math.pi
degree= float(input("degree: "))
radian = degree*(pi/180)
print("Radian")
print(radian)

r = int(input("radius: "))
suf_area=4*pi*(r*r)
volume=4/3*pi*math.pow(r,3)
print("surface area: ")
print(suf_area)
print ("")
print("volume: ")
print(volume)


