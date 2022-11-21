Id = int((input("Enter student ID : ")))
con1 = Id%100
con2 = (Id//10**7)%10
con3 = Id//10**8
Group_1 = con1 in [21,23,25,28]
Group_2 = con1 in [22,24,26,27]
Bac = con2 in [3,4]
master = con2 in [7]
prefix_1 = 50 <= con3 <= 55
prefix_2 = con3 >= 56
if len(str(Id)) == 10 :
    Id = int(Id)
    check2 = 50 <= con3 <= 64
    check3 = con2 in [3,4,7]
    check4 = 21 <= con1 <= 28 
    if check2 and check3 and check4 :
        Semester = int(input("Enter semester : "))
        if Semester in [1,2,3] :
            if Group_1 == True :
                if Bac == True :
                    if Semester in [1,2] :
                        if prefix_1 == True :
                            print("Registration fee : 18,000")
                        elif prefix_2 == True :
                            print("Registration fee : 21,000")
                    elif Semester == 3 :
                        if prefix_1 == True :
                            print("Registration fee : 4,500")
                        elif prefix_2 == True :
                            print("Registration fee : 5,250")
                elif master == True :
                    if Semester in [1,2] :
                        if prefix_1 == True :
                            print("Registration fee : 26,000")
                        elif prefix_2 == True :
                            print("Registration fee : 31,000")
                    elif Semester == 3 :
                        if prefix_1 == True :
                            print("Registration fee : 7,000")
                        elif prefix_2 == True :
                            print("Registration fee : 7,750")
            elif Group_2 == True :
                if Bac == True :
                    if Semester in [1,2] :
                        if prefix_1 == True :
                            print("Registration fee : 14,500")
                        elif prefix_2 == True :
                            print("Registration fee : 17,000")
                    elif Semester == 3 :
                        if prefix_1 == True :
                            print("Registration fee : 4,500")
                        elif prefix_2 == True :
                            print("Registration fee : 5,250")
                elif master == True :
                    if Semester in [1,2] :
                        if prefix_1 == True :
                            print("Registration fee : 19,000")
                        elif prefix_2 == True :
                            print("Registration fee : 23,000")
                    elif Semester == 3 :
                        if prefix_1 == True :
                            print("Registration fee : 7,000")
                        elif prefix_2 == True :
                            print("Registration fee : 7,750")
        else :
            print("Invalid semester")
    else :
        print("Invalid ID")
else :
    print("Invalid ID")