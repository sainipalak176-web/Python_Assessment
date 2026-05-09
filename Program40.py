# Mini Student Management System

import pandas as pd

students = {}

# ---------------- FUNCTIONS ---------------- #

# Add student
def add_student():
    try:
        roll = int(input("Enter Roll No: "))   # 1
        name = input("Enter Name: ")           # Amit
        marks = int(input("Enter Marks: "))    # 85

        students[roll] = {"Name": name, "Marks": marks}
        print("Student added!")  
        # Output: Student added!

    except ValueError:
        print("Invalid input!")


# Update student
def update_student():
    try:
        roll = int(input("Enter Roll No to update: "))   # 1

        if roll in students:
            marks = int(input("Enter new marks: "))      # 90
            students[roll]["Marks"] = marks
            print("Updated successfully!")  
            # Output: Updated successfully!
        else:
            print("Student not found!")

    except ValueError:
        print("Invalid input!")


# Display students
def display_students():
    print("Student Records:", students)
    # Output: {1: {'Name': 'Amit', 'Marks': 90}}


# Save to file
def save_to_file():
    with open("students.txt", "w") as f:
        for roll, data in students.items():
            f.write(f"{roll},{data['Name']},{data['Marks']}\n")

    print("Data saved to file!")  
    # Output: Data saved to file!


# Load from file
def load_from_file():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                students[int(roll)] = {"Name": name, "Marks": int(marks)}

        print("Data loaded!")  
        # Output: Data loaded!

    except FileNotFoundError:
        print("File not found!")


# Generate report using Pandas
def generate_report():
    if not students:
        print("No data available!")
        return

    df = pd.DataFrame.from_dict(students, orient='index')
    df.index.name = "Roll No"

    print("\nStudent Report:\n", df)
    # Output:
    #          Name  Marks
    # Roll No
    # 1        Amit     90

    print("\nStatistics:\n", df.describe())
    # Output:
    #           Marks
    # count      1.0
    # mean      90.0
    # std        NaN
    # min       90.0
    # 25%       90.0
    # 50%       90.0
    # 75%       90.0
    # max       90.0


# ---------------- MENU ---------------- #

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Save to File")
    print("5. Load from File")
    print("6. Generate Report")
    print("7. Exit")

    choice = int(input("Enter choice: "))   # 1

    if choice == 1:
        add_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        display_students()
    elif choice == 4:
        save_to_file()
    elif choice == 5:
        load_from_file()
    elif choice == 6:
        generate_report()
    elif choice == 7:
        print("Exiting program...")  
        # Output: Exiting program...
        break
    else:
        print("Invalid choice!")