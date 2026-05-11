def dictionary_attack(target_password):

    common_passwords = [
        "123456",
        "password",
        "12345678",
        "qwerty",
        "admin",
        "welcome",
        "password123",
        "12345"
    ]

    print(f"[*] Checking password strength against dictionary...")

    target_password = target_password.lower()

    for password in common_passwords:

        if target_password == password:
            return f"[!] Weak Password Detected: '{password}' found in dictionary."

    return "[+] Password not found in dictionary."
