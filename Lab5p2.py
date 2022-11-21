my_name = "Phichaphop"
user_name = input("Enter username : ")
count = 1 
while user_name != my_name and count <= 2 :
    user_name = input("Incorrect. Enter again : ")
    count += 1
if user_name != my_name :
    print("Not allowed. Incorrect name.")
else :
    print("Hello,",user_name)

