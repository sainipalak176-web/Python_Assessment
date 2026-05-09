# Program to count uppercase, lowercase, digits, spaces, and special characters

# Input paragraph from user
text = input("Enter a paragraph:\n")

# Initialize counters
uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

# Count characters
for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

# Store results
result = {
    "Uppercase Letters": uppercase,
    "Lowercase Letters": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special Characters": special
}

# Sort in descending order based on frequency
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Display output
print("\nCharacter Frequency Analysis (Descending Order):")
for category, count in sorted_result:
    print(f"{category}: {count}")


"""
Sample Output:

Enter a paragraph:
Hello World! 123

Character Frequency Analysis (Descending Order):
Lowercase Letters: 8
Digits: 3
Uppercase Letters: 2
Spaces: 2
Special Characters: 1
"""