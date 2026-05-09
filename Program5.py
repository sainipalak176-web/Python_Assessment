# Function to find second smallest and second largest (without sorting)

def find_second_elements(arr):
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in arr:
        # For smallest & second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

        # For largest & second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_smallest, second_largest


# Example input
numbers = [10, 5, 20, 8, 15]

result = find_second_elements(numbers)

print("Second Smallest:", result[0])   # Output: Second Smallest: 8
print("Second Largest:", result[1])    # Output: Second Largest: 15