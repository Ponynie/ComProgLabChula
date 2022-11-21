import math
a , b , c = input("Enter coefficients a, b, c : ").split(sep=",")
a = float(a)
b = float(b)
c = float(c)
x1 = ((-b) + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = ((-b) - math.sqrt(b**2 - 4*a*c))/(2*a)
print("x =",x1,",",x2)
