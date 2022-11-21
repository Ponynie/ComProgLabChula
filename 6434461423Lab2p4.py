a , b , c = input("Length of 3 sides: ").split(sep=",")
a = float(a)
b = float(b)
c = float(c)
con1 = a**2 + b**2 == c**2
con2 = b**2 + c**2 == a**2
con3 = a**2 + c**2 == b**2
print("Right triangle:", con1 or con2 or con3)