# Set Operations Program

# Input sets from user
set1 = set(map(int, input("Enter elements of Set 1 (space separated): ").split()))  
# Input: 1 2 3 4 5

set2 = set(map(int, input("Enter elements of Set 2 (space separated): ").split()))  
# Input: 4 5 6 7

# Union
union_set = set1 | set2
print("Union:", union_set)  
# Output: Union: {1, 2, 3, 4, 5, 6, 7}

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)  
# Output: Intersection: {4, 5}

# Symmetric Difference
sym_diff = set1 ^ set2
print("Symmetric Difference:", sym_diff)  
# Output: Symmetric Difference: {1, 2, 3, 6, 7}

# Subset check
if set1.issubset(set2):
    print("Set1 is a subset of Set2")  
else:
    print("Set1 is NOT a subset of Set2")  
# Output: Set1 is NOT a subset of Set2

if set2.issubset(set1):
    print("Set2 is a subset of Set1")  
else:
    print("Set2 is NOT a subset of Set1")  
# Output: Set2 is NOT a subset of Set1