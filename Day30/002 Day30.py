#file not found
# with open("a_file.txt") as file:
#     file.read()
#key error
# a_dictionary={"key":"value"}
# value=a_dictionary["new_key"]
#index error
# fruit_list=["apple","banana","orange","mango"]
# fruit=fruit_list[4]
#type error
# text='abc'
# print(text+5)

try:
    file = open("passwords.txt")
    a_dictionary={"key":"value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("passwords.txt","w")
    file.write("Welcome to 100 Days of Code")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")
    # print("Key Error")
else:
    content=file.read()
    print(content)
finally:
    raise KeyError("This is an error")
    file.close()
    print("The file has been closed")
