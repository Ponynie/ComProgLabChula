#6434461423 Phichaphop Raqsaboon 1
with open("transcript.txt") as file :
    sum_grade = 0
    grade_freq = 0
    for line in file :
        line_list = line.strip().split(" ")
        sum_grade = sum_grade + (float(line_list[1])*float(line_list[2]))
        grade_freq = grade_freq + int(line_list[1])
    Gpax = sum_grade / grade_freq
    print(f"GPAX: {Gpax}")
