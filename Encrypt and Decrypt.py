def create_substitution_dict():
    original = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/'
    shifted = 'mnopqrstuvwxyzabcdefghijklABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/'
    return {original[i]: shifted[i] for i in range(len(original))}

def create_reverse_substitution_dict():
    original = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/'
    shifted = 'mnopqrstuvwxyzabcdefghijklABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/'
    return {shifted[i]: original[i] for i in range(len(original))}

def encrypt_message(message, substitution_dict):
    return ''.join(substitution_dict.get(char, char) for char in message)

def decrypt_message(message, reverse_substitution_dict):
    return ''.join(reverse_substitution_dict.get(char, char) for char in message)

def main():
    substitution_dict = create_substitution_dict()
    reverse_substitution_dict = create_reverse_substitution_dict()

    operation = input("Enter 'e' for encryption or 'd' for decryption: ").strip().lower()
    message = input("Enter the message: ")

    if operation == 'e':
        result = encrypt_message(message, substitution_dict)
        print("Encrypted message:", result)
    elif operation == 'd':
        result = decrypt_message(message, reverse_substitution_dict)
        print("Decrypted message:", result)
    else:
        print("Invalid option. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
