def dic_sort(x) :
    a = x[0]
    return a
i = 1
Data = {}
while i <= 10 :
    Id , size , number = input("Enter product ID, size, number of items :").split(" ")
    number = int(number)
    Id = int(Id)
    Id_size = (Id , size)
    Data[Id_size] = Data.get(Id_size , 0) + number
    i = i + 1
key_sort = list(Data.keys())
key_sort.sort(key=dic_sort)
print("Stocks : ")
for i in key_sort :
    print(f"{i[0]} {i[1]} {Data[i]}")
