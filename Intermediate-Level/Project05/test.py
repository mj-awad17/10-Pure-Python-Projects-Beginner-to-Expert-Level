# basic file operation
# f = open('secret.txt', 'r')
# print(f.read())

# f = open(input("Enter filename to process (e.g., secret.txt): "), 'r')
# print(f.read())


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

    process_file(filename, mode, shift)

def caesar_cipher(text, mode, shift):
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'.")
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

def process_file(filename, mode, shift):
    print("🔐 File Processing working")

    try:
        # Check if the file exists
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Simulate file processing
        print(f"File content: {content}")
        processed = caesar_cipher(content, mode, shift)
        print(f"File is {mode}ed as:: {processed}")

        # save in the specific folder
        output_folder = f"Intermediate-Level/Project05/output/"
        output_filename = f"{output_folder}/{mode}ed_{filename}.txt"

        # create new empty file
        new_filename = input("Enter new filename (without extension): ").strip()
        with open(f"{new_filename}.txt", 'x', encoding='utf-8') as output:
            output.write(processed)

        if not new_filename:
            print("No new filename provided. Using default.")
            new_filename = filename.split('.')[0]

        # Create the output folder if it doesn't exist
        with open(f"{output_folder}/{new_filename}.txt", 'w', encoding='utf-8') as output:
            output.write(processed)
        print(f"✅ Done! Your file is saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ File not found. Make sure the filename is correct.")
        return
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")
        return
    
    # print(f"File content: {content}")

if __name__ == "__main__":
    main()