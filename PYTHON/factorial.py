def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a positive integer to calculate its factorial: "))
if n > 0:
    print("Factorial is:", factorial(n))
else:
    print("Please enter a positive integer!")
