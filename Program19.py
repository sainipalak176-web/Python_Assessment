# Function to return factorials of even numbers

def even_factorials(lst):
    result = []

    for num in lst:
        if num % 2 == 0:   # check even number
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            result.append(fact)

    return result


# Example input
numbers = [1, 2, 3, 4, 5, 6]

output = even_factorials(numbers)

print("Factorials of even numbers:", output)  
# Output: Factorials of even numbers: [2, 24, 720]