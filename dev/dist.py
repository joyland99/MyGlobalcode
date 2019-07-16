def cl_dis():
    from geopy.geocoders import Nominatim
    a=input("location 1:")
    #b=input("location 2:")
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode("175 5th Avenue NYC")
   # loc1 = geolocator.geocode(b)
    loc2 = geolocator.geocode(a)
    print(location.address)
    #print((loc1.latitude, loc1.longitude))
    print((loc2.latitude, loc2.longitude))
    #print(loc1.raw)
    #print(loc2.raw)

    #from geopy.distance import geodesic
    #print(geodesic(a,b).miles)


cl_dis()
