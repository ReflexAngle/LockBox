import other_things
import main
import json

# the sort is to make it eaiser to find what the user is looking for
# and if the list is printed in order it also allows for the use of a binary search 
def sorting(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    else:  # use a quick sort algorithm to accomplish the task
        pivot = arr[0]
        pivot_left = [x for x in arr[1:] if key(x) <= key(pivot)]
        pivot_right = [x for x in arr[1:] if key(x) > key(pivot)]
        return sorting(pivot_left, key) + [pivot] + sorting(pivot_right, key)

def build_hash_map(passwords):
    username_map = {}
    website_map = {}

    for entry in passwords:
        # Index by username
        username = entry['username']
        if username not in username_map:
            username_map[username] = [entry]
        else:
            username_map[username].append(entry)

        # Index by website
        website = entry['website']
        if website not in website_map:
            website_map[website] = [entry]
        else:
            website_map[website].append(entry)

    return username_map, website_map

# changed from binary search to use a hash map to search
def search_by_username(username_map, target):
    if target in username_map:
        for entry in username_map[target]:
            print_entry(entry)
    else:
        print("Username not found.")

def search_by_website(website_map, target):
    if target in website_map:
        for entry in website_map[target]:
            print_entry(entry)
    else:
        print("Website not found.")


def print_entry(entry):
    print(f"Found: Username: {entry['username']}, Website: {entry['website']}, Password: {entry['password']}")


# prints out a list of you password on the terminal
def password_list(key):
    continue_on = None

    try:
        with open("passwords.txt", 'r') as f:
            passwords = []
            for line in f.readlines():
                # each credential is a json string
                credentials = json.loads(line)

                decrypted_password = main.decrypt(credentials['password'].encode(), key)
                passwords.append({
                    'username': credentials['username'],
                    'website' : credentials['website'],
                    'password': decrypted_password
                })

            # sending the variables into the sorting algorith
            # this is to make it eaiser to read when they print
            sorted_passwords = sorting(passwords, key=lambda x: x['username'])
            for entry in sorted_passwords:
                print(f"Username: {entry['username']}, Website: {entry['website']}, Password: {entry['password']}")

            username_map, website_map = build_hash_map(passwords)

           

    except FileNotFoundError:
        print("Password file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")

    # this pulls from the other_things.py file to show further instructions
    other_things.find_intruct()

    user_choice(username_map, website_map)

def user_choice(username_map, website_map):
    while True:
        continue_on = input("Enter command: ")
        if continue_on.upper() == 'Y':
            main.main()
            break  # Assuming main.main() doesn't loop back here
        elif continue_on.upper().startswith("S "):
            target = continue_on[2:]
            search_by_username(username_map, target)  # Corrected call
            search_by_website(website_map, target)  # Corrected call
        elif continue_on.upper() == "EXIT":
            other_things.close()
            break
        else:
            print("Enter a valid input")