# Recursive function to find sum of digits
def sum_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + sum_recursive(n // 10)


# Iterative approach
def sum_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# Input
num = int(input("Enter a number: "))   # 1234

# Function calls
rec_result = sum_recursive(num)
iter_result = sum_iterative(num)

print("Recursive Sum:", rec_result)  
# Output: Recursive Sum: 10

print("Iterative Sum:", iter_result)  
# Output: Iterative Sum: 10