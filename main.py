import sys
import os

# Import functions from your subfolders
from password_checker.checker import check_password_strength
from password_generator.generator import generate_strong_password
from file_integrity_checker.integrity import get_file_hash
from brute_force_demo.brute_force import dictionary_attack

def clear_screen():
    # Clears the terminal screen for a cleaner look
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("="*30)
        print("   CYBER SECURITY TOOLKIT   ")
        print("="*30)
        print("1. Password Strength Checker")
        print("2. Password Generator")
        print("3. File Integrity Checker (SHA-256)")
        print("4. Brute Force Demo (Dictionary Attack)")
        print("5. Exit")
        print("-"*30)
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            pwd = input("\nEnter password to evaluate: ")
            remark, score = check_password_strength(pwd)
            print(f"\n[!] Strength: {remark}")
            print(f"[!] Score: {score}/5")
            if score < 4:
                print("[-] Suggestion: Use symbols, numbers, and more than 12 characters.")
            input("\nPress Enter to return to menu...")

        elif choice == '2':
            try:
                length = input("\nEnter length (default 16): ")
                length = int(length) if length else 16
                new_pwd = generate_strong_password(length)
                print(f"\n[+] Generated Password: {new_pwd}")
            except ValueError:
                print("\n[!] Error: Please enter a valid number.")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            path = input("\nEnter the full path of the file: ")
            file_hash = get_file_hash(path)
            if file_hash:
                print(f"\n[+] SHA-256 Hash: {file_hash}")
            else:
                print("\n[!] Error: File not found. Check the path.")
            input("\nPress Enter to return to menu...")

        elif choice == '4':
            pwd = input("\nEnter a common password to test: ")
            result = dictionary_attack(pwd)
            print(f"\n{result}")
            input("\nPress Enter to return to menu...")

        elif choice == '5':
            print("\nExiting... Stay secure!")
            sys.exit()

        else:
            print("\n[!] Invalid selection. Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()