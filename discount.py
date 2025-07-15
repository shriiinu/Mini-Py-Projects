try:
    age=int(input("Enter age: "))
    

    if age <18 or age > 60:
        print("You are eligible for Discount")
        if age <18:
            Q=input("do you have a student ID? (yes/no): ")
            if Q=="yes":
                print("You can get Student Discount")
                st_id=input("Enter student ID: ")
            else:
                print("You can't get discount if don't have Student ID")
        elif age>60:
            Q= Q=input("do you have a ID? (yes/no): ")
            if Q=="yes":
                print("You can get senior citizen Discount")
            else:
                print("You can't get discount if don't have ID")
    
    
        
    else:
        print("You are not eligible for Discount")
except Exception as e:
    print("error ",e)

