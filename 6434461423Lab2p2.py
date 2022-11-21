a , b , c = input("Enter coefficients a, b, c :").split(sep=",")
a = float(a) ;b = float(b) ;c = float(c)
print("Can use quadratic formula:",((b**2) - (4*a*c)) >= 0 and a != 0 )
