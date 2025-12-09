import string
import random
class SimpleSubstitutionCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.key = self.generate_key()
        self.reversed_key = {v: k for k, v in self.key.items()}
    def generate_key(self):
        alphabet = list(self.alphabet)
        shuffled = alphabet[:]
        random.shuffle(shuffled)
        return dict(zip(alphabet, shuffled))
    def encrypt(self, plaintext):
        source = self.alphabet
        destination = "".join(self.key.values())
        key_map = str.maketrans(source, destination)
        return plaintext.lower().translate(key_map)
    def decrypt(self, ciphertext):
        source = "".join(self.key.values())
        destination = self.alphabet
        key_map = str.maketrans(source, destination)
        return ciphertext.lower().translate(key_map)
cipher = SimpleSubstitutionCipher()
print("Substitution Key:", cipher.key)
plaintext = input("Enter the plain text: ")
ciphertext = cipher.encrypt(plaintext)
print("\nPlaintext :", plaintext)
print("Ciphertext :", ciphertext)
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted text :", decrypted_text)