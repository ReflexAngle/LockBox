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

# do a binary search to find the user name
def search(arr, inputed_name, key=lambda x: x):
    target = inputed_name[2:]
    
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 
        mid_val = key(arr[mid])
        if mid_val == target:
            # If found, print the result and return to exit the function.
            print(f"Found: Username: {arr[mid]['username']}, Website: {arr[mid]['website']}, Password: {arr[mid]['password']}")
            return  
        elif mid_val < target:
            low = mid + 1 
        else:
            high = mid - 1  

    search_web(arr, target, key = lambda x: x["website"])


# if a username doesnt exist then try searching for a websiteassociated
def search_web(arr, target, key = lambda x: x):
    for entry in arr:
        if key(entry) == target:
            print(f"Found: Username: {entry['username']}, Website: {entry['website']}, Password: {entry['password']}")
            return entry  
    print("Website not found.")
    return None


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
    other_things.find_intruct()
    
    def user_choice():
        substring = "S "
        substring2 = "s "
        while True:
            continue_on = input()
            if continue_on.upper() == 'Y':
                main.main()
            elif substring in continue_on or substring2 in continue_on:
                search(after_password_sorted, continue_on, key=lambda x: x['username'])
            elif continue_on.upper() == "EXIT":
                other_things.close()
            else:
                print("Enter a valid input")

    user_choice()
