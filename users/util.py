from django.contrib.auth.models import User
import random
def get_new_password():
    password_base = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    password_base_list = list(password_base)
    abrakadabra = random.sample(password_base_list, 10)
    new_password = ''.join(abrakadabra)
    return new_password
