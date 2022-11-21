Weight = float(input("kg."))
Height = float(input("m."))
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