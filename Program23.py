# Program to print number pyramid and calculate sum

n = int(input("Enter number of rows: "))   # 4

sum_total = 0

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print numbers
    for k in range(1, i + 1):
        print(k, end=" ")
        sum_total += k

    print()

print("Sum of all numbers:", sum_total)  
# Output:
#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
# Sum of all numbers: 20