# Program to copy contents from one file to another
# and count total number of words copied

try:
    # Open source file
    source = open("source.txt", "r")
    # Assume source.txt contains:
    # This is a sample file
    # It contains some words

    content = source.read()
    source.close()

    # Count words
    words = content.split()
    word_count = len(words)

    # Open destination file
    dest = open("destination.txt", "w")
    dest.write(content)
    dest.close()

    print("File copied successfully!")  
    # Output: File copied successfully!

    print("Total words copied:", word_count)  
    # Output: Total words copied: 9

# Handle file not found
except FileNotFoundError:
    print("Error: Source file not found!")  
    # Output: Error: Source file not found!

# Handle other errors
except Exception as e:
    print("Error:", e)