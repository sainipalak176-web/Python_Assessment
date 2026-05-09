# File Processing Program with Exception Handling

try:
    filename = input("Enter file name: ")   # sample.txt

    file = open(filename, "r")

    lines = 0
    words = 0
    characters = 0

    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

    file.close()

    print("Total Lines:", lines)  
    # Output: Total Lines: 3

    print("Total Words:", words)  
    # Output: Total Words: 12

    print("Total Characters:", characters)  
    # Output: Total Characters: 65

# Handle file not found error
except FileNotFoundError:
    print("Error: File not found!")  
    # Output: Error: File not found!

# Handle any other error
except Exception as e:
    print("Error:", e)