Subject = {
    "2301117":("Calculus I", 4),
    "2301118":("Calculas II", 4),
    "2301286":("Probability and Statistics", 3 ),
    "2301399":("project Proposal", 1),
    "2301499":("Senior Project", 2),
    "2302113":("Gnerral Chemistry Lab I", 1),
    "2302161":("General Chemistry", 3)
    }
Id = input("Course ID: ")
while Id != "0" :
    if Id in Subject.keys() :
        x = Subject.get(Id)
        print(x[0],x[1])
    else :
        print("Unknown")
    Id = input("Course ID: ")