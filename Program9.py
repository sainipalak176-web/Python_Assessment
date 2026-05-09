# Inventory Management System

inventory = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock")
    print("5. Exit")

    choice = int(input("Enter your choice: "))   # 1

    # Add Product
    if choice == 1:
        name = input("Enter product name: ")   # Apple
        qty = int(input("Enter quantity: "))   # 10
        inventory[name] = qty
        print("Product added successfully!")  
        # Output: Product added successfully!

    # Update Quantity
    elif choice == 2:
        name = input("Enter product name: ")   # Apple
        if name in inventory:
            qty = int(input("Enter new quantity: "))   # 5
            inventory[name] = qty
            print("Quantity updated!")  
            # Output: Quantity updated!
        else:
            print("Product not found!")

    # Search Product
    elif choice == 3:
        name = input("Enter product name: ")   # Apple
        if name in inventory:
            print("Product:", name, "Quantity:", inventory[name])  
            # Output: Product: Apple Quantity: 5
        else:
            print("Product not found!")

    # Display Low Stock (less than 10)
    elif choice == 4:
        print("Low stock products:")
        for item in inventory:
            if inventory[item] < 10:
                print(item, ":", inventory[item])  
                # Output: Apple : 5

    # Exit
    elif choice == 5:
        print("Exiting program...")  
        # Output: Exiting program...
        break

    else:
        print("Invalid choice!")