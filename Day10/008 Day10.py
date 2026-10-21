# calculator
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def power(n1,n2):
    return n1**n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power

}
# function= operations["*"]
# function(2,3)
def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number? "))
        cal_fun=operations[operation_symbol]
        answer=cal_fun(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} ,or type 'n' to exit.: ") == "y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()
