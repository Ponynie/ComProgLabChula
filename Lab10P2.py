with open("C:\\Users\\CharmQuark\\Downloads\\Lab10_2_conversation.txt") as text :
    freq = {}
    for line in text :
        if line.isspace() :
            continue
        else :
            line_list = line.strip().split(" ")
            line_list = [ i.strip(":?,.").casefold() for i in line_list]
            for i in line_list :
                freq[i] = freq.get(i , 0) + 1
    freq__list_tuple = list(freq.items())
    for i in range(len(freq__list_tuple)) :
        print(freq__list_tuple[i][0],freq__list_tuple[i][1])