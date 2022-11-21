from math import factorial 
def f(x) :
    ans = 1 / factorial(x)
    return ans
def summation(a,b) :
    ans = 0
    for i in range(a,b+1) :
        ans = ans + f(i)
    return ans
m = int(input("Enter m: "))
n = int(input("Enter n: "))
if m > n :
    print(summation(n,m))
elif m < n :
    print(summation(m,n))
else :
    print("Invalid")
