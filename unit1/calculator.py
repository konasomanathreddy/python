# Simple calculator
def calculator():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operator"

    print("Result:", result)

# Area calculation
def area_calculator():
    print("1. Rectangle  2. Circle  3. Triangle")
    choice = int(input("Choose shape: "))

    if choice == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area:", l * w)
    elif choice == 2:
        r = float(input("Enter radius: "))
        print("Area:", 3.14159 * r * r)
    elif choice == 3:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area:", 0.5 * b * h)
    else:
        print("Invalid choice")

calculator()
area_calculator()