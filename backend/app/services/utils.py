import random


def create_unic_name(username: str) -> str:
    number_code = ''.join(random.choices('0123456789', k=6))
    return f"{username}#{number_code}"
