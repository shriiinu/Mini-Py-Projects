x=int(input("Enter a number: "))
z=x
y=0
while x>0:
    y=y*10+x%10
    x=x//10
print(z)
if z==y:
   print("Palindrome")
else:
   print("Not a Palindrome")
