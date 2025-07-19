# operation with exxception handling
# This program performs basic arithmetic operations on two numbers
try:
  a=int(input("Enter 1st number : "))
  b=int(input("Enter 2nd number : "))
  print("Available Operations are : +, -, *, /, ^ input any one of them")
  op=(input("which Operation Want To Perform : "))

# print(a ,op, b  is)")

  if op=='+':
      print("Addition of two numbers is : ",a+b)
  elif op=='-':
      print("Subtraction of two numbers is : ",a-b)
  elif op=='*':
      print("Multiplication of two numbers is : ",a*b)
  elif op=='/':
      if b==0:
          print("Division by zero is not allowed")
      else:
          print("Division of two numbers is : ",a/b)
  elif op=='^':
      print("Exponentiation of two numbers is : ",a**b)
    

  else:
      print("Invalid Operation, ")
except Exception as e:
    print("error ",e)