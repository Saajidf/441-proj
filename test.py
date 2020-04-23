import gmpy2

n = 3233
e = 17
d = 413


# Encrypting and decrypting functions
def encrypt_this(m):
    result = gmpy2.powmod(m, e, n)
    return result


def decrypt_this(c):
    plain = gmpy2.powmod(c, d, n)
    return plain


def main():
    M = 'user input'

    x = 0
    for c in M:
        x = x << 8
        x = x ^ ord(c)

    print("x = ", int(x))
    # Encrypt
    enc = encrypt_this(x)
    print("Encypted number: ", enc)
    # Decrypt
    dec = decrypt_this(enc)
    print("Decrypted plain number: ", dec)



if __name__ == "__main__":
    main()
