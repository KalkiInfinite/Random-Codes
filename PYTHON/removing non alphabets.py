import re

def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text)

input_text = "Hello, World! 123"
cleaned_text = remove_non_alphanumeric(input_text)
print(cleaned_text)  