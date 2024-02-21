import random
import os
import json
from cryptography.fernet import Fernet


def help_me():
    pass


def save_key():
    pass


def load_key():
    pass


def encrypt():
    pass


def decrypt():
    pass


# Generates the password with the provided strength for it
def generate(password_strength):

    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_characters = '!@#$%^&*()?/<>-'

    all_chars = upper_case + lower_case + numbers + special_characters

    # Generate a password using a random sample of the characters
    password = ''.join(random.choice(all_chars) for _ in range(password_strength))
    return password


# the save function allows the user to save the password and have an associated username
# and the website its for
def save(username, associated_website, password_after, key):
    pass


def load_password_list():
    pass


def main():
    
    '''key_file = "secret.key"

    # Check if the key file exists, if not, generate a new key and save it.
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)'''

    print("Hello")
    doing = input()

    # checks to see in if the inputted value is
    # if it's not then it will call the function again for the user to correct
    def valid_strength():
        while True:
            password_strength = input('Length: ')
            try:
                return int(password_strength)
            except ValueError:
                print("Please enter a valid integer.")

    password_strength = valid_strength()
    password_after = generate(password_strength)

    # asks isf the user is pleased and to save it or not
    # if it's a yes it calls the save function
    # makes sure the user inputted a valid input
    print("Is this acquitted? ", password_after)
    print('Y/N')

    def yes_or_no():
        while True:
            yes_no = input()
            yes_no = yes_no.upper()
            if yes_no == 'Y' or yes_no == 'YES':
                return True
            elif yes_no == 'N' or yes_no == 'NO':
                return False

    key = load_key()

    # if the return is tru then the user is prompted to input the associated username and website
    # the values are then passed into the save function
    your_answer = yes_or_no()
    if your_answer:
        username = input("User name: ",)
        associated_website = input("website: ",)
        save(username, associated_website, password_after, key)
        print("Credentials saved successfully!")


if __name__ == '__main__':
    main()
