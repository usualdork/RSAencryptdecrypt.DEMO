import random

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def encrypt(public_key, plaintext):
    n, e = public_key
    encrypted = [pow(ord(char), e, n) for char in plaintext]
    return encrypted

def decrypt(private_key, encrypted):
    n, d = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)

if __name__ == '__main__':
    print("RSA Encryption and Decryption Demo")
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    
    message = input("Enter the message to be encrypted: ")
    print("Original Message:", message)
    
    encrypted_message = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_message)
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
