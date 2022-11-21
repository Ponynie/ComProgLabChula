num_student = int(input("Number of students : "))
total_n = 0
total_p = 0 
total_f = 0
high_score = 0
p_count = 0
f_count = 0
for i in range(1 , num_student + 1) :
    score = float(input("Student "+str(i)))
    total_n += score
    if score >= 5 :
        total_p += score
        p_count += 1
    elif score < 5 :
        total_f += score
        f_count += 1
    if score > high_score :
        high_score = score
Avg_n = total_n / num_student
if p_count == 0 :
    Avg_p = 0
else :
    Avg_p = total_p / p_count
if f_count == 0 :
    Avg_f = 0
else :
    Avg_f = total_f / f_count
print("Average score :",Avg_n)
print("Average pasasing score :",Avg_p)
print("Average failing score :", Avg_f)
print("Highest score :",high_score)


