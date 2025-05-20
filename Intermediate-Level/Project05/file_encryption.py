# 🔐 File Encryption Tool using Caesar Cipher
# Pure Python – No external libraries

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26
            result += chr(base + shifted)
        else:
            result += char  # Leave punctuation/spaces unchanged
    return result

def process_file(filename, shift, mode):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        processed = caesar_cipher(content, shift, mode)

        output_filename = f"{mode}ed_{filename}"
        with open(output_filename, 'w', encoding='utf-8') as output:
            output.write(processed)

        print(f"✅ Done! Your file is saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ File not found. Make sure the filename is correct.")
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

def main():
    print("🔐 Caesar Cipher File Encryption Tool")
    while True:
        mode = input("Enter mode (encrypt/decrypt): ").lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'.")
            continue
        break

    filename = input("Enter filename to process (e.g., secret.txt): ").strip()

    try:
        shift = int(input("Enter shift amount (e.g., 3): "))
    except ValueError:
        print("Shift must be a number.")
        return

    process_file(filename, shift, mode)

if __name__ == "__main__":
    main()
