# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Input
message = input("Enter message: ")   # HELLO
shift = int(input("Enter shift value: "))   # 3

# Encryption
encrypted = encrypt(message, shift)
print("Encrypted Message:", encrypted)  
# Output: Encrypted Message: KHOOR

# Decryption
decrypted = decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)  
# Output: Decrypted Message: HELLO