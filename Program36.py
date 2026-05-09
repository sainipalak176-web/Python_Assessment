# ATM Simulation with PIN validation

correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your PIN: ")   # 1111

    if pin == correct_pin:
        print("Access granted!")  
        # Output: Access granted!
        break
    else:
        attempts += 1
        print("Invalid PIN!")  
        # Output: Invalid PIN!

        if attempts == max_attempts:
            print("Account locked due to 3 incorrect attempts.")  
            # Output: Account locked due to 3 incorrect attempts.
        else:
            print("Attempts left:", max_attempts - attempts)  
            # Output: Attempts left: 2