# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Answer =", result)

elif operator == "-":
    result = num1 - num2
    print("Answer =", result)

elif operator == "*":
    result = num1 * num2
    print("Answer =", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Answer =", result)
    else:
        print("Error: You cannot divide by zero.")

else:
    print("Invalid operator.")