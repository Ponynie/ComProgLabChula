Id = input("Enter student ID :")
if len(Id) == 10 :
    check_1 = int(Id[0:2]) >= 48
    check_2 = 21 <= int(Id[8:10]) <= 40
    check_3 = int(Id[8:10]) in [51,53]
    if check_1 and (check_2 or check_3) :
        Semes = int(input("Enter semester :"))
        if Semes in [1,2,3] :
            if int(Id[8:10]) in [21,23,25,28,30,31,32,33,35,36,37,38,39,53] :
                Group = "Group_1"
            elif int(Id[8:10]) in [22,24,26,27,29,34,40,51] :
                Group = "Group_2"
            if Semes in [1,2] :
                Semes = "One_Two_Semes"
            else :
                Semes = "Three_Semes"
            if int(Id[2]) == 7 :
                Degree = "Master"
            else :
                Degree = "Bachelor"
            if 48 <= int(Id[0:2]) <= 49 :
                Year = "48-49"
            elif 50 <= int(Id[0:2]) <= 55 :
                Year = "50-55"
            else :
                Year = "56up"
            Data = {
                "Group_1":{
                    "Bachelor":{
                        "One_Two_Semes":{
                            "48-49":16000 , "50-55":18000 , "56up":21000
                        },
                        "Three_Semes":{
                            "48-49":4000 , "50-55":4500 , "56up":5250
                        }
                    },
                    "Master":{
                        "One_Two_Semes":{
                            "48-49":22500 , "50-55":26000 , "56up":31000
                        },
                        "Three_Semes":{
                            "48-49":6000 , "50-55":7000 , "56up":7750
                        }
                    }
                },
                "Group_2":{
                    "Bachelor":{
                        "One_Two_Semes":{
                            "48-49":12000 , "50-55":14500 , "56up":17000
                        },
                        "Three_Semes":{
                            "48-49":4000 , "50-55":4500 , "56up":5250
                        }
                    },
                    "Master":{
                        "One_Two_Semes":{
                            "48-49":16500 , "50-55":19000 , "56up":23000
                        },
                        "Three_Semes":{
                            "48-49":6000 , "50-55":7000 , "56up":7750
                        }
                    }
                }
            }
            Fee = Data[Group][Degree][Semes][Year]
            print(F"Registration fee : {Fee}")
        else :
            print("Invalid semester")
    else :
        print("Invalid ID")
else :
    print("Invalid ID")