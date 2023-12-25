def add(a,b):
    return a+b
#
def subtract(a,b):
    return a+b
#
def multiply(a,b):
    return a+b
#
def divide(a,b):
    return a+b
#

operators = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
for operation in operators:
    print(operation)

operation_symbol = input("Enter the operation you want to perform : ")

operators[operation_symbol](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {operators[operation_symbol](num1,num2)}")

