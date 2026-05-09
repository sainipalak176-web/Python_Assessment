# Read CSV and display students with attendance below 75%

import pandas as pd

# Create sample CSV file
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
    "Attendance (%)": [80, 72, 65, 90, 74]
}

df = pd.DataFrame(data)
df.to_csv("attendance.csv", index=False)

# Read CSV file
df = pd.read_csv("attendance.csv")

print("Attendance Data:\n", df)
# Output:
#     Name  Attendance (%)
# 0   Amit              80
# 1   Neha              72
# 2  Rahul              65
# 3  Priya              90
# 4  Karan              74

# Filter students below 75%
low_attendance = df[df["Attendance (%)"] < 75]

print("\nStudents with attendance below 75%:\n", low_attendance)
# Output:
#     Name  Attendance (%)
# 1   Neha              72
# 2  Rahul              65
# 4  Karan              74