# Program to check voting eligibility with exception handling

try:
    age = int(input("Enter your age: "))   # 18

    if age < 0:
        print("Invalid age! Age cannot be negative.")  
        # Output: Invalid age! Age cannot be negative.

    elif age >= 18:
        print("You are eligible to vote.")  
        # Output: You are eligible to vote.

    else:
        print("You are not eligible to vote.")  
        # Output: You are not eligible to vote.

# Handle non-numeric input
except ValueError:
    print("Error: Please enter a valid number!")  
    # Output: Error: Please enter a valid number!

# Handle any other unexpected error
except Exception as e:
    print("Unexpected Error:", e)