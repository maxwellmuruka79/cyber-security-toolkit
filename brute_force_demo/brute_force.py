def dictionary_attack(target_password):
    # A list of the most common passwords used globally
    common_passwords = [
        "123456", "password", "12345678", "qwerty", 
        "admin", "welcome", "password123", "12345"
    ]
    
    print(f"[*] Scanning dictionary for: {target_password}")
    
    if target_password in common_passwords:
        return f"[!] CRACKED! '{target_password}' is a common password found in our dictionary."
    else:
        return "[+] SUCCESS: Password not found in the common dictionary."

if __name__ == "__main__":
    test_pwd = input("Enter a password to test: ")
    print(dictionary_attack(test_pwd))
