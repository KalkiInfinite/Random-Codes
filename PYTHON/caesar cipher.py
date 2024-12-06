def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

text = input("Enter text: ")
shift = int(input("Enter shift key: "))
encrypted_text = caesar_encrypt(text, shift)
print(f"Encrypted Text: {encrypted_text}")
decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Decrypted Text: {decrypted_text}")
