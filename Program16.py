# Function to generate Fibonacci numbers up to N
# and store only even Fibonacci numbers

def even_fibonacci(n):
    a, b = 0, 1
    even_list = []

    print("Fibonacci series up to", n, ":")

    while a <= n:
        print(a, end=" ")   # Output: 0 1 1 2 3 5 8 13 21 34

        if a % 2 == 0:
            even_list.append(a)

        a, b = b, a + b

    return even_list


# Input
n = int(input("Enter value of N: "))   # 34

# Function call
result = even_fibonacci(n)

print("\nEven Fibonacci numbers:", result)  
# Output: Even Fibonacci numbers: [0, 2, 8, 34]