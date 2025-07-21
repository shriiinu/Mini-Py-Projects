for i in range(1,1000):
    y=i
    x=y
    sqre=y**2
    digit=0
    while x>0:
        digit+=1
        x=x//10
    if y==sqre%(10**digit):
        print(y)
        
    
    