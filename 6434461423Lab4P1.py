import math
shape = input("Choose circle, square or rectangle : ")
if shape == "circle" :
    length  = float(input("Length of the radius of the circle : "))
    Area = math.pi * math.pow(length , 2)
    print("Area is",Area)
elif shape == "square" :
    length = float(input("Length of the side of the square : "))
    Area = math.pow(length , 2)
    print("Area is",Area)
elif shape == "rectangle" :
    length_1 , length_2 = input("Length of two sides of the rectangle : ").split(sep=",")
    length_1 = float(length_1)
    length_2 = float(length_2)
    Area = length_1 * length_2
    print("Area is",Area)
else :
    print("Invalid choice.")
