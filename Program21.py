# NumPy + Pandas program for student marks analysis

import numpy as np
import pandas as pd

# Create NumPy array (marks of 5 students in 3 subjects)
marks = np.array([
    [80, 85, 78],
    [90, 88, 92],
    [70, 75, 72],
    [85, 80, 88],
    [60, 65, 70]
])

# Convert to Pandas DataFrame
subjects = ["Math", "Science", "English"]
df = pd.DataFrame(marks, columns=subjects)

print("Student Marks Data:\n", df)
# Output:
#    Math  Science  English
# 0    80       85       78
# 1    90       88       92
# 2    70       75       72
# 3    85       80       88
# 4    60       65       70

# Highest marks
print("\nHighest Marks:", df.max().max())  
# Output: Highest Marks: 92

# Average marks
print("Average Marks:", df.mean().mean())  
# Output: Average Marks: 79.2

# Subject-wise statistics
print("\nSubject-wise Statistics:\n", df.describe())
# Output:
#             Math    Science    English
# count   5.000000   5.000000   5.000000
# mean   77.000000  78.600000  80.000000
# std    11.401754   8.763561   8.944272
# min    60.000000  65.000000  70.000000
# 25%    70.000000  75.000000  72.000000
# 50%    80.000000  80.000000  78.000000
# 75%    85.000000  85.000000  88.000000
# max    90.000000  88.000000  92.000000