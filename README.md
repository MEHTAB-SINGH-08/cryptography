# Classical Cryptography & Cryptanalysis in Python

A collection of from-scratch Python implementations exploring foundational symmetric encryption algorithms and statistical cryptanalysis techniques. Built to demonstrate how classical ciphers operate—and how mathematical and frequency-based attacks break them.

---

## Implemented Modules

### 1. Caesar Cipher
* **Encryption & Decryption:** Modular shift-cipher implementation supporting configurable shift keys.
* **Brute-Force Cryptanalysis:** Automated key-space exhaustion across all 26 shifts to recover plaintext without prior key knowledge.

### 2. Vigenère Cipher
* **Encryption & Decryption:** Polyalphabetic substitution using repeating keyword schedules.
* **Kasiski Examination:** Automated detection of repeated ciphertext sequences and greatest common divisor (GCD) spacing analysis to estimate keyword length.
* **Automated Index of Coincidence (IoC):** Statistical letter-frequency distribution analysis to determine probable key lengths and break polyalphabetic encryption.

---

## Tech Stack & Tools
* **Language:** Python 3.x (Standard Library: `math`, `collections`, `string`)
* **Focus Areas:** Classical Cryptography, Statistical Cryptanalysis, Modular Arithmetic

---

## Roadmap & Future Additions
* [ ] Modern Symmetric & Asymmetric Primitives (AES, RSA, Diffie-Hellman)
* [ ] Lattice-Based Post-Quantum Encryption Prototype (Ring-LWE)

---

