x , y = input("x,y : ").split(sep=",")
x = int(x)
y = int(y)
if 0 < x < 10 and 0 < y < 20 :
    print("(",x,",",y,")","is in","C")
elif 0 < x < 40 and 0 < y < 40 :
    print("(",x,",",y,")","is in","A")
elif -40 < x < 10 and -20 < y < 20 :
    print("(",x,",",y,")","is in","B")
else :
    print("(",x,",",y,")","is in","D")


