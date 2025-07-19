try:    
    maths=int(input("Enter your maths marks: "))
    physics=int(input("Enter your physics marks: "))
    chemistry=int(input("Enter your chemistry marks: "))
    co_name=input("Enter your preferred course name: ")
    prf_co=int(input("Enter your preferred course marks: "))

    avg=(maths+physics+chemistry+prf_co)/4

    if maths >=60 and physics >=60 and chemistry >=60 and prf_co >=60:
        if avg >= 85 and co_name == "engineering":
            print("you are eligible for full scholarship Engineering Admission")
        elif avg >= 85 and co_name == "science":
            print("eligible for Science Honors")
        else:
            print("you are eligible for general admission")
    elif avg > 70 and avg<80:
            print("you are eligible for general admission")
            if maths >=80:
                print("Eligible for Engineering without Scholarship")
            else:
                 print("eligible for science or general degree")
    elif maths <65 and physics <65 and chemistry <65 and prf_co <65:
            print("apply for foundation program")
    elif maths >50 and physics >50 and chemistry >50 and prf_co >50:
            print("consider community college option")
    else:
        if maths <50 and physics <50 and chemistry <50 and prf_co <50:
            print("Not eligible for addmission")
        else:
                print("consider reappearing for exams")
except Exception as e:
    print("error ",e)
            
            
