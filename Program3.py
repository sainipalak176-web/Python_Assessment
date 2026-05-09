# Program to generate first N prime numbers

n = int(input("Enter value of N: "))   # 5

count = 0
num = 2
sum_primes = 0

print("Prime numbers:")

for i in range(1, n+1):
    while True:
        is_prime = True
        
        for j in range(2, int(num/2) + 1):
            if num % j == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")   # Output: 2 3 5 7 11
            sum_primes += num
            num += 1
            break
        else:
            num += 1

# Calculate average
average = sum_primes / n

print("\nSum of prime numbers:", sum_primes)   # Output: Sum of prime numbers: 28
print("Average of prime numbers:", average)   # Output: Average of prime numbers: 5.6