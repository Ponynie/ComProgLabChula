side1 , side2 , side3 = input("Length of 3 sides: ").split(sep=",")
side1 = float(side1)
side2 = float(side2)
side3 = float(side3)
con1 = side1 + side2 > side3
con2 = side2 + side3 > side1
con3 = side1 + side3 > side2
print("Triangle:", con1 and con2 and con3)