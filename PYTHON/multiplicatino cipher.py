def multiplicative_encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_to_num = {alphabet[i]: i + 1 for i in range(26)}
    num_to_letter = {i + 1: alphabet[i] for i in range(26)}
    num_to_letter[0] = 'Z'
    plaintext = plaintext.upper()
    encrypted_text = ""
    for char in plaintext:
        if char in letter_to_num:
            num = letter_to_num[char]
            encrypted_num = (num * key) % 26
            encrypted_char = num_to_letter[encrypted_num if encrypted_num != 0 else 26]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (integer): "))
encrypted_text = multiplicative_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
