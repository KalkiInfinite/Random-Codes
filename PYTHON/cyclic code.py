import numpy as np

def binary_to_polynomial(binary):
    return [int(bit) for bit in str(binary)]

def polynomial_division(dividend, divisor):
    dividend = np.array(dividend, dtype=int)
    divisor = np.array(divisor, dtype=int)
    dividend_len = len(dividend)
    divisor_len = len(divisor)
    temp = dividend.copy()
    for i in range(dividend_len - divisor_len + 1):
        if temp[i] == 1:
            for j in range(divisor_len):
                temp[i + j] ^= divisor[j]
    return temp[-(divisor_len - 1):].tolist()

def crc_encode(data_bits, generator):
    data = binary_to_polynomial(data_bits)
    gen = binary_to_polynomial(generator)
    n_k = len(gen) - 1
    padded_data = data + [0] * n_k
    remainder = polynomial_division(padded_data, gen)
    codeword = data + remainder
    return codeword

def validate_binary_input(input_str):
    return all(bit in '01' for bit in input_str)

def get_user_input():
    while True:
        try:
            data_bits = input("\nEnter message bits: ")
            if not validate_binary_input(data_bits):
                print("Error: Message bits must contain only 0s and 1s")
                continue
            if len(data_bits) == 0:
                print("Error: Message bits cannot be empty")
                continue
            generator = input("Enter generator polynomial: ")
            if not validate_binary_input(generator):
                print("Error: Generator must contain only 0s and 1s")
                continue
            if len(generator) <= 1:
                print("Error: Generator polynomial must be at least 2 bits long")
                continue
            if generator[0] != '1':
                print("Error: Generator polynomial must start with 1")
                continue
            return data_bits, generator
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def run_interactive_simulation():
    data_bits, generator = get_user_input()
    print(f"\nInput Summary:")
    print(f"Data bits (d(x)): {data_bits}")
    print(f"Generator (g(x)): {generator}")
    codeword = crc_encode(data_bits, generator)
    print("\nResults:")
    print(f"Generated codeword: {''.join(map(str, codeword))}")
    n = len(codeword)
    k = len(data_bits)
    rate = k / n
    print(f"\nTheoretical Analysis:")
    print(f"Code length (n): {n}")
    print(f"Message length (k): {k}")
    print(f"Code rate (k/n): {rate:.2f}")
    print("\nPolynomial Representations:")
    print("Message polynomial d(x):", end=" ")
    for i, bit in enumerate(reversed(data_bits)):
        if bit == '1':
            if i == 0:
                print("1", end="")
            elif i == 1:
                print("x", end="")
            else:
                print(f"x^{i}", end="")
            if i != len(data_bits) - 1:
                print(" + ", end="")
    print("\nGenerator polynomial g(x):", end=" ")
    for i, bit in enumerate(reversed(generator)):
        if bit == '1':
            if i == 0:
                print("1", end="")
            elif i == 1:
                print("x", end="")
            else:
                print(f"x^{i}", end="")
            if i != len(generator) - 1:
                print(" + ", end="")
    print("\n")
    return codeword

if __name__ == "__main__":
    run_interactive_simulation()
