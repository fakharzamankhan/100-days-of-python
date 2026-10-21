#  functions with outputs
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version"""
    
    if f_name=="" or l_name=="":
        return "Invalid input"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f" Result: {formated_f_name},{formated_l_name}"

formated_string=format_name(input("What is your f_name? "),input("What is your l_name? "))
print(formated_string)
