import json
import random
import string

def expand_json(json_obj, num_objects, custom_fields={}):
    expanded_objects = []

    for _ in range(num_objects):
        expanded_obj = {}
        for key, value in json_obj.items():
            if key in custom_fields:
                # Apply custom field operations
                if custom_fields[key] == "random_id":
                    expanded_obj[key] = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                elif custom_fields[key] == "user_code_prefix":
                    expanded_obj[key] = f"{custom_fields['user_code_prefix']}-{value}"
            else:
                expanded_obj[key] = value

        expanded_objects.append(expanded_obj)

    return expanded_objects
