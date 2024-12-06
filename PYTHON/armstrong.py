def is_armstrong(num):
    original_num = num
    arm_sum = 0
    while num > 0:
        digit = num % 10
        arm_sum += digit ** len(str(original_num))
        num //= 10
    return original_num == arm_sum

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")