def calculate_parity_bits(data_bits):
    D2, D4, D5, D6, D8, D9, D10 = data_bits
    R0 = D2 ^ D4 ^ D6 ^ D8 ^ D10
    R1 = D2 ^ D5 ^ D6 ^ D9 ^ D10
    R2 = D4 ^ D5 ^ D6
    R3 = D8 ^ D9 ^ D10
    return [R0, R1, R2, R3]

def generate_hamming_code(data_bits):
    R0, R1, R2, R3 = calculate_parity_bits(data_bits)
    hamming_code = [R0, R1, data_bits[0], R2, data_bits[1], data_bits[2], data_bits[3], R3, data_bits[4], data_bits[5], data_bits[6]]
    return hamming_code

def correct_hamming_code(received_code):
    R0, R1, D2, R2, D4, D5, D6, R3, D8, D9, D10 = received_code
    R0_check = R0 ^ D2 ^ D4 ^ D6 ^ D8 ^ D10
    R1_check = R1 ^ D2 ^ D5 ^ D6 ^ D9 ^ D10
    R2_check = R2 ^ D4 ^ D5 ^ D6
    R3_check = R3 ^ D8 ^ D9 ^ D10
    h = 8 * R3_check + 4 * R2_check + 2 * R1_check + 1 * R0_check
    if h == 0:
        print("No error in the received code.")
    else:
        print(f"Error detected at position: {h}")
    received_code[h-1] = 1 - received_code[h-1]
    return received_code

if __name__ == "__main__":
    data_bits = [1, 1, 1, 1, 1, 1, 1]
    hamming_code = generate_hamming_code(data_bits)
    print("Generated 11-bit Hamming code:", hamming_code)
    received_code = hamming_code.copy()
    received_code[9] = 0
    print("Received code with error:", received_code)
    corrected_code = correct_hamming_code(received_code)
    print("Corrected Hamming code:", corrected_code)
