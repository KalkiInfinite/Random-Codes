def odd_even_numbers(numbers_list):
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    return odd_numbers, even_numbers

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers, even_numbers = odd_even_numbers(numbers_list)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)