for i in range(1,6):
  x=input("Enter Your Password: ")
  if x=="skip":
    continue
  if x=="OpenAI123":
    print("Access Granted")
    break
    
  if i==5:
    print("Access Denied")

    