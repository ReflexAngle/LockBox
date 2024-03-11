import pyfiglet
import sys

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