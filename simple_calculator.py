print("Enter a math expression:")
expression = input()
parts = expression.strip().split()

if len(parts) != 3:
    print("Invalid expression.")

else:
    num1_str, operator, num2_str = parts
    num1 = float(num1_str)
    num2 = float(num2_str)

    if operator == "+":
        print("Tada! You get ", num1 + num2)
    elif operator == "-":
        print("Tada! You get ", num1 - num2)
    elif operator == "*":
        print("Tada! You get ", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Oops! You can't divide by zero.")
        else:
            print("Tada! You get ", num1 / num2)
    else:
        print("Sorry, I don’t know how to do that operation.")