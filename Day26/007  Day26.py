names = ["Alex","Healey","Sara","John","David","Queen","Beth"]
import  random

student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

passed_students={student:score  for (student,score) in student_scores.items() if score >=60}
print(f"The passed students are: {passed_students}")
