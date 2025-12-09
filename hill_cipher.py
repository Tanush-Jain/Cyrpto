import numpy as np
import string
ALPHABET = string.ascii_uppercase
MOD = 2
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None 
def calculate_inverse_2x2(K):
    a, b = K[0]
    c, d = K[1]
    det = (a * d - b * c) % MOD
    if det < 0:
        det += MOD
    det_inv = mod_inverse(det, MOD)
    if det_inv is None:
        raise ValueError(f"Key is NOT INVERTIBLE (Determinant {det} has no modular inverse mod 26). The cipher cannot be decrypted with this key.")
    adj = np.array([[d, -b % MOD], [-c % MOD, a]]) % MOD
    K_inv = (det_inv * adj) % MOD
    return K_inv
def text_to_numbers(text):
    return [ALPHABET.index(char) for char in text.upper() if char in ALPHABET]
def numbers_to_text(numbers):
    return "".join([ALPHABET[n % MOD] for n in numbers])
def hill_cipher(text, key_matrix):
    n = key_matrix.shape[0]
    numbers = text_to_numbers(text)
    if len(numbers) % n != 0:
        padding_needed = n - (len(numbers) % n)
        numbers.extend([23] * padding_needed)
    output_numbers = []   
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n]) 
        result_vector = np.dot(block, key_matrix) % MOD
        output_numbers.extend(result_vector.tolist())
    return numbers_to_text(output_numbers)
def get_user_key_matrix():
    """Prompts the user to enter the 4 elements of the 2x2 key matrix."""
    print("\n--- Key Matrix Input (2x2) ---")
    print("Enter 4 integer values for the 2x2 matrix, row by row.")
    print("Example: 9 4 (for the first row) and then 5 7 (for the second row)")
   
    matrix = []
    try:
        for i in range(2):
            row_input = input(f"Enter row {i+1} (two space-separated integers): ")
            row_values = [int(x) for x in row_input.split() if x.strip()]
            if len(row_values) != 2:
                raise ValueError("Must enter exactly two numbers per row.")
            matrix.append(row_values)
        return np.array(matrix)
    except ValueError as e:
        print(f"Input Error: {e}")
        return None
if __name__ == "__main__":
    
    print("--- User-Defined Hill Cipher (2x2) ---")
    print("NOTE: The key you enter must be INVERTIBLE modulo 26 for decryption.")
    print("A known invertible key is: (9 4 / 5 7)")
    print("-" * 50)
    while True:
        KEY_MATRIX = get_user_key_matrix()
        if KEY_MATRIX is None:
            continue
        try:
            INVERSE_KEY_MATRIX = calculate_inverse_2x2(KEY_MATRIX)
            break # Exit loop if key is valid
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try a different key matrix.")
    print(f"\n--- Key Validated ---")
    print(f"Encryption Key (K):\n{KEY_MATRIX}")
    print(f"Decryption Key (K^-1):\n{INVERSE_KEY_MATRIX}")
    print("-" * 50)
    plaintext = input("Enter the plaintext (letters only, spaces ignored): ")
    ciphertext = hill_cipher(plaintext, KEY_MATRIX)
    print(f"\nCiphertext: {ciphertext}")
    decrypted_text = hill_cipher(ciphertext, INVERSE_KEY_MATRIX)
    print(f"Decrypted Text: {decrypted_text}")