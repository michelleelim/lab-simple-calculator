print("Enter the first number:")
num1 = float(input())
print("Enter the second number:")
num2 = float(input())
print("Enter an operation (+, -, *, /):")
operator = input()

if operator == "+":
    print("The result is ", num1 + num2)
elif operator == "-":
    print("The result is ", num1 - num2)
elif operator == "*":
    print("The result is ", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Oops! You can't divide by zero.")
    else:
        print("The result is ", num1 / num2)