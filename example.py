from json_expander import expand_json, generate_random_id, add_prefix_suffix

json_obj = {
    "_id": {"$oid": ""},
    "bulkCode": "",
    "time": "21",
    "isActive": True,
    "locked": False,
    "woreda": "10"
}

num_objects = 3

custom_fields = {
    "id[$oid]": lambda value: generate_random_id(10),
    "bulkCode": lambda value: add_prefix_suffix(value, "AAU","",True,7),
}

expanded_objects = expand_json(json_obj, num_objects, False, custom_fields)

for obj in expanded_objects:
    print(obj)
