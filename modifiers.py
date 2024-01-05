import random
import string

def generate_random_id(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def user_code_prefix(value, prefix, suffix):
    if prefix and suffix:
        return f"{prefix}-{value}-{suffix}"
    elif prefix:
        return f"{prefix}-{value}"
    elif suffix:
        return f"{value}-{suffix}"
    else:
        return value
