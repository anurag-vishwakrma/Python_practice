def normalize_dict(d: dict, key=""):
    final_dict = {}
    for k, v in d.items():
        parent_key = f"{key}.{k}" if key else k
        if isinstance(v, dict):
            final_dict.update(normalize_dict(v, parent_key))
        else:
            final_dict[parent_key] = v
    return final_dict


data = {
    "name":"Anurag",
    "last_name":"Vishwakrma",
    "marks":{
        "hindi":78,
        "english":89,
        "sub_subject":{
            "hindi1":23,
            "hindi2":45
        }
    }
}

print(normalize_dict(data))