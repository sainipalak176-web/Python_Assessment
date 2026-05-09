# Merge two lists, remove duplicates, sort in descending order,
# and display numbers divisible by both 3 and 5

list1 = [10, 15, 20, 30, 45]
list2 = [5, 15, 25, 30, 60]

# Merge lists
merged_list = list1 + list2
print("Merged List:", merged_list)  
# Output: Merged List: [10, 15, 20, 30, 45, 5, 15, 25, 30, 60]

# Remove duplicates
unique_list = []
for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)  
# Output: [10, 15, 20, 30, 45, 5, 25, 60]

# Sort in descending order (without built-in sort)
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):
        if unique_list[i] < unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

print("Sorted List (Descending):", unique_list)  
# Output: [60, 45, 30, 25, 20, 15, 10, 5]

# Display numbers divisible by both 3 and 5 (i.e., divisible by 15)
print("Numbers divisible by both 3 and 5:")

for num in unique_list:
    if num % 15 == 0:
        print(num, end=" ")  
        # Output: 60 45 30 15