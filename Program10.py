# Program to check palindrome after removing spaces, punctuation, and converting to lowercase

import string

text = input("Enter a string: ")   # A man, a plan, a canal: Panama

# Convert to lowercase
text = text.lower()

# Remove spaces and punctuation
cleaned = ""
for ch in text:
    if ch not in string.punctuation and ch != " ":
        cleaned += ch

print("Processed string:", cleaned)  
# Output: Processed string: amanaplanacanalpanama

# Check palindrome
if cleaned == cleaned[::-1]:
    print("It is a palindrome")  
    # Output: It is a palindrome
else:
    print("It is not a palindrome")