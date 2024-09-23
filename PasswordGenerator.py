import random
import string

# Function to generate password
def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ''
    
    # Add characters to pool based on user preferences
    if use_letters:
        character_pool += string.ascii_letters  # Includes both lowercase and uppercase letters
    if use_numbers:
        character_pool += string.digits  # Adds numbers (0-9)
    if use_symbols:
        character_pool += string.punctuation  # Adds symbols (e.g., @, #, $, etc.)
    
    if not character_pool:
        print("No character types selected! Cannot generate a password.")
        return None
    
    # Generate random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        # Get password length
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length should be a positive integer.")
            return
        
        # Get user preferences for character types
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        
        # Check if at least one character type is selected
        if not (use_letters or use_numbers or use_symbols):
            print("You must select at least one character type (letters, numbers, or symbols).")
            return
        
        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
