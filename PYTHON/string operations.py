import re

def find_vowel_words(text):
    pattern = r'\b\w{3,4}\b[aeiou]'
    return re.findall(pattern, text, re.IGNORECASE)

input_text = "The quick brown fox jumps over the lazy dog. Aida ate the apple."
vowel_words = find_vowel_words(input_text)
print(vowel_words)