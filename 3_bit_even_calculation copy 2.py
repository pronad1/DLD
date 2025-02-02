def even_parity(x1, x2, x3):
    return x1 ^ x2 ^ x3  # XOR operation

# Test cases
for x1 in [0, 1]:
    for x2 in [0, 1]:
        for x3 in [0, 1]:
            print(f"X1: {x1}, X2: {x2}, X3: {x3} -> P_even: {even_parity(x1, x2, x3)}")
