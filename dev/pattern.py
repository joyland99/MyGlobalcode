#displaying a '*' pattern
    
def function1():
    a=4
    for i in range(0,a):
            print("****")
    
    
    
def function2():
    a=4
    x="*"
    print(x)
    while len(x)<4:
        x+="*"
        print(x)
    for i in range(a,0,-1):
        for j in range (0,i-1):
            print("*",end="")
        print("")
    
function1()
print('')
function2()
