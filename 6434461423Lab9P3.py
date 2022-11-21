n = int(input("Enter a number between [0,9]: "))
result = [ i for i in range(2,100) if str(n) in str(i)]
print(result)