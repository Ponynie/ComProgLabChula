import random 
Correct_num = random.randint(1 , 9)
guess = int(input("Your guess : "))
while guess != Correct_num :
    guess = int(input("Your guess : "))
print("Correct.")