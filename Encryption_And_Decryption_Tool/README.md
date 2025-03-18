Title: Simple Text Encryption/Decryption Tool with Tkinter

Description:

This Python script provides a basic text encryption and decryption tool using the Tkinter library for the graphical user interface and the 

base64 encoding method. Users can enter text, provide a secret key (password), and then encrypt or decrypt the text. The tool displays the processed text in a separate window.

Key Features:

    Encryption and Decryption: Encrypts and decrypts text using base64 encoding.
    Secret Key Protection: Requires a secret key ("1234") for both encryption and decryption.
    User-Friendly Interface: Uses Tkinter to create a simple and intuitive GUI.
    Error Handling: Includes error messages for invalid secret keys and empty text fields.
    Clear Output: Displays the processed text in a separate, read-only window.
    Reset Functionality: Provides a reset button to clear input fields.
    Icon Support: Attempts to load a custom icon ("encryption.png") for the application window.

Usage:

    Clone or download the repository.
    Ensure you have Python installed.
    Run the main.py script (or whatever you named the python file).
    Enter the text you want to encrypt or decrypt in the top text field.
    Enter the secret key ("1234") in the password field.
    Click "ENCRYPT" or "DECRYPT" to process the text.
    The processed text will be displayed in a new window.
    Use the "RESET" button to clear the fields.

Dependencies:

    Python standard library (Tkinter, base64)

Note:

    This tool uses base64 encoding, which is a simple encoding scheme. For stronger encryption, consider using more robust encryption libraries like cryptography.
    The secret key is hardcoded ("1234") for simplicity. In a real-world application, store and manage keys securely.
    The icon "encryption.png" is optional. If not found, a warning will be printed to the console, and the default Tkinter icon will be used.
