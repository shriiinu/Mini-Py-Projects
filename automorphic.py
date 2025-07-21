y=9316
x=y
sqre=y**2
digit=0
while x>0:
    digit+=1
    x=x//10
if y==sqre%(10**digit):
    print("Automorphic")
else:
    print(" Not Automorphic")
     