import random

def Start():   
    Username = "MrLeeman"
    password = "MrLeeman569"

    UN = input("Enter Username: ")
    PW = input("Enter password: ")

    if UN != Username or PW != password:
        print("Wrong credentails")
        Start()
    elif UN == Username and PW == password:
        Action = input("What do you want to do - Report, Enter, Logout or Search: ")
        if Action == "Enter":
            F = open("Students.txt", "a")
            ID = (random.randint(100000,999999))
            SN = input("Enter SurName: ")
            FN = input("Enter ForName: ")
            DOB = input("Enter D.O.B: ")
            ADRS = input("Enter Address: ")
            PN = input("Enter PhoneNumber: ")
            GENDER = input("Enter Gender: ")
            TUTOR = input("Enter Tutor: ")
            F.write(str(ID))
            F.write("-")
            F.write(SN)
            F.write("-")
            F.write(FN)
            F.write("-")
            F.write(DOB)
            F.write("-")
            F.write(ADRS)
            F.write("-")
            F.write(PN)
            F.write("-")
            F.write(GENDER)
            F.write("-")
            F.write(TUTOR)
            F.write("\n")
            F.close()
            
            
        elif Action == "Report":
            lines = 1
            F = open("Students.txt", "r")
            students = F.readlines()
            for i in students:
                print(lines,"-", i)
                lines = lines + 1
            Report = int(input("What line do you want a report of:"))
            if Report > 0 and Report <= int(lines):
                print(students[Report-1])
                F.close()
            else:
                print("Invalid line")
                
        elif Action == "Logout":
            print("Logging out")
            Start()

        elif Action == "Search":
            Number = input("Enter Id number of student:")
            F = open("Students.txt", "r")
            lines = F.readlines()
            for i in lines:
                if Number in i:
                    print(i)

            F.close()
            
            

Start()
    
    
