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

#calculation_function=mathe_operations[operation_symbol]
#answer=calculation_function(num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")

if operation_symbol in mathe_operations:
    print(f"{num1} {operation_symbol} {num2} = {mathe_operations[operation_symbol](num1,num2)}")
else:
    print("Invalid operation")

