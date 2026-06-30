"""
Collect user preference for password length(min. 9 chars ,max 19 chars)
Should contain both uppercase & lowercase
Should have special characters
Should have numbers
"""

# Get all characters (atleast 9)
# ensure at least one of each type is included

import secrets
import string


def get_input() -> int:
    length: int = 0
    while True:
        try:
            length = int(input("Input Length of the password(9 - 19): ").strip())
            if length < 9 or length > 19:
                print("length should be between 9 and 19 characters")
                continue
            else:
                break

        except ValueError or TypeError:
            print("Invalid input. Please enter a valid integer.")
            continue

    return length


def generate_password(length: int) -> str:
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation  # e.g., !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # initialize password with at least one of each type
    password = [
        secrets.choice(letters_lower),
        secrets.choice(letters_upper),
        secrets.choice(digits),
        secrets.choice(special),
        # Using secrets.choice to ensure secure randomness
    ]

    # fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(
            secrets.choice(letters_lower + letters_upper + digits + special)
        )

    # shuffle the password to ensure randomness
    secrets.SystemRandom().shuffle(password)

    # return the generated password as a string
    # .join converts the list of characters into a single string automatically
    return "".join(password)


def download_password(filetodownload: str) -> None:
    response = input("Do you want to save this password? (y/n)")

    responses = ["y", "yes", "hell yea gng", "ye", "yes"]

    if response.lower() in responses:
        with open("password.txt", "w") as file:
            file.write(filetodownload + "\n")
            print("Password saved to password.txt")
    else:
        print("Password not saved, Thanks for using!")


def main():
    passlen: int = get_input()
    finalpassword: str = generate_password(passlen)
    print(f"\n{finalpassword}\n")
    download_password(finalpassword)


if __name__ == "__main__":
    main()
