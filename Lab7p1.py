xi , yi = input("Inittial position : ").split(sep=",")
xi = int(xi) ; yi = int(yi)
check = "Valid"
f = open("move.txt")
for line in f :
    line = line.strip()
    if line == "L" :
        xi = xi - 1
    elif line == "R" :
        xi = xi + 1
    elif line == "U" :
        yi = yi + 1
    elif line == "D" :
        yi = yi - 1
    else :
        check = "Invalid"
f.close
if check == "Valid" :
    print(f"Robot stops at {xi},{yi}")
else :
    print("Invalid command")

