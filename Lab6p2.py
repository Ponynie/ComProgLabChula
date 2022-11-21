num = int(input("Enter an integer : "))
print(num,"is divisible by:")
for i in range(1 , num + 1) :
    if num % i == 0 :
        print(i)
