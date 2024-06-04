import random

def get_new_password():
    password_base = "abcdefghjkmnpqrstuvwxyz"
    password_base_list = list(password_base)
    new_pass = random.sample(password_base_list, 10)
    new_password = ''.join(new_pass)
    return new_password


