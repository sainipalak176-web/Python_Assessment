# Contact Management System

contacts = []

while True:
    print("\n--- Contact Menu ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))   # 1

    # Add Contact
    if choice == 1:
        name = input("Enter name: ")    # Amit
        phone = input("Enter phone: ")  # 9876543210

        contacts.append({"name": name, "phone": phone})
        print("Contact added!")  
        # Output: Contact added!

    # Update Contact
    elif choice == 2:
        name = input("Enter name to update: ")   # Amit
        found = False

        for c in contacts:
            if c["name"] == name:
                new_phone = input("Enter new phone: ")   # 9999999999
                c["phone"] = new_phone
                print("Contact updated!")  
                # Output: Contact updated!
                found = True
                break

        if not found:
            print("Contact not found!")

    # Search Contact
    elif choice == 3:
        name = input("Enter name to search: ")   # Amit
        found = False

        for c in contacts:
            if c["name"] == name:
                print("Contact found:", c)  
                # Output: Contact found: {'name': 'Amit', 'phone': '9999999999'}
                found = True
                break

        if not found:
            print("Contact not found!")

    # Delete Contact
    elif choice == 4:
        name = input("Enter name to delete: ")   # Amit
        found = False

        for c in contacts:
            if c["name"] == name:
                contacts.remove(c)
                print("Contact deleted!")  
                # Output: Contact deleted!
                found = True
                break

        if not found:
            print("Contact not found!")

    # Exit
    elif choice == 5:
        print("Exiting program...")  
        # Output: Exiting program...
        break

    else:
        print("Invalid choice!")