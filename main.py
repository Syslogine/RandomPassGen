import secrets
import string
import pyperclip

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True, custom_characters=''):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    characters += custom_characters

    if not characters:
        print("Error: No character types selected. Please include at least one character type.")
        return None

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_choices():
    print("Welcome to the Random Password Generator!")
    print("Password security tip: Longer passwords are generally more secure.")
    print("Consider using a length of at least 16 characters.")
    use_lowercase = input("Include lowercase letters? (y/n, default: y): ").lower() in {'y', ''}
    use_uppercase = input("Include uppercase letters? (y/n, default: y): ").lower() in {'y', ''}
    use_digits = input("Include digits? (y/n, default: y): ").lower() in {'y', ''}
    use_punctuation = input("Include punctuation? (y/n, default: y): ").lower() in {'y', ''}
    custom_characters = input("Enter any additional characters to include: ")

    return use_lowercase, use_uppercase, use_digits, use_punctuation, custom_characters

if __name__ == "__main__":
    use_lowercase, use_uppercase, use_digits, use_punctuation, custom_characters = get_user_choices()

    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            if password_length > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    generated_password = generate_password(
        length=password_length,
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_punctuation=use_punctuation,
        custom_characters=custom_characters
    )

    if generated_password is not None:
        print("Generated Password:", generated_password)
        try:
            pyperclip.copy(generated_password)
            print("Password copied to clipboard.")
        except pyperclip.PyperclipException:
            print("Warning: Unable to copy to clipboard.")
