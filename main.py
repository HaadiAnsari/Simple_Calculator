keep_going = True

print("Welcome to the calculator!")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while keep_going:
    operation = input("Enter 'add', 'subtract', 'multiply', 'divide': ")
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))

    if operation.lower() == "add":
        print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
    elif operation.lower() == "subtract":
        print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
    elif operation.lower() == "multiply":
        print(f"{first_number} x {second_number} = {multiply(first_number, second_number)}")
    elif operation.lower() == "divide":
        if second_number == 0:
            print("Cannot divide by 0!")
        else:
            print(f"{first_number} / {second_number} = {divide(first_number, second_number)}")
    else:
        print("Invalid operation!")




