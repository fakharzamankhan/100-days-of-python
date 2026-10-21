#The Absolute file path always start with the root

#The dot in the relative file path indicates "look in the current folder"

with open("../../OneDrive/Desktop/my_file.txt") as file:
    content= file.read()
    print(content)

# file=open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt",mode="w") as file:
#     file.write("New text .")

"""In write mode if the file is not existed then python will create it"""

#By default, the mode is set of read only


# with open("my_file.txt",mode="a") as file:
#     file.write("\nNew text .")
