Here is the clean version of the code with all NumPy dependencies and comments removed.

```python
import string

ALPHABET = string.ascii_uppercase
MOD = 26 

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None 

def calculate_inverse_2x2(K):
    a, b = K[0][0], K[0][1]
    c, d = K[1][0], K[1][1]
    
    det = (a * d - b * c) % MOD
    det_inv = mod_inverse(det, MOD)
    
    if det_inv is None:
        raise ValueError(f"Key is NOT INVERTIBLE mod {MOD}.")
    
    inv_a = (d * det_inv) % MOD
    inv_b = (-b * det_inv) % MOD
    inv_c = (-c * det_inv) % MOD
    inv_d = (a * det_inv) % MOD
    
    return [[inv_a, inv_b], [inv_c, inv_d]]

def text_to_numbers(text):
    return [ALPHABET.index(char) for char in text.upper() if char in ALPHABET]

def numbers_to_text(numbers):
    return "".join([ALPHABET[n % MOD] for n in numbers])

def hill_cipher(text, key_matrix):
    n = 2
    numbers = text_to_numbers(text)
    
    if len(numbers) % n != 0:
        padding_needed = n - (len(numbers) % n)
        numbers.extend([23] * padding_needed)
    
    output_numbers = []   
    for i in range(0, len(numbers), n):
        block = numbers[i:i+n] 
        row_result = []
        for col in range(n):
            sum_val = 0
            for row in range(n):
                sum_val += block[row] * key_matrix[row][col]
            row_result.append(sum_val % MOD)
        output_numbers.extend(row_result)
        
    return numbers_to_text(output_numbers)

def get_user_key_matrix():
    matrix = []
    try:
        for i in range(2):
            row_input = input(f"Enter row {i+1}: ")
            row_values = [int(x) for x in row_input.split() if x.strip()]
            if len(row_values) != 2:
                raise ValueError("Must enter two numbers.")
            matrix.append(row_values)
        return matrix
    except ValueError:
        return None

if __name__ == "__main__":
    while True:
        KEY_MATRIX = get_user_key_matrix()
        if KEY_MATRIX is None:
            continue
        try:
            INVERSE_KEY_MATRIX = calculate_inverse_2x2(KEY_MATRIX)
            break 
        except ValueError as e:
            print(e)

    plaintext = input("Enter plaintext: ")
    ciphertext = hill_cipher(plaintext, KEY_MATRIX)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = hill_cipher(ciphertext, INVERSE_KEY_MATRIX)
    print(f"Decrypted: {decrypted_text}")

```

Would you like me to adapt this code to handle larger matrices (e.g., 3x3 or 4x4) without NumPy?
