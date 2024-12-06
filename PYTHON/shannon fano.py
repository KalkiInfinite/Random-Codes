import math

def shannon_fano(symbols, probabilities):
    sorted_indices = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)
    sorted_symbols = [symbols[i] for i in sorted_indices]
    sorted_probabilities = [probabilities[i] for i in sorted_indices]
    codes = [''] * len(symbols)

    def assign_codes(start, end):
        if start == end:
            return
        total = sum(sorted_probabilities[start:end+1])
        cumulative = 0
        split = start
        for i in range(start, end+1):
            cumulative += sorted_probabilities[i]
            if cumulative >= total / 2:
                split = i
                break
        for i in range(start, split+1):
            codes[sorted_indices[i]] += '0'
        for i in range(split+1, end+1):
            codes[sorted_indices[i]] += '1'
        assign_codes(start, split)
        assign_codes(split+1, end)

    assign_codes(0, len(symbols)-1)
    codebook = {symbols[i]: codes[i] for i in range(len(symbols))}
    return codebook

def calculate_entropy(probabilities):
    entropy = 0
    for prob in probabilities:
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy

def calculate_avg_length(probabilities, codes, symbols):
    avg_length = 0
    symbol_to_prob = dict(zip(symbols, probabilities))
    for symbol, code in codes.items():
        prob = symbol_to_prob[symbol]
        length = len(code)
        avg_length += prob * length
    return avg_length

def calculate_efficiency(entropy, avg_length):
    return entropy / avg_length

def main():
    num_messages = int(input("Enter the number of symbols: "))
    symbols = []
    probabilities = []

    for _ in range(num_messages):
        symbol = input("Enter symbol: ")
        while True:
            try:
                probability = float(input("Enter probability: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number for the probability.")
        symbols.append(symbol)
        probabilities.append(probability)

    total_prob = sum(probabilities)
    if not math.isclose(total_prob, 1.0):
        print(f"Warning: Probabilities sum to {total_prob:.4f}, expected 1.0")
        return

    codebook = shannon_fano(symbols, probabilities)
    entropy = calculate_entropy(probabilities)
    avg_length = calculate_avg_length(probabilities, codebook, symbols)
    efficiency = calculate_efficiency(entropy, avg_length)

    print("\nShannon-Fano Codes:")
    for symbol in sorted(codebook):
        print(f"Symbol: {symbol}, Code: {codebook[symbol]}")
    print(f"\nEntropy: {entropy:.4f} bits")
    print(f"Average Code Length: {avg_length:.4f} bits")
    print(f"Efficiency: {efficiency * 100:.2f}%")

if __name__ == "__main__":
    main()
