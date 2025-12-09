def power(base, expo, mod):
    result = 1
    base %= mod
    while expo > 0:
        if expo % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        expo //= 2
    return result
def gcd (a,b):
    while b:
        a, b = b, a % b
    return a
def extendeded_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extendeded_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
def mod_inverse(e, phi):
    gcd, x, y = extendeded_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi   
def generate_key(p,q,e):
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime to phi(n)")
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))
def encrypt(message,public_key):
    e, n = public_key
    return power(message,e,n)
def decrypt(ciphertext,private_key):
    d, n = private_key
    return power(ciphertext,d,n)
def main():
    print("RSA ENCRYPTION-DECRYPTION")
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public exponent e (commonly 3 or 65537): "))
    public_key, private_key = generate_key(p, q, e)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    message = int(input("Enter message as an integer (less than n): "))
    ciphertext = encrypt(message, public_key)
    print(f"Encrypted Ciphertext: {ciphertext}")
    decrypted_message = decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")
    if message == decrypted_message:
        print("SUCCESS: Decrypted message matches the original message.")
    else:
        print("FAILURE: Decrypted message does not match the original message.")
if __name__ == "__main__":
    main()

