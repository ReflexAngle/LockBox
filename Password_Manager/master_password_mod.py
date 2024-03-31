import json
import main
import other_things

def save_master(master_pass, key):
    encrypted_password = main.encrypt(master_pass, key)
    master_password = {
        'password': encrypted_password.decode()  # Store as a string
    }
    # Save to a file, appending to the existing file
    with open('master_pass.txt', 'a') as f:
        f.write(json.dumps(master_password) + "\n")


def create_master_password(key):
    master_pass = input("Pick you master password: ",)
    save_master(master_pass, key)


# checks if the password you input is correct
def authenticate_user(app_state, key):
    password = input("Master Password: ")
    if compare_enter(password, key):
        app_state.authenticate()
        other_things.clear_screen()
        print(other_things.banner())
    else:
        print("Incorrect password. Try again.")

def compare_enter(password, key):
    try:
        with open('master_pass.txt', 'r') as f:
            line = f.readline()
            credential = json.loads(line)

            decrypt_master = main.decrypt(credential['password'].encode(), key)
            return decrypt_master == password
    except ValueError:
        print("Error during password comparison.")
        return False




def enter_master(key):
    key = key
    what_is_your_password = input("Master Password: ", )
    return comapre_enter(what_is_your_password, key)

