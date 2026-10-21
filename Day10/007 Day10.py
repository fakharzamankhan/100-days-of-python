def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

mathe_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}

num1=int(input("Enter the first number: "))


for symbol in mathe_operations:
    print(symbol)
operation_symbol = input("Pick an operation from the above line: ")
num2=int(input("Enter the second number: "))

calculation_function=mathe_operations[operation_symbol]
first_answer=calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick an other operation from the above line: ")
num3=int(input("Enter the next number: "))

calculation_function=mathe_operations[operation_symbol]
second_answer=calculation_function(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")





