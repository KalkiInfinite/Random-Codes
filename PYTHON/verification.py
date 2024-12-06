import re

def is_valid_credit_card(card_number):
    card_number = card_number.replace("-", "")

    if not card_number.startswith(("4", "5", "6")):
        return False

    if len(card_number) != 16:
        return False

    if not card_number.isdigit():
        return False

    return True

credit_card_number = input("Enter the credit card number: ")
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")