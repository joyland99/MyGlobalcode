def list():    
    list = []
    a=int(input("min"))
    b=int(input("max"))
    list.append(a)
    list.append(b)

    if(a % 2 == 0):
        while (a<b):
           
            a=a+2
            print (a)
    elif (a % 2 == 1):
        a+=1
        while (a<b):
            a=a+2
            print (a)
            
        
        

list()