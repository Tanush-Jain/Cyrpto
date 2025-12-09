from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii
def encrypt_des(key, data):
    key_bytes = key.encode('utf-8')
    cipher = DES.new(key_bytes, DES.MODE_CBC)
    padded_data = pad(data.encode('utf-8'), DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    iv_hex = binascii.hexlify(cipher.iv).decode('utf8')
    ciphertext_hex = binascii.hexlify(encrypted_data).decode('utf-8')
    return iv_hex, ciphertext_hex
def decrypt_des(key, iv_hex, encrypted_data_hex):
    key_bytes = key.encode('utf-8')
    iv_bytes = binascii.unhexlify(iv_hex)
    encrypted_data_bytes = binascii.unhexlify(encrypted_data_hex)
    cipher = DES.new(key_bytes, DES.MODE_CBC, iv_bytes)
    decrypted_data_padded = cipher.decrypt(encrypted_data_bytes)
    decrypted_data_unpadded = unpad(decrypted_data_padded, DES.block_size)
    return decrypted_data_unpadded.decode('utf-8')
def interactive_mode():
    print("\n" + "=" * 60)
    print("DES ALGORITHM INTERACTIVE DEMONSTRATION")
    print("NOTE: The DES Key MUST be exactly 8 characters long.")
    print("Enter 'quit' or 'exit' for the key to stop.")
    print("=" * 60)
    while True:
        try:
            key = input("\nEnter 8-character Key (e.g., ABCDEFGH): ")
            if key.lower() in ['quit', 'exit']:
                break        
            if len(key) != 8:
                print(">>> ERROR: Key must be exactly 8 characters long. Please try again.")
                continue
            data = input("Enter Plaintext Data to encrypt: ")
            if not data:
                print(">>> ERROR: Plaintext data cannot be empty. Please try again.")
                continue
            print("\n--- ENCRYPTION PROCESS ---")
            iv, encrypted_data = encrypt_des(key, data)
            print(f"Original Data:      '{data}'")
            print(f"Generated IV (Hex): {iv}")
            print(f"Ciphertext (Hex):   {encrypted_data}")
            print("\n--- DECRYPTION PROCESS ---")
            decrypted_data = decrypt_des(key, iv, encrypted_data)
            print(f"Decrypted Data:     '{decrypted_data}'")
            if decrypted_data == data:
                print("\nSTATUS: SUCCESS! Encryption and decryption matched.")
            else:
                print("\nSTATUS: FAILURE! Data mismatch.")            
        except ValueError as e:
            print(f"\n>>> ERROR: A value error occurred, usually due to invalid key or padding: {e}")
        except Exception as e:
            print(f"\n>>> CRITICAL ERROR: An unexpected error occurred: {e}")           
    print("\nDemonstration finished. Goodbye!")
if __name__ == "__main__":
    interactive_mode()
