# Mathematical Utility Program

# Function for factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

# Function to check Armstrong number
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


# Menu-driven program
while True:
    print("\n--- Math Utility Menu ---")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Armstrong Check")
    print("4. Exit")

    choice = int(input("Enter your choice: "))   # 1

    if choice == 1:
        num = int(input("Enter number: "))   # 5
        print("Factorial:", factorial(num))  
        # Output: Factorial: 120

    elif choice == 2:
        num = int(input("Enter number: "))   # 7
        if is_prime(num):
            print("It is a Prime Number")  
            # Output: It is a Prime Number
        else:
            print("Not a Prime Number")

    elif choice == 3:
        num = int(input("Enter number: "))   # 153
        if is_armstrong(num):
            print("It is an Armstrong Number")  
            # Output: It is an Armstrong Number
        else:
            print("Not an Armstrong Number")

    elif choice == 4:
        print("Exiting program...")  
        # Output: Exiting program...
        break

    else:
        print("Invalid choice!")