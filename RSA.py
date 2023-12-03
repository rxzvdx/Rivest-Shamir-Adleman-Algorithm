import random

# This code is an implementation of the RSA (Rivest–Shamir–Adleman) encryption algorithm,
#  which is a widely used public-key cryptosystem for securing communication over the internet. 
# RSA involves the use of two keys, a public key for encryption and a private key for decryption.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number():
    # Generate a random prime number
    while True:
        num = random.randint(2**15, 2**16)  # Adjust the range as needed
        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_coprime(totient):
    # Generate a random number less than totient and coprime with totient
    while True:
        e = random.randint(2, totient - 1)
        if gcd(e, totient) == 1:
            return e

def generate_keypair():
    # Step 1: Choose two large prime numbers
    p = generate_prime_number()
    q = generate_prime_number()

    # Step 2: Compute n (modulus)
    n = p * q

    # Step 3: Compute totient (Euler's totient function)
    totient = (p - 1) * (q - 1)

    # Step 4: Choose public exponent e (should be coprime with totient)
    e = generate_coprime(totient)

    # Step 5: Compute private exponent d (modular multiplicative inverse of e mod totient)
    d = modinv(e, totient)

    return ((n, e), (n, d))

def modinv(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Rest of the code remains the same...


def encrypt(message, public_key):
    n, e = public_key
    # Convert the message to numerical representation
    numeric_message = [ord(char) for char in message]

    # Encrypt each character using the public key
    encrypted_message = [pow(char, e, n) for char in numeric_message]

    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    # Decrypt each character using the private key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]

    # Convert numerical representation back to string
    decrypted_string = ''.join(decrypted_message)

    return decrypted_string

# Generate key pair
public_key, private_key = generate_keypair()

# Define a message
message = "Hello, RSA!"

# Encrypt the message
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
