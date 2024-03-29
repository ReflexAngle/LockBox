import os
import json
from cryptography.fernet import Fernet
import other_things
import generate_password
import find
import master_password_mod

is_authenticated = False

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


def has_entered(key, master_password):
    global is_authenticated

    if not os.path.exists(master_password):
        master_password_mod.create_master_password(key)
    if is_authenticated == False:
        is_authenticated = master_password_mod.enter_master(key)
        print(is_authenticated)

    while not is_authenticated:
        print("Authentication failed. Please try again.")
        is_authenticated = master_password_mod.enter_master(key)
        # Optionally, include a break condition or a limit to attempts

def main():

    hello = other_things.banner()
    print(hello)

    global is_authenticated
    password_strength = None
    password_after = None
    key = None
    key_file = "secret.key"
    master_password = "master_pass.txt"
    user_enter = None 


    # Check if the key file exists, if not, generate a new key and save it.
    if not os.path.exists(key_file):
        generate_key()
        key = load_key(key_file)
    else:
        key = load_key(key_file)
        
    # checks if a master password exists
    # id it does then you will be 
    if not is_authenticated:  
        has_entered(key, master_password)

    print("Hello welcome to my password manager \ntype help for help")

    # allows the user to input what they intend to do
    # if help a list of commands appears
    # if list then shows password list
    def choose_to():
        while True:
            doing = input()
            doing = doing.upper()
            if doing == 'HELP':
                other_things.clear_screen()
                other_things.help_me()
            elif doing == 'LIST':
                other_things.clear_screen()
                find.password_list(key)
            elif doing == 'NEW':
                return doing
            elif doing == 'EXIT':
                return doing
            elif doing == 'ENTER':
                return doing
            else:
                print('input a valid command \ntype help if you dont know the commands')

    # checks to see in if the inputted value is
    # if it's not then it will call the function again for the user to correct
    def valid_strength():
        while True:
            password_strength = input('Length: ', )
            try:
                password_strength = int(password_strength)
                if password_strength < 16:  # checks password strength if they're greater than 16
                    print("seriously you should at least make your password 16 characters")
                else:  # if it is greater than 16 then it returns
                    return password_strength 
            except ValueError:
                print("Please enter a valid integer.")

    proceed = choose_to()
    if proceed == "EXIT":
        other_things.close()
    elif proceed == "NEW":
        password_strength = valid_strength()
        password_after = generate_password.generate(password_strength)
    elif proceed == "ENTER":
        password_after = generate_password.enter_password()
         

    # asks if the user is pleased and to save it or not
    # if it's a yes it calls the save function
    # makes sure the user inputted a valid input
    print("Is this acquitted? ", password_after)
    print('Y/N/ENTER')

    def yes_or_no():
        while True:
            yes_no = input()
            yes_no = yes_no.upper()
            if yes_no == 'Y' or yes_no == 'YES':
                return True
            elif yes_no == 'N' or yes_no == 'NO':
                return False
            elif yes_no == 'E' or yes_no == 'ENTER':  # allows the user to enter a password after the fact if the want to
                user_enter = generate_password.enter_password()
                return user_enter
            elif yes_no == 'EXIT':  # can always back out
                other_things.close()
            elif yes_no == 'RESTART':
                main()
            else:
                print("input a valid response")

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
        other_things.clear_screen()
        main()

    main()


if __name__ == '__main__':
    main()
