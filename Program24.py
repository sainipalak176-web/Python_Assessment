# Function for division with exception handling

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))   # 10
        num2 = float(input("Enter second number: "))  # 0

        result = num1 / num2
        print("Result:", result)

    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")  
        # Output: Error: Cannot divide by zero

    # Handle invalid input (non-numeric)
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")  
        # Output: Error: Invalid input! Please enter numbers only.

    # Handle any other unexpected error
    except Exception as e:
        print("Unexpected Error:", e)


# Function call
divide_numbers()