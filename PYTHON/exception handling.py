class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise InvalidPasswordError("Password must contain at least one uppercase letter.")
    if not any(char in "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/~" for char in password):
        raise InvalidPasswordError("Password must contain at least one special character.")
    return True

while True:
    try:
        password = input("Enter a password: ")
        if validate_password(password):
            print("Password is valid.")
            break
    except InvalidPasswordError as e:
        print("Invalid password. Please try again.")
        print(e)