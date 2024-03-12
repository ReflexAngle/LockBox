import secrets

# generates a password based on the streanth that the user inputed
def generate(password_strength):

    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_characters = '!@#$%^&*()?/<>-}{[]|'

    all_chars = upper_case + lower_case + numbers + special_characters

    # Generate a password using a random sample of the characters
    password = ''.join(secrets.choice(all_chars) for _ in range(password_strength))
    return password


def enter_password():
    enter_password = input("Enter your password: ", )
    return enter_password
