import pyfiglet


# I decide that the other file was getting to long and hard to read
# so why no seperate diffrent things into their own files
def banner():
    hello = pyfiglet.figlet_format("LockBox", font='slant')
    return hello


def help_me():
    print("HELP: for what you're looking at now")
    print("NEW: to generate a new password")
    print("LIST: to see list of you passwords")
    print("CLOSE: to exit the program")
