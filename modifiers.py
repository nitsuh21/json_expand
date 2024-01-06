import random
import string

def generate_random_id(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def add_prefix_suffix(value, prefix='', suffix='', generate_random=False, length=0):
    if generate_random:
        value = generate_random_id(length)
    if prefix and suffix:
        return f"{prefix}{value}{suffix}"
    elif prefix:
        return f"{prefix}{value}"
    elif suffix:
        return f"{value}{suffix}"
    else:
        return value
