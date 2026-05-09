# Program to separate vowels and consonants

sentence = input("Enter a sentence: ")  
# Input: Hello World

vowels = []
consonants = []

for ch in sentence:
    if ch.isalpha():   # check only alphabets
        if ch.lower() in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels:", vowels)  
# Output: Vowels: ['e', 'o', 'o']

print("Consonants:", consonants)  
# Output: Consonants: ['H', 'l', 'l', 'W', 'r', 'l', 'd']