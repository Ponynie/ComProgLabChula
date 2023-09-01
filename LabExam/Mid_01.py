Choice = input("Name or Age or Weigh")
if Choice == "Name" :
    x = str(input("Name Here : "))
elif Choice == "Age" :
    x = int(input("Age Here"))
elif Choice == "Weigh" :
    x = float(input("Weigh Here"))
if Choice == "Name" :
    l = len(x)
    print(f"Your name lenght is {l} letter")
if Choice == "Age" :
    if x > 18 :
        print("Your are adult !!")
    else :
        print("Your are a kid")
if Choice == "Weigh" :
    if x > 80 :
        print("น้ำหนักเกิน")
    else :
        print("น้ำหนักพอดี")
