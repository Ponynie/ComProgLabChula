with open("vectors.txt") as f :
    v1_string = f.readline().strip().split(" ")
    v2_string = f.readline().strip().split(" ")
    v1 = [float(i) for i in v1_string]
    v2 = [float(i) for i in v2_string]
    if len(v1) == len(v2) :
        Summation = []
        for i in range(len(v1)) :
            x = v1[i] * v2[i]
            Summation.append(x)
        dotproduct = sum(Summation)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v1*v2 = {dotproduct}")
    else :
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print("Incompatible size")


