def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice!")
        
        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()

