def has_required_characters(password):
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if not char.isalnum())
    
    return (uppercase_count >= 2) and (lowercase_count >= 2) and (digit_count >= 2) and (special_count >= 2)

def has_repeating_characters(password):
    for i in range(len(password) - 3):
        if password[i] == password[i + 1] == password[i + 2] == password[i + 3]:
            return True
    return False

def has_sequence_from_username(password, username):
    for i in range(len(username) - 2):
        if username[i:i + 3] in password:
            return True
    return False

def validate_password(password, username, last_three_passwords):
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."
    
    if not has_required_characters(password):
        return False, "Password must contain at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 special characters."
    
    if has_repeating_characters(password):
        return False, "No character should repeat more than three times in a row."
    
    if has_sequence_from_username(password, username):
        return False, "Password should not contain sequences of three or more consecutive characters from the username."
    
    if password in last_three_passwords:
        return False, "Password cannot be the same as any of the last three passwords."
    
    return True, "Password is valid."

def main():
    username = input("Enter your username: ")
    
    last_three_passwords = []
    for i in range(3):
        last_three_passwords.append(input("Enter your last password used: "))
    
    while True:
        password = input("Enter your new password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password successfully set.")
            break
        else:
            print("Invalid password:", message)

if __name__ == "__main__":
    main()
