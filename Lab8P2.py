with open("ComProgLab/sol.txt") as file_sol, open("ComProgLab/exam.txt") as file_exam :
    sol = file_sol.readline().strip().split(" ")
    student_score = []
    sum_average_score = [i*0 for i in range(len(sol))]
    for line in file_exam :
        list_answer = line.strip().split(" ")
        score = 0
        for i in range(len(list_answer)) :
            if list_answer[i] == sol[i] :
                score = score + 1
                sum_average_score[i] = sum_average_score[i] + 1
        student_score.append(score)
    average_score = [i/8 for i in sum_average_score]
    max_score = max(average_score)
    min_score = min(average_score)
    max_index = [i+1 for i in range(len(average_score)) if max_score == average_score[i]]
    min_index = [i+1 for i in range(len(average_score)) if min_score == average_score[i]]
    print(f"Student score : {student_score}")
    for i in range(len(average_score)) :
        print(f"Question {i+1} :{average_score[i]}")
    print(*min_index,"is the hardest question.")
    print(*max_index,"is the easiest question.")