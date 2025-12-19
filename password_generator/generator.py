import secrets
import string

def generate_strong_password(length=16):
    # Combines letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # 'secrets' is more secure than 'random' for passwords
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print(f"Generated Password: {generate_strong_password()}")
