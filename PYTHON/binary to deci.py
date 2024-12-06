binary_num = input("Enter a binary number: ")

decimal_num = 0
for i, digit in enumerate(binary_num[::-1]):
    decimal_num += int(digit) * 2 ** i

print(f"The decimal equivalent of {binary_num} is {decimal_num}")