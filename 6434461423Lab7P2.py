xi , yi = input("Inittial position : ").split(sep=",")
xi = int(xi) ; yi = int(yi)
check = "Valid"
f = open("move.txt")
for line in f :
    line = line.strip()
    if line == "L" :
        if xi - 1 == -10 or xi - 1 == 10 :
            continue
        else :
            xi = xi - 1
    elif line == "R" :
        if xi + 1 == -10 or xi + 1 == 10 :
            continue
        else :
            xi = xi + 1
    elif line == "U" :
        if yi + 1 == -10 or yi + 1 == 10 :
            continue
        else :
            yi = yi + 1
    elif line == "D" :
        if yi - 1 == -10 or yi - 1 == 10 :
            continue
        else :
            yi = yi - 1
    else :
        check = "Invalid"
f.close
if check == "Valid" :
    print(f"Robot stops at {xi},{yi}")
else :
    print("Invalid command")

