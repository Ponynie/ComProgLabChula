Total = 50000
withdraw = 0 
Balance = Total - withdraw
while Balance != 0 :
    withdraw = int(input("Withdraw : "))
    Balance = Total - withdraw
    if Balance < 0 :
        print("Insufficient  fund.")
        Balance = Balance + withdraw
    elif Balance == 0 :
        print("Balance is 0.")
    else :
        Total = Balance