Weight , Weight_Unit = input("Weight").split()
Height , Height_Unit = input("Height").split()
Weight = float(Weight)
Height = float(Height)
if Weight_Unit == "lbs" : 
    Weight = Weight / 2.205
else :
    exit
if Height_Unit == "ft" :
    Height = Height / 3.2808399
elif Height_Unit == "cm":
    Height = Height / 100
bmi = Weight / Height**2
if bmi < 18.5 :
    print("ผอม")
elif 18.5 <= bmi < 23 :
    print("รูปร่างปกติ")
elif 23 <= bmi < 25 :
    print("รูปร่างอ้วน")
elif 25 <= bmi < 30 :
    print("อ้วนระดับ 1")
elif bmi >= 30 :
    print("อ้วนระดับ 2")