Current_Tem = float(input("Day 1 : "))
Pre_Tem = Current_Tem
for i in range(2 , 8) :
    Current_Tem = float(input("Day"+" "+str(i)+" : "))
    if Current_Tem < Pre_Tem :
        print("Temperature dropped on day",i)
    Pre_Tem = Current_Tem