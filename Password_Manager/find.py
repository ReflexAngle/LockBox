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


def search(arr):
    pass


def search_web():
    pass

# prints out a list of you password on the terminal
def password_list(key):
    continue_on = None

    try:
        with open("passwords.txt", 'r') as f:
            passwords = []
            after_password_sorted = []
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
                after_password_sorted.append(entry)

           

    except FileNotFoundError:
        print("Password file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")

    # this pulls from the other_things.py file to show further instructions
    print(other_things.find_intruct())

    continue_on = input()
    continue_on = continue_on.upper()
    if continue_on == 'Y':
        main.main()
    elif continue_on == 'S':
        search(after_password_sorted)
    elif continue_on == "EXIT":
        other_things.close()
    else:
        print("Enter a valid input")
