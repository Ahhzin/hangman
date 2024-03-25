import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Get password length from user
    length = int(input("Enter the length of the password: "))
    
    # Generate password
    password = generate_password(length)
    
    # Output the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()