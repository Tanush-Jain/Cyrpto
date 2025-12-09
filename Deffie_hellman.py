def power(base, expo, mod):
    result = 1
    base %= mod
    while expo > 0:
        if expo % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        expo //= 2
    return result
def main():
    print("Diffie-Helm an Key Exchange Simulation   ")
    try:
        p = int(input("Enter a prime number (p): "))
        g = int(input("Enter a primitive root modulo p (g): "))
        a = int(input("Enter private key for User A (a): "))
        b = int(input("Enter private key for User B (b): "))
        x= power(g, a, p)
        y= power(g, b, p)
        print(f"\Alice sends : {x}")
        print(f"Bob sends : {y}")
        K1 = power(y, a, p)
        K2 = power(x, b, p)
        print(f"\nUser A's Computed Shared Secret Key: {K1}")
        print(f"User B's Computed Shared Secret Key: {K2}")
        if K1 == K2:
            print("SUCCESS: Both users have derived the same shared secret key.")
        else:
            print("FAILURE: The derived keys do not match.")
    except ValueError:
        print("Error: Please enter valid integers for p, g, a, and b.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()  