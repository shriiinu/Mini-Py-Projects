try:
    age=int(input("Enter your age: "))
    eye_test=input("Have You Passed the Eye Test? (yes/no): ")
    if age >= 18 and eye_test == "yes":
        print("Eligible for driver's license")
    else:
        print("Need to pass eye-test")

    if age < 18: print("Not eligible for driver's license")
except Exception as e:
    print("error ",e)

