def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = 0
composite_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1

print(f"Prime numbers entered: {prime_count}")
print(f"Composite numbers entered: {composite_count}")