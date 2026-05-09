# Calculator with Exception Handling

try:
    num1 = float(input("Enter first number: "))   # 10
    num2 = float(input("Enter second number: "))  # 0
    op = input("Enter operator (+, -, *, /): ")   # /

    if op == '+':
        result = num1 + num2
        print("Result:", result)  
        # Output: Result: 10.0

    elif op == '-':
        result = num1 - num2
        print("Result:", result)

    elif op == '*':
        result = num1 * num2
        print("Result:", result)

    elif op == '/':
        result = num1 / num2   # This will raise ZeroDivisionError
        print("Result:", result)

    else:
        raise ValueError("Invalid operator")

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero")  
    # Output: Error: Cannot divide by zero

# Handle invalid number input
except ValueError:
    print("Error: Invalid input or operator")  
    # Output: Error: Invalid input or operator

# Handle any other unexpected error
except Exception as e:
    print("Unexpected Error:", e)