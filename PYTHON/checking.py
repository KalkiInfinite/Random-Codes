import re

def extract_phone_numbers(text):
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

text = """
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800.555.5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560.555.5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com
"""

phone_numbers = extract_phone_numbers(text)
print(phone_numbers)