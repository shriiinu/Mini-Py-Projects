prime=[]
for i in range(50,101):
  
  for j in range(2,i):
    if i%j==0:
      break
  else:
    prime.append(i)

# print(prime)

print(prime)
    


# x=int(input("Enter a number: "))
# for i in range(2,x):
#   if x%i==0:
#     print(x,"is not a prime number")
#     break
# else:
#   print(x,"is a prime number")