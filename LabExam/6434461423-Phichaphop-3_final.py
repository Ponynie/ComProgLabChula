#6434461423 Phichaphop Raqsaboon 3
covid_patients = {
    "UdonThani": 17657,
    "SakonNakhon": 7692,
    "NakhonPhanom": 4974,
    "Loei": 3614,
    "NongKhai": 3901,
    "NongBuaLumphu": 4204,
    "BuengKan": 2014,
}
print("Enter patients in each of 7 provinces: ")
for i in range(0,7) :
    name , case = input().split(" ")
    if name in covid_patients.keys() :
        covid_patients[name] = covid_patients[name] + int(case)
print("Report: ")
for i in covid_patients.keys() :
    print(f"{i} {covid_patients[i]}")