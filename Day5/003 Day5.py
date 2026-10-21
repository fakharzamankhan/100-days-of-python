
#156 178 165 171 187
# print(sum(students_heights))
#easy way
# total_height=sum(students_heights)
# number_of_students=len(students_heights)
# average_height= total_height/number_of_students
# print(f"The Average height of the students is {average_height} " )

students_heights=input("Enter a list of student heights:\n ").split()
for n in range(len(students_heights)):
    students_heights[n]=int(students_heights[n])
print(students_heights)

total_height=0
for height in students_heights:
    total_height+=height
print(f"The Total height of all the student is {total_height} ")

number_of_students=0
for student in students_heights:
    number_of_students+=1
print(f"The Number of students are {number_of_students}")

average_height=round(total_height/number_of_students)
print(f"The Average height of all the student is {average_height} ")





