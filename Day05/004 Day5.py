student_scores =input("Input a list of student \n\n").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(f"The Student score is {student_scores} ")

#78 65 89 86 55 91 89
highest_score =0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The Highest Score in the class is: {highest_score}")








