def affine_encrypt(plaintext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_to_num = {alphabet[i]: i + 1 for i in range(26)}
    num_to_letter = {i + 1: alphabet[i] for i in range(26)}
    num_to_letter[0] = 'Z'
    plaintext = plaintext.upper()
    encrypted_text = ""
    for char in plaintext:
        if char in letter_to_num:
            num = letter_to_num[char]
            num = num + 3
            encrypted_num = (num * 5) % 26
            encrypted_char = num_to_letter[encrypted_num]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter the plaintext: ")
encrypted_text = affine_encrypt(plaintext)
print("Encrypted text:", encrypted_text)
