# Banking Application

balance = 0

while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))   # 1

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))   # 1000
        balance += amount
        print("Amount deposited successfully!")  
        # Output: Amount deposited successfully!

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))   # 500
        if amount > balance:
            print("Insufficient balance!")  
            # Output: Insufficient balance!
        else:
            balance -= amount
            print("Amount withdrawn successfully!")  
            # Output: Amount withdrawn successfully!

    elif choice == 3:
        print("Current balance:", balance)  
        # Output: Current balance: 500.0

    elif choice == 4:
        print("Thank you for using banking system!")  
        # Output: Thank you for using banking system!
        break

    else:
        print("Invalid choice! Please try again.")