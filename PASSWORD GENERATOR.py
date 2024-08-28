import random
import string

def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
