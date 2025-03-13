import random
import re


def create_unic_name(username: str) -> str:
    number_code = ''.join(random.choices('0123456789', k=6))
    return f"{username}#{number_code}"


def check_password(pswd: str, pswd_copy: str):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[A-Za-z\d!@#$%^&*()_+={}\[\]:;"\'<>,.?~`-]{8,}$'
    if(pswd == pswd_copy):
        return bool(re.match(pattern, pswd))
    else:
        return False

