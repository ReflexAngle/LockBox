import random
import os
import json
import sys
from cryptography.fernet import Fernet


def hello():
    pass


def help_me():
    print("HELP: for what you're looking at now")
    print("NEW: to generate a new password")
    print("LIST: to see list of you passwords")
    print("CLOSE: to exit the program")


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


def load_key(file_name="secret.key"):
    return open(file_name, "rb").read()


def encrypt(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def decrypt(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()


# Generates the password with the provided strength for it
def generate(password_strength):

    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_characters = '!@#$%^&*()?/<>-{}[]|'

    all_chars = upper_case + lower_case + numbers + special_characters

    # Generate a password using a random sample of the characters
    password = ''.join(random.choice(all_chars) for _ in range(password_strength))
    return password


# the save function allows the user to save the password and have an associated username
# and the website its for
def save(username, associated_website, password_after, key):

    encrypted_password = encrypt(password_after, key)
    credentials = {
        'username': username,
        'website': associated_website,
        'password': encrypted_password.decode()  # Store as a string
    }
    # Save to a file, appending to the existing file
    with open('passwords.txt', 'a') as f:
        f.write(json.dumps(credentials) + "\n")


# supposed to print the list out for the user
def password_list(key):
    continue_on = None

    try:
        with open("passwords.txt", 'r') as f:
            for line in f.readlines():
                # each credential is a json string
                credentials = json.loads(line)

                decrypted_password = decrypt(credentials['password'].encode(), key)
                print(f"Username: {credentials['username']}, Website: {credentials['website']}, Password: {decrypted_password}")

    except FileNotFoundError:
        print("Password file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        
    continue_on = ("type Y to continue: ")
    continue_on = continue_on.upper()
    if continue_on == 'Y':
        main()

# when prompted the program will show all relevant accounts for the user
def find_password():
    pass


def enter_pass():
    enter_password = input("Enter your password: ", )
    return enter_pass

def close():
    sys.exit()


def main():

    password_strength = None
    key = None
    key_file = "secret.key"
    user_enter = None

    # Check if the key file exists, if not, generate a new key and save it.
    if not os.path.exists(key_file):
        generate_key()
    else:
        key = load_key(key_file)
        

    print("Hello welcome to my password manager \ntype help for help")

    # allows the user to input what they intend to do
    # if help a list of commands appears
    # if list then shows password list
    def choose_to():
        while True:
            doing = input()
            doing = doing.upper()
            if doing == 'HELP':
                help_me()
            elif doing == 'LIST':
                return doing
            elif doing == 'NEW':
                return doing
            elif doing == 'EXIT':
                return doing
            else:
                print('input a valid command \ntype help if you dont know the commands')

    # checks to see in if the inputted value is
    # if it's not then it will call the function again for the user to correct
    def valid_strength():
        while True:
            password_strength = input('Length: ')
            try:
                return int(password_strength)
            except ValueError:
                print("Please enter a valid integer.")

    proceed = choose_to()
    if proceed == "EXIT":
        close()
    elif proceed == "LIST":
        password_list(key)
    elif proceed == "NEW":
        password_strength = valid_strength()
        


    password_after = generate(password_strength)

    # asks if the user is pleased and to save it or not
    # if it's a yes it calls the save function
    # makes sure the user inputted a valid input
    print("Is this acquitted? ", password_after)
    print('Y/N/E')

    def yes_or_no():
        while True:
            yes_no = input()
            yes_no = yes_no.upper()
            if yes_no == 'Y' or yes_no == 'YES':
                return True
            elif yes_no == 'N' or yes_no == 'NO':
                return False
            elif yes_no == 'E' or yes_no == 'ENTER':
                enter_pass()  # allows the user to enter a password they want to save
                yes_no == 'enter'
                user_enter = enter_pass
                return yes_no
            elif yes_no == 'EXIT':  # can always back out
                close()
            elif yes_no == 'RESTART':
                main()

    # if the return is tru then the user is prompted to input the associated username and website
    # the values are then passed into the save function
    your_answer = yes_or_no()
    if your_answer:
        username = input("User name: ",)
        associated_website = input("website: ",)
        save(username, associated_website, password_after, key)
        print("Credentials saved successfully!")
    elif your_answer == 'enter':
        username = input("User name: ",)
        associated_website = input("website: ",)
        save(username, associated_website, user_enter, key)
        print("Credentials saved successfully!")
    else:
        main()

    main()


if __name__ == '__main__':
    main()
