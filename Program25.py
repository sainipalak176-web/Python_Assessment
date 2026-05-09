# Program to store word frequencies from a file and display top 5 words

import string

try:
    # Open file
    file = open("sample.txt", "r")
    # Assume file content:
    # This is a test file. This file is simple. Test file example.

    text = file.read().lower()
    file.close()

    # Remove punctuation
    cleaned = ""
    for ch in text:
        if ch.isalnum() or ch == " ":
            cleaned += ch

    # Split into words
    words = cleaned.split()

    # Count frequency
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print("Word Frequencies:", freq)
    # Output: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'file': 3, 'simple': 1, 'example': 1}

    # Sort words by frequency (descending)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Display top 5 words
    print("Top 5 most frequent words:")
    for word, count in sorted_words[:5]:
        print(word, ":", count)
        # Output:
        # file : 3
        # this : 2
        # is : 2
        # test : 2
        # a : 1

# Handle file not found
except FileNotFoundError:
    print("Error: File not found!")

# Handle other errors
except Exception as e:
    print("Error:", e)