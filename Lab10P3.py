with open("C:\\Users\\CharmQuark\\Desktop\\ETC\\Python Program\\studentScore.txt") as file :
    score_dict = {}
    for line in file :
        temp_list = line.strip().split(" ")
        score_dict[temp_list[0]] = int(temp_list[1])
    score_dict = sorted(score_dict , key=score_dict.get,reverse=True)
    for i in range(len(score_dict)) :
        print(score_dict[i])