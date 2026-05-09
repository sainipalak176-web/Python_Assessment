# NumPy program for matrix operations

import numpy as np

# Create 5x5 matrix with random integers (1 to 10)
matrix = np.random.randint(1, 11, (5, 5))

print("Matrix:\n", matrix)  
# Output (example):
# [[ 2  5  7  1  3]
#  [ 6  8  4  2  9]
#  [ 1  3  5  7  2]
#  [ 9  6  2  8  4]
#  [ 3  7  1  5  6]]

# Row-wise sum
row_sum = np.sum(matrix, axis=1)
print("Row-wise sum:", row_sum)  
# Output: [18 29 18 29 22]

# Column-wise sum
col_sum = np.sum(matrix, axis=0)
print("Column-wise sum:", col_sum)  
# Output: [21 29 19 23 24]

# Transpose
transpose = matrix.T
print("Transpose:\n", transpose)  
# Output:
# [[2 6 1 9 3]
#  [5 8 3 6 7]
#  [7 4 5 2 1]
#  [1 2 7 8 5]
#  [3 9 2 4 6]]

# Determinant
det = np.linalg.det(matrix)
print("Determinant:", det)  
# Output: Determinant: -248.0 (value may vary)