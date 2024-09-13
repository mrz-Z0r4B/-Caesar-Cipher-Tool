def caesar_cipher_encrypt(plain_text, shift):
    # Define the characters to be included in the Caesar Cipher (letters, digits, special characters)
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    encrypted_text = ""
    
    for char in plain_text:
        if char in characters:
            index = characters.find(char)
            new_index = (index + shift) % len(characters)
            encrypted_text += characters[new_index]
        else:
            encrypted_text += char  # Characters not in the defined set remain unchanged

    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    # Define the characters to be included in the Caesar Cipher (letters, digits, special characters)
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    decrypted_text = ""
    
    for char in encrypted_text:
        if char in characters:
            index = characters.find(char)
            new_index = (index - shift) % len(characters)
            decrypted_text += characters[new_index]
        else:
            decrypted_text += char  # Characters not in the defined set remain unchanged

    return decrypted_text

def main():
    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color

    # Display the title and introduction
    print(f"{RED}={'='*40}{RESET}")
    print(f"{RED}{' '*10}Caesar Cipher Tool{RESET}")
    print(f"{RED}={'='*40}{RESET}")
    print("Welcome to the Caesar Cipher Tool!")
    print("You can use this tool to encrypt or decrypt text using a Caesar Cipher.")
    
    # Display the options with colors
    print(f"\n{CYAN}Would you like to: {RESET}")
    print(f"{GREEN}1. Encrypt text{RESET}")  # Green color for encryption
    print(f"{YELLOW}2. Decrypt text{RESET}")  # Yellow color for decryption

    # Prompt with colored choices
    prompt = f"{CYAN}Please enter {GREEN}1{RESET} {CYAN}or {YELLOW}2{RESET}: {RESET}"
    question_choice = input(prompt)

    if question_choice == '1':
        text = input("\nEnter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher_encrypt(text, shift)
        print(f"\n{GREEN}Encrypted text:{RESET} {result}")
    elif question_choice == '2':
        text = input("\nEnter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher_decrypt(text, shift)
        print(f"\n{BLUE}Decrypted text:{RESET} {result}")
    else:
        print("\nInvalid choice. Please enter 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    main()
