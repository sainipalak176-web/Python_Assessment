# Word Frequency Counter

text = input("Enter a paragraph: ")  
# Input: This is a test. This test is simple.

# Convert to lowercase
text = text.lower()

# Remove punctuation
cleaned = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        cleaned += ch

# Split into words
words = cleaned.split()

# Count frequency using dictionary
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:", freq)  
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}

# Find most repeated word
max_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print("Most repeated word:", max_word)  
# Output: Most repeated word: this