# Write a python program to perform encryption and decryption using the
# following algorithms
# a) Ceaser Cipher
# b) Substitution Cipher
# c) Hill Cipher



def caes_cip(text, shift):
    result = ""      
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            asci_offset = 65 if char.isupper() else 97

            new_char = chr((ord(char) - asci_offset + shift_amount) % 26 + asci_offset)
            result += new_char
        else:
            result += char           
    return result  
def decrypt_caes_cip(text, shift):
    return caes_cip(text, -shift)

if __name__ == "__main__":
    plaintext = input("Enter the plain text: ")
    try:
        shift = int(input("Enter the number of shifts: "))
    except ValueError:
        print("Error: Shift must be a whole number.")
        exit()
    ciphertext = caes_cip(plaintext, shift)
    print("\nCipher Text :", ciphertext)
    print("Shift Amount:", shift)
    original_text = decrypt_caes_cip(ciphertext, shift)
    print("Original Text :", original_text)