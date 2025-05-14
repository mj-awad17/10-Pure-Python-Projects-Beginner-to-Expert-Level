def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print("Welcome to the Simple Calculator!")
print('Type "exit" at any time to quit.\n')

while True:
    # Get first number
    first_input = input("Enter first number: ")
    if first_input.lower() in ['exit', 'stop']:
        print("👋 Thanks for using the calculator. Goodbye!")
        break

    try:
        num1 = float(first_input)
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.\n")
        continue

    # Get operation
    operation = input("Enter operation (+, -, *, /): ")
    if operation.lower() in ['exit', 'stop']:
        print("👋 Thanks for using the calculator. Goodbye!")
        break
    if operation not in ['+', '-', '*', '/']:
        print("❌ Invalid operation. Choose from +, -, *, /.\n")
        continue

    # Get second number
    second_input = input("Enter second number: ")
    if second_input.lower() in ['exit', 'stop']:
        print("👋 Thanks for using the calculator. Goodbye!")
        break

    try:
        num2 = float(second_input)
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.\n")
        continue

    # Perform calculation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print(f"✅ Result: {result}\n")

    # Ask if user wants to continue
    next_action = input("Would you like to calculate again? (yes/exit): ")
    if next_action.lower() in ['exit', 'stop', 'no']:
        print("👋 Thanks for using the calculator. See you next time!")
        break

    print()  # Add a blank line for clarity
