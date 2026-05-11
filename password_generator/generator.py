import secrets
import string

def generate_strong_password(length=16):

    if length < 4:
        return "Length must be at least 4"

    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    symbol = secrets.choice(string.punctuation)

    remaining = ''.join(
        secrets.choice(
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        for _ in range(length - 4)
    )

    password_list = list(lowercase + uppercase + digit + symbol + remaining)

    secrets.SystemRandom().shuffle(password_list)

    return ''.join(password_list)

print(generate_strong_password())
