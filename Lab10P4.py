price = {
    "Cappuccino":{"S": 60 , "L": 70},
    "Espresso":{"S": 45 , "L": 50},
    "Latte":{"S": 65 , "L": 75}
}
Drink , Size , Number = input("Enter drink, size and number : ").split(" ")
Number = int(Number)
if Drink in price.keys() :
    if Size in price[Drink].keys() :
        total = price[Drink][Size] * Number
        print(f"Total : {total}")
    else:
        print("Incorrect size.")
else:
    print("Drink not avaliable.")