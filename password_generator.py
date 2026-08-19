import random
import string

def password_generator():
    print("=== Password Generator ===")
    
    length = int(input("Kitne digit ka password chahiye? "))
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = letters + digits + symbols
    
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    
    print("\nTumhara Strong Password hai:")
    print(password)

password_generator()