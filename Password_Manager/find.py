import other_things
import main
import json

# prints out a list of you password on the terminal
def password_list(key):
    continue_on = None

    try:
        with open("passwords.txt", 'r') as f:
            for line in f.readlines():
                # each credential is a json string
                credentials = json.loads(line)

                decrypted_password = main.decrypt(credentials['password'].encode(), key)
                print(f"Username: {credentials['username']}, Website: {credentials['website']}, Password: {decrypted_password}")

    except FileNotFoundError:
        print("Password file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        
    continue_on = input("type Y to continue: ", )
    continue_on = continue_on.upper()
    if continue_on == 'Y':
        main.main()
    elif continue_on == "EXIT":
        other_things.close()


# when promted it will look up a password from the user based on the username
def search_password():
    pass