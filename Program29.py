# Pandas program to calculate total, percentage and grade using apply()

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Math": [80, 90, 70, 85],
    "Science": [85, 88, 75, 80],
    "English": [78, 92, 72, 88]
}

df = pd.DataFrame(data)

print("Student Data:\n", df)
# Output:
#     Name  Math  Science  English
# 0   Amit    80       85       78
# 1   Neha    90       88       92
# 2  Rahul    70       75       72
# 3  Priya    85       80       88

# Calculate Total
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculate Percentage
df["Percentage"] = df["Total"] / 3

# Function for grade
def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "Fail"

# Apply function
df["Grade"] = df["Percentage"].apply(grade)

print("\nFinal Data:\n", df)
# Output:
#     Name  Math  Science  English  Total  Percentage Grade
# 0   Amit    80       85       78    243        81.0     A
# 1   Neha    90       88       92    270        90.0    A+
# 2  Rahul    70       75       72    217        72.3     B
# 3  Priya    85       80       88    253        84.3     A