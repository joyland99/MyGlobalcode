def is_even():
    numbers = [1,56,234,87,4,76,24,69,90,135]  
    even = lambda x:x % 2==0
    l=list(map(even,numbers))
    print(l)
    
    
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

    positive= lambda x:x > 0
    l=list(filter(positive,numbers))
    print(l)
        
    numbers1 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
    even= lambda x:x%2==0
    print([list(filter(even,numbers1))])

    for x in range (1,51):
        print(x)
        
        
    odd= lambda x:x%2==1
    print(list(filter(odd,range(1,51))))



      



is_even()