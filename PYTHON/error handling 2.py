class EmptyListError(Exception):
    pass

def calculate_average(numbers):
    if not numbers:
        raise EmptyListError("Cannot calculate the average of an empty list.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    input_str = input("Enter a list of numbers (space-separated): ")
    numbers = list(map(float, input_str.split()))
    
    average = calculate_average(numbers)
    print("Average:", average)
except ValueError:
    print("Invalid input. Please enter a valid list of numbers.")
except EmptyListError as e:
    print("Error:", str(e))
