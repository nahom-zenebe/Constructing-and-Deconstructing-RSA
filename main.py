import random
from math import gcd



def mod_inverse(e, phi):
    """
    Extended Euclidean Algorithm
    Returns d such that (d * e) % phi == 1
    """
    old_r, r = e, phi
    old_s, s = 1, 0

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    return old_s % phi



# Step 1: RSA Key Generation (Using Euler's Totient ONLY)

print("=" * 60)
print("RSA KEY GENERATION (Euler Totient φ only)")
print("=" * 60)

# Small primes (required for classical simulation)
p = 61
q = 53

N = p * q 

# Euler's Totient function
phi = (p - 1) * (q - 1)

# Public exponent
e = 17

# Ensure e is valid (coprime with phi)
if gcd(e, phi) != 1:
    raise ValueError("e must be coprime with φ(N). Choose another e.")

# Private exponent
d = mod_inverse(e, phi)

print(f"Prime p          = {p}")
print(f"Prime q          = {q}")
print(f"Modulus N        = {N}")
print(f"Euler Totient φ  = {phi}")
print(f"Public exponent e= {e}")
print(f"Private exponent d= {d}")


# Step 2: Encryption


print("\n" + "=" * 60)
print("RSA ENCRYPTION")
print("=" * 60)

message = 65  # small integer message

ciphertext = pow(message, e, N)

print("Original Message :", message)
print("Ciphertext       :", ciphertext)



# Step 3: Decryption


print("\n" + "=" * 60)
print("RSA DECRYPTION")
print("=" * 60)

decrypted = pow(ciphertext, d, N)

print("Recovered Message:", decrypted)



# Step 4: Classical Period Finding Attack


print("\n" + "=" * 60)
print("CLASSICAL PERIOD FINDING ATTACK")
print("=" * 60)

# Choose random a coprime with N
while True:
    a = random.randint(2, N - 2)
    if gcd(a, N) == 1:
        break

print("Chosen a =", a)

r = 1

# Find period r such that a^r ≡ 1 (mod N)
while pow(a, r, N) != 1:
    r += 1

print("Period r =", r)



# Step 5: Factor Recovery


print("\n" + "=" * 60)
print("RECOVERING PRIME FACTORS")
print("=" * 60)

if r % 2 != 0:
    print("Attack failed: period is odd.")
else:
    x = pow(a, r // 2, N)

    if x == N - 1:
        print("Attack failed: trivial root (-1 mod N).")
    else:
        factor1 = gcd(x - 1, N)
        factor2 = gcd(x + 1, N)

        print("gcd(a^(r/2) - 1, N) =", factor1)
        print("gcd(a^(r/2) + 1, N) =", factor2)

        if factor1 * factor2 == N:
            print("\nSuccessfully recovered factors!")
            print("Recovered p =", factor1)
            print("Recovered q =", factor2)
        else:
            print("\nAttack unsuccessful.")