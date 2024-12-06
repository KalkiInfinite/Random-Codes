def check_divide(number):
    for digit in str(number):
        if digit != '0' and number % int(digit) != 0:
            return "No"
    return "Yes"

print(check_divide(128))  
print(check_divide(123))  