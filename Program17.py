# Program to check Armstrong number

n = int(input("Enter a number: "))   # 153

temp = n
sum = 0
digits = len(str(n))

# Loop to calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

# Check Armstrong condition
if sum == n:
    print("It is an Armstrong number")  
    # Output: It is an Armstrong number
else:
    print("It is not an Armstrong number")