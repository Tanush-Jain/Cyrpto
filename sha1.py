import hashlib
def calculate_sha1_step_by_step():
    print("--- SHA-1 Message Digest Calculator ---\n")
    input_string = input("Enter the text to hash: ")
    if not input_string:
        print("Error: Input cannot be empty.")
        return
    input_bytes = input_string.encode('utf-8')
    print(f"\n[Step 1] Input converted to bytes (hex representation):")
    print(f"Result: {input_bytes.hex()}")
    hash_object = hashlib.sha1()
    print(f"\n[Step 2] SHA-1 Hash object initialized.")
    hash_object.update(input_bytes)
    print(f"[Step 3] Hash object updated with input data.")
    final_hash = hash_object.hexdigest()
    print("-" * 40)
    print(f"FINAL SHA-1 MESSAGE DIGEST: {final_hash}")
    print("-" * 40)
if __name__ == "__main__":
    calculate_sha1_step_by_step()