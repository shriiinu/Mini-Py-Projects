x=input("enter year to check if it is leap year or not : ")
try:
    x=int(x)
    if x%4==0 and x%100!=0:     
      print("it is leap year")
    elif x%400==0:
      print("it is leap year")
    else:
      print("it is not leap year")
except Exception as e:
    print("error ",e)
