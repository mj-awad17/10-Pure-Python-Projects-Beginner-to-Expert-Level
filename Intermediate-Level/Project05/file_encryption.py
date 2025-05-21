import os

# Caesar Cipher Implementation

# This script implements a simple Caesar cipher encryption and decryption.
"""
Steps to implement the case_cipher function:
1. Define the function with parameters for text, shift, and mode (encrypt/decrypt).
2. Initialize an empty string to store the result.
3. Reverse the shift for decryption.
4. Loop through each character in the text.
5. Check if the character is an uppercase letter.
6. Determine the base (A or a) and perform the shift.
7. Apply the shift and wrap around using modulo.
8. Append the shifted character to the result string.
9. If the character is not an alphabetic character, keep it unchanged.
10. Return the result string.
"""
def case_cipher(text, shift, mode='encrypt'):
    result = ""
    # reverse the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # loop through each character in the text
    for char in text:
        if char.isalpha():
            # determine the base (a/A) and perform the shift
            base = ord('A') if char.isupper() else ord('a')
            # apply shift and wrap around using (26 letters in alphates) modulo
            shifted = chr((ord(char)-base + shift) % 26 + base)
            result += shifted
        else:
            # if not an alphabetic character, keep it unchanged
            result += char
    
    return result

# This function takes a string and a shift value, and returns the encrypted/decrypted string.
"""
Steps to implement the process_file function:
1. Open the file in read mode.
2. Read the contents of the file.
3. Process the content using the case_cipher function.
4. Create the output file directory if it doesn't exist.
5. Write the processed content to the output file.
6. Handle any exceptions that may occur during file operations.
7. Return a success message or an error message.
"""
def process_file(input_file, output_file, shift):
    try:
        # Open the input file in read mode
        with open(input_file, 'r', endcoding='utf-8') as file:
            # read the contents of the file
            content = file.read()
        
        # process the content using the case_cipher function
        processed_content = case_cipher(content, shift, mode='encrypt')

        # Create the output file directory if it doesn't exist
        os.path.dirname('output', exits_ok=True)
        
        # write to the output file
        output_path = os.path.join('output', output_file)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        
        return True, output_path

    # Handle file not found error
    except FileNotFoundError:
        return False, f"❌ Error: File {input_file} not found."
    except Exception as e:
        return False, f"⚠ Error: {str(e)}"

# This is the main function that will call the case_cipher and process_file functions.
# It will also handle user input and output too.
def main():
    pass

if __name__ == "__main__":
    main()