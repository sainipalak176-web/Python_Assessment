# NumPy program for matrix operations

import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
# Output:
# [[1 2]
#  [3 4]]

print("Matrix B:\n", B)
# Output:
# [[5 6]
#  [7 8]]

# Addition
add = A + B
print("\nAddition:\n", add)
# Output:
# [[ 6  8]
#  [10 12]]

# Subtraction
sub = A - B
print("\nSubtraction:\n", sub)
# Output:
# [[-4 -4]
#  [-4 -4]]

# Multiplication (Matrix multiplication)
mul = np.dot(A, B)
print("\nMultiplication:\n", mul)
# Output:
# [[19 22]
#  [43 50]]

# Inverse of Matrix A
inv_A = np.linalg.inv(A)
print("\nInverse of A:\n", inv_A)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Inverse of Matrix B
inv_B = np.linalg.inv(B)
print("\nInverse of B:\n", inv_B)
# Output:
# [[-4.   3. ]
#  [ 3.5 -2.5]]