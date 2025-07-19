age = int(input("Enter your age: "))
citizen = input("Are you a citizen of India? (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible to vote (Not a citizen)")
elif 16 <= age < 18:
    print("Can pre-register to vote")
else:
    print("Too young to vote")
