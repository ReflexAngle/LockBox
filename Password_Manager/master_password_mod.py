import json
import main

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
def comapre_enter(password, key):
    has_enterd = False
    try:
        with open('master_pass.txt', 'r') as f:
            line = f.readline()  # Read the first line from the file
            credential = json.loads(line)  # Parse JSON data from the read line

            decrypt_master = main.decrypt(credential['password'].encode(), key)

            if decrypt_master == password:
                has_enterd = True
            elif decrypt_master != password:
                print("incorrect try agian")
                enter_master()
    except ValueError:
        print("incorrect try agian")
        enter_master()

    return has_enterd



def enter_master(key):
    key = key
    what_is_your_password = input("Master Password: ", )
    return comapre_enter(what_is_your_password, key)

