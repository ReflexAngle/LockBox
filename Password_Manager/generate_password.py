import random

def generate(password_strength):

    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_characters = '!@#$%^&*()?/<>-}{[]|'

    all_chars = upper_case + lower_case + numbers + special_characters

    # Generate a password using a random sample of the characters
    password = ''.join(random.choice(all_chars) for _ in range(password_strength))
    return password