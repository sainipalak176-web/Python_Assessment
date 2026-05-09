# Program to store employee records in tuples
# and display employees with salary above average

# Employee records (id, name, salary)
employees = [
    (101, "Amit", 25000),
    (102, "Neha", 30000),
    (103, "Rahul", 20000),
    (104, "Priya", 35000),
    (105, "Karan", 28000)
]

# Calculate total salary
total_salary = 0
for emp in employees:
    total_salary += emp[2]

# Calculate average salary
avg_salary = total_salary / len(employees)
print("Average Salary:", avg_salary)  
# Output: Average Salary: 27600.0

# Display employees with salary above average
print("Employees with salary above average:")

for emp in employees:
    if emp[2] > avg_salary:
        print(emp)  
        # Output:
        # (102, 'Neha', 30000)
        # (104, 'Priya', 35000)
        # (105, 'Karan', 28000)