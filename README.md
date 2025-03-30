# Password Strength Checker

## Overview

This project is a Python script that evaluates the strength of a given password. It analyzes the password based on various criteria such as length, character diversity (uppercase, lowercase, digits, special characters), and patterns like repeated characters. Depending on the strength, the script either offers to save a strong password or suggests a new, stronger one.

## Features

- **Password Strength Evaluation:**
  - **Length Checks:** Tiered scoring based on password length.
  - **Character Diversity:** Verifies the presence of uppercase letters, lowercase letters, digits, and special characters.
  - **Pattern Detection:** Penalizes passwords with three or more consecutive repeated characters.
  - **Common Password Detection:** Immediately flags commonly used weak passwords.
  
- **Strong Password Handling:**
  - If a password is deemed "Strong," the user is prompted to save it to a file.

- **Password Suggestion:**
  - For "Weak" or "Medium" passwords, the user can opt to generate a strong password suggestion.
  - Offers an option to save the newly generated strong password.

## Usage

1. **Download or Clone the Repository:**
   - Save the Python script file to your local machine.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Run the script using Python 3:
     ```bash
     python your_script_name.py
     ```
   - Replace `your_script_name.py` with the actual file name.

3. **Follow the Prompts:**
   - **Password Input:** Enter the password you wish to evaluate.
   - **Strength Feedback:** The script will display the password strength (Weak, Medium, or Strong).
   - **Actions Based on Strength:**
     - **Strong Password:** You will be asked if you want to save it.
     - **Weak/Medium Password:** You will be prompted whether to generate a new strong password suggestion. If accepted, you'll see the suggested password and be asked if you want to save it.

## Customization

- **Common Passwords:**
  - Modify the `COMMON_PASSWORDS` set in the script to add more commonly used weak passwords.

- **Password Generation:**
  - Adjust the `generate_strong_password` function to change the default password length or character set as needed.

- **File Handling:**
  - The strong passwords are saved in `saved_passwords.txt`. Feel free to change the file name or path based on your requirements.

## License

This project is open source. You are free to use, modify, and distribute it as needed.

## Contributing

Contributions are welcome! If you have ideas or improvements, please submit a pull request or open an issue.
