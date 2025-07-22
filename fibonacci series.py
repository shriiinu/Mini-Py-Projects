num=int(input("Enter a number: "))
a=0
b=1
for i in range(1,num+1):
    print(a)
    c=a+b              #a,b,c
    a=b                #0,1,1,2,3,5
    b=c
   