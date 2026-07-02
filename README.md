# Synent Task 4: Secure Password Generator 🔒

A lightweight, robust command-line interface (CLI) tool built in Python to generate high-entropy, random passwords. Developed as part of the Synent internship/technical track (Task 4).

This tool leverages Python's `secrets` module for cryptographically secure pseudo-random number generation (CSPRNG), ensuring passwords are safe from predictability vectors common in standard pseudo-random generators.

## ✨ Features
* **Cryptographic Security:** Built using the `secrets` module to ensure high-entropy randomness suitable for security credentials.
* **Guaranteed Complexity:** Enforces the strict inclusion of at least one lowercase letter, one uppercase letter, one digit, and one special character (`string.punctuation`).
* **Robust Input Sanitization:** Safely constrains user input between 9 and 19 characters with comprehensive `ValueError` and `TypeError` protection.
* **Pattern Elimination:** Shuffles the generated array before joining to remove any predictability regarding character placement.

## 🚀 Getting Started

### Prerequisites
* Python 3.6 or higher.

