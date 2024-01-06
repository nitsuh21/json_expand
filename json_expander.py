from modifiers import generate_random_id, add_prefix_suffix
import json
import random
import string

def generate_mongodb_object_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    
def expand_json(json_obj, num_objects, export, custom_fields={}):
    expanded_objects = []
    
    for _ in range(num_objects):
        expanded_obj = {}
        for key, value in json_obj.items():
            if key in custom_fields:
                if callable(custom_fields[key]):
                    expanded_obj[key] = custom_fields[key](value)
                else:
                    expanded_obj[key] = value
            else:
                if key == "_id": 
                    expanded_obj[key] = {"$oid": generate_mongodb_object_id()}
                else:
                    expanded_obj[key] = value

        expanded_objects.append(expanded_obj)
    
    if export:
        with open("expanded.json", "w") as f:
            json.dump(expanded_objects, f, indent=4)

    else:
        return expanded_objects
