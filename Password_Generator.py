import random
import string

def generate_password(length):
    """
    Function to generate a random password of given length.
    
    Parameters:
    length (int): The length of the password to be generated.
    
    Returns:
    str: The randomly generated password.
    """
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(characters)
    return password

# Prompt the user to enter the length of the password
length = int(input("Enter the length of the password: "))

# Generate the password
password = generate_password(length)

# Print the generated password
print("Generated Password:", password)
