my_name = "Phichaphop"
user_name = input("Enter username : ") 
while True :
    if user_name != my_name :
        user_name = input("Incorrect. Enter again : ")
    else : 
        break
print("Hello,",user_name)

