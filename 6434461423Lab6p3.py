import math
num = int(input("Enter an integer : "))
if num == 1 :
    prime = 0
else :
    prime = 1
for i in range(2 ,math.ceil(math.sqrt(num)) + 1) :
    if num % i == 0 and num != 2 :
        prime = 0
        break
if prime == 0 :
    print(num,"is not a prime number.")
elif prime == 1 :
    print(num,"is a prime number")


