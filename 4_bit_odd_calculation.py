def odd_parity(x1, x2, x3, x4):
    even_parity = x1 ^ x2 ^ x3 ^ x4  # XOR operation
    odd_parity = not even_parity     # Invert the result
    return int(odd_parity)           # Convert boolean to integer (0 or 1)

# Example usage:
for x1 in [0, 1]:
    for x2 in [0, 1]:
        for x3 in [0, 1]:
            for x4 in [0, 1]:
                print(f"X1: {x1}, X2: {x2}, X3: {x3}, X4: {x4} -> P_odd: {odd_parity(x1, x2, x3, x4)}")
