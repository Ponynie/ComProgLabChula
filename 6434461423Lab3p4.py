ID = input("Enter student ID : ")
check = [21,22,23,24,25,26,27,28]
if len(ID) == 10 :
    ID = int(ID)
    con2 = 50 <= ID//10**8 <= 64
    con3 = (ID//10**7)%10 == 3 or (ID//10**7)%10 == 4 or (ID//10**7)%10 == 7
    con4 = ID%100 in check
    if con2 and con3 and con4 :
        print("Valid ID")
    else :
        print("Invalid ID")
else :
    print("Invalid ID")
