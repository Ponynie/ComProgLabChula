with open("score.txt") as file :
    dic_score = {}
    list_winner = [0,0,0]
    for line in file :
        line = line.strip()
        singer ,judge1 ,judge2 ,judge3 ,audience = line.split(" ")
        score = int(judge1) + int(judge2) + int(judge3) + int(audience)
        dic_score[singer] = score
    list_singer_sort = list(dic_score.keys())
    list_singer_sort.sort(key=dic_score.get , reverse=True)
    list_winner[0] = list_singer_sort[0]
    list_winner[1] = list_singer_sort[1]
    list_winner[2] = list_singer_sort[2]
    print("The winner are :")
    for i in range(len(list_winner)):
        print(f"{i+1} : {list_winner[i]} {dic_score[list_winner[i]]}")
