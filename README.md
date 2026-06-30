# RSA Encryption and Classical Period-Finding Attack

## Overview

This project demonstrates the complete lifecycle of the RSA cryptosystem and a simplified classical simulation of the mathematical idea behind Shor's quantum factoring algorithm.

The program performs four major tasks:

1. Generates RSA public and private keys.
2. Encrypts a plaintext integer.
3. Decrypts the ciphertext.
4. Performs a classical brute-force period-finding attack to recover the original prime factors.


---

# Project Objectives

The program demonstrates:

- RSA Key Generation
- RSA Encryption
- RSA Decryption
- Classical Period Finding
- Prime Factor Recovery using GCD

---

# Mathematical Background

## Step 1 — Choose Two Prime Numbers

The algorithm begins with two small prime numbers.

Example:

```
p = 61
q = 53
```

---

## Step 2 — Compute the RSA Modulus

The modulus is

```
N = p × q
```

Example

```
N = 61 × 53 = 3233
```

The modulus becomes part of both the public and private keys.

---

## Step 3 — Compute Euler's Totient

Using Euler's Totient:

```
φ(N) = (p − 1)(q − 1)
```

Example

```
φ(N) = 60 × 52 = 3120
```

The totient is used for generating the private key.

---

## Step 4 — Choose the Public Exponent

Choose an integer

```
e
```

such that

```
gcd(e, φ(N)) = 1
```

Example

```
e = 17
```

Since

```
gcd(17,3120)=1
```

it is a valid public exponent.

---

## Step 5 — Compute the Private Exponent

The private exponent satisfies

```
d × e ≡ 1 (mod φ(N))
```

The program computes

```
d
```

using the Extended Euclidean Algorithm.

Example

```
d = 2753
```

---

# RSA Keys

Public Key

```
(e, N)
```

Example

```
(17, 3233)
```

Private Key

```
(d, N)
```

Example

```
(2753, 3233)
```

---

# Encryption

Given a message

```
M
```

Encryption is performed using

```
C = M^e mod N
```

Example

```
Message = 65

Ciphertext = 65^17 mod 3233

Ciphertext = 2790
```

---

# Decryption

Recover the original message using

```
M = C^d mod N
```

Example

```
2790^2753 mod 3233

Message = 65
```

The decrypted message matches the original plaintext.

---

# Classical Period-Finding Attack

## Purpose

Instead of knowing the prime factors directly, the attacker only knows

```
N
```

The goal is to recover

```
p
```

and

```
q
```

---

## Step 1 — Choose a Random Integer

Choose a random number

```
a
```

such that

```
gcd(a,N)=1
```

This ensures

```
a
```

is coprime with

```
N
```

---

## Step 2 — Find the Period

The program repeatedly computes

```
a^r mod N
```

starting with

```
r = 1
```

until

```
a^r mod N = 1
```

The smallest such value is called the **period**.

Example

```
a = 2

2¹ mod N
2² mod N
2³ mod N
...

Eventually

2^780 mod 3233 = 1

Therefore

r = 780
```

---

## Step 3 — Verify the Period

The attack only succeeds if

```
r
```

is even.

If

```
r
```

is odd,

the attack stops.

---

## Step 4 — Recover the Factors

Compute

```
x = a^(r/2) mod N
```

Then compute

```
gcd(x−1,N)
```

and

```
gcd(x+1,N)
```

Example

```
gcd(x−1,N)=61

gcd(x+1,N)=53
```

The original primes are successfully recovered.

---

# Program Workflow

```
Choose p and q
        │
        ▼
Compute N
        │
        ▼
Compute φ(N)
        │
        ▼
Choose e
        │
        ▼
Compute d
        │
        ▼
Encrypt Message
        │
        ▼
Decrypt Message
        │
        ▼
Choose random a
        │
        ▼
Find period r
        │
        ▼
Recover p and q using GCD
```

---

# Why Small Prime Numbers?

This project intentionally uses small prime numbers (less than 100).

Example

```
p = 61
q = 53
```

The period-finding algorithm is implemented using a brute-force loop:

```
r = 1

while a^r mod N != 1:
    r += 1
```

For small values of

```
N
```

the loop finishes quickly.

For real RSA keys (2048-bit or larger), the required period becomes astronomically large, making brute-force period finding computationally infeasible on classical computers.

This computational difficulty is the foundation of RSA security.

---

# Relationship to Shor's Algorithm

This implementation does **not** perform quantum computing.

Instead, it simulates the mathematical idea used in Shor's Algorithm.

| Classical Simulation | Quantum Shor's Algorithm |
|----------------------|--------------------------|
| Brute-force search for the period | Quantum Fourier Transform finds the period efficiently |
| Very slow | Exponentially faster |
| Educational demonstration | Practical quantum factoring algorithm |

The period-finding step is the key insight behind Shor's Algorithm.

---

# Running the Program

## Requirements

- Python 3.8+
- No external libraries are required.

---

## Run

```bash
python rsa.py
```

---

# Example Output

```
============================================================
RSA KEY GENERATION
============================================================

Prime p           = 61
Prime q           = 53
Modulus N         = 3233
Euler Totient φ   = 3120
Public exponent e = 17
Private exponent d= 2753

============================================================
RSA ENCRYPTION
============================================================

Original Message : 65
Ciphertext       : 2790

============================================================
RSA DECRYPTION
============================================================

Recovered Message: 65

============================================================
CLASSICAL PERIOD FINDING ATTACK
============================================================

Chosen a = 2
Period r = 780

============================================================
RECOVERING PRIME FACTORS
============================================================

gcd(a^(r/2)-1,N) = 61
gcd(a^(r/2)+1,N) = 53

Successfully recovered factors!

Recovered p = 61
Recovered q = 53
```

---

# Files

```
.
├── main.py
└── README.md
```

---

# Learning Outcomes

After completing this project, you should understand:

- How RSA keys are generated
- Why Euler's Totient is required
- How public and private keys are related
- How RSA encryption and decryption work
- Why factoring large integers is difficult
- The concept of period finding
- The mathematical foundation of Shor's Algorithm
- Why quantum computers pose a threat to RSA

---

# Disclaimer

This project is intended solely for educational purposes to demonstrate RSA cryptography and the mathematical principles underlying Shor's Algorithm. It should not be used for real-world cryptographic applications, as it relies on intentionally small prime numbers that are insecure.