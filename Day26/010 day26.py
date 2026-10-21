import pandas
students_dict={
    "Students": ["Sara","Sana","Lily"],
    "Score":[56,76,98]
}

# for (key,value) in students_dict.items():
#     print(key)
#     print(value)

student_data=pandas.DataFrame(students_dict)
print(student_data)

# for (key,value) in student_data.items():
#     print(value) Not useful it iterates each of the Column rather the row

#Loop Through rows of a data frame
for (index,row) in student_data.iterrows():
    if row.Students == "Sara":
        print(row.Score)
