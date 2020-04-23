# message: I deserve a 100

import sys
import random
import os

msg = b'I deserve a 100'

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# Returns modulo inverse of a with respect to m using extended Euclid
# a and m are coprimes
def modInverse(a, m):
    m1 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # turn x positive
    if x < 0:
        x = x + m1

    return x


# This function is called k times
# false if n is composite
# false if n is probably prime.
def millTest(d, n):
    # Pick a random number in 2 to n-2
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n using python built in modular exponentiation
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    # Square x while
    # d does not reach n-1
    # (x^2) % n is not 1
    # (x^2) % n is not n-1
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    # Return composite
    return False


# false if n is composite and true if n is prime. k is number of trials
def isPrime(n, k):
    # edge cases
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    # do miller test k times
    for i in range(k):
        if not millTest(d, n):
            return False

    return True


def generateLargePrime(keysize):
    # Return a random prime number of keysize bits in size.
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num, 4):
            return num


def generateKey(keySize):
    # Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    p = generateLargePrime(keySize)
    print('Generating q prime...')
    q = generateLargePrime(keySize)
    n = p * q

    # Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = modInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return publicKey, privateKey


def makeKeyFiles(keySize):
    publicKey, privateKey = generateKey(keySize)

    # write to file with keysize, then n, then d
    myfile = open('private_key.txt', 'w')
    myfile.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    myfile.close()

    # write to file with keysize, then n, then e
    myfile = open('public_key.txt', 'w')
    myfile.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    myfile.close()

    x = 0
    for c in msg:
        x = x << 8
        x = x ^ ord(c)





if __name__ == "__main__":
    makeKeyFiles(int(sys.argv[1]))