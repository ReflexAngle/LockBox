import pyfiglet
import sys
import os

# I decide that the other file was getting to long and hard to read
# so why not seperate diffrent things into their own files
# this file is for seperating things that wont affect the program is it were removed
def banner():
    hello = pyfiglet.figlet_format("LockBox", font='slant')
    return hello


def help_me():
    print("HELP: for what you're looking at now")
    print("NEW: to generate a new password")
    print("ENTER: to enter an already existing password")
    print("LIST: to see list of you passwords")
    print("CLOSE: to exit the program")


def close():
    sys.exit()


# this goes in the find.py file to promt the user for cammands they can do
def find_intruct():
    print("Type S and your username or website for a search")
    print("Y or YES to leave")


def clear_screen():
    if os.name == 'nt':  # for windows
        os.system('cls')
    else:  # for unix like
        os.system('clear')
