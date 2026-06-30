# Secure Password Generator 🔒

A lightweight, secure command-line tool built in Python to generate strong, random passwords. 

Unlike standard random generators, this project utilizes Python's `secrets` module to ensure true cryptographic security, guaranteeing that your passwords meet strict modern security requirements.

## ✨ Features
* **Cryptographically Secure:** Uses `secrets` instead of `random` to prevent predictability.
* **Guaranteed Variety:** Forces the inclusion of at least one lowercase letter, uppercase letter, number, and special character.
* **Smart Input Validation:** Constrains password length safely between 9 and 19 characters with robust error handling.
* **Shuffle Protection:** Thoroughly mixes character sets to eliminate predictable structural patterns.
* **Local Storage:** (Optional) Easily extensible to append generated passwords to a local file.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
   cd YOUR-REPO-NAME

