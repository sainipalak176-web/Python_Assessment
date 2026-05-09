# Pandas program for employee data analysis

import pandas as pd

# Create sample CSV file
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 70000, 65000]
}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)

# Read CSV file
df = pd.read_csv("employees.csv")

print("Employee Data:\n", df)
# Output:
#     Name Department  Salary
# 0   Amit         IT   50000
# 1   Neha         HR   60000
# 2  Rahul         IT   55000
# 3  Priya    Finance   70000
# 4  Karan         HR   65000

# Department-wise average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nDepartment-wise Average Salary:\n", avg_salary)
# Output:
# Department
# Finance    70000.0
# HR         62500.0
# IT         52500.0

# Highest salary employee
max_row = df.loc[df["Salary"].idxmax()]
print("\nHighest Salary Employee:\n", max_row)
# Output:
# Name          Priya
# Department  Finance
# Salary        70000