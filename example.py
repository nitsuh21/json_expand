from json_expander import expand_json, generate_random_id, add_prefix_suffix

json_obj = {
    "_id": {"$oid": ""},
    "userCode": "",
    "time": "21",
    "isActive": True,
    "role": "student"
}

num_objects = 3

custom_fields = {
    "id[$oid]": lambda value: generate_random_id(10),
    "bulkCode": lambda value: add_prefix_suffix(value, "AU","",True,7),
}

expanded_objects = expand_json(json_obj, num_objects, False, custom_fields)

for obj in expanded_objects:
    print(obj)
