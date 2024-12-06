numbers = input("Enter a list of numbers: ")
numbers_list = [int(x) for x in numbers.split()]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_list))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)