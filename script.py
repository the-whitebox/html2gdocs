from dict import my_dict

def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, (dict, list)):
                    items.update(flatten_dict({str(i): item}, new_key, sep=sep))
                else:
                    items[f"{new_key}{sep}{i}"] = item
        else:
            items[new_key.replace('data_', '')] = v
    return items

def parse_complex_dict(input_dict):
    flat_data = flatten_dict(input_dict)
    return flat_data

# Example usage:
parsed_data = parse_complex_dict(my_dict)
for key, value in parsed_data.items():
    print(f"{key}  =  {value}")

