import re
import random
import string

# A small list of common passwords. You can expand this list.
COMMON_PASSWORDS = {"password", "123456", "123456789", "qwerty", "abc123", "111111"}

def password_strength(password):
    # Immediately flag common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak"
    
    score = 0
    length = len(password)
    
    # Tiered length scoring: more points for longer passwords.
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
        
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        
    # Check for digits
    if re.search(r"\d", password):
        score += 1
        
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        
    # Deduct points for three or more consecutive repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 1
        
    # Determine strength level based on the total score
    if score < 3:
        return "Weak"
    elif score < 6:
        return "Medium"
    else:
        return "Strong"

def save_strong_password(password):
    """Prompt the user to save a strong password to a text file."""
    choice = input("Your password is strong. Do you want to save this password to a file? (Yes/No): ")
    if choice.lower() == "yes":
        try:
            with open("saved_passwords.txt", "a") as file:
                file.write(password + "\n")
            print("Password saved to 'saved_passwords.txt'.")
        except Exception as e:
            print("An error occurred while saving the password:", e)
    else:
        print("Exiting without saving the password.")

def generate_strong_password(length=16):
    """
    Generate a strong random password that includes at least one uppercase letter,
    one lowercase letter, one digit, and one special character.
    """
    if length < 8:
        length = 8  # Enforce a minimum length
    
    # Ensure inclusion of at least one character from each category.
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*(),.?\":{}|<>")
    
    # Fill remaining characters from a pool of all characters.
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    remaining = ''.join(random.choices(all_chars, k=remaining_length))
    
    # Combine and shuffle to ensure randomness.
    password_list = list(upper + lower + digit + special + remaining)
    random.shuffle(password_list)
    return ''.join(password_list)

def suggest_new_password():
    """Offer to generate and optionally save a new strong password suggestion."""
    choice = input("Your password is weak/medium. Would you like to generate a strong password suggestion? (Yes/No): ")
    if choice.lower() == "yes":
        new_password = generate_strong_password()
        print("Here is your new strong password suggestion:", new_password)
        # Ask if the user wants to save the suggested password.
        save_choice = input("Do you want to save this suggested password? (Yes/No): ")
        if save_choice.lower() == "yes":
            try:
                with open("saved_passwords.txt", "a") as file:
                    file.write(new_password + "\n")
                print("Suggested password saved to 'saved_passwords.txt'.")
            except Exception as e:
                print("An error occurred while saving the password:", e)
        else:
            print("Exiting without saving the suggested password.")
    else:
        print("No suggestion will be generated. Exiting.")

def main():
    user_password = input("Enter your password: ")
    strength = password_strength(user_password)
    print(f"Your password strength is: {strength}")
    
    if strength == "Strong":
        save_strong_password(user_password)
    else:
        suggest_new_password()

if __name__ == "__main__":
    main()
# This script checks the strength of a password, suggests improvements, and allows saving strong passwords.
# It also generates strong passwords if the user opts for it.