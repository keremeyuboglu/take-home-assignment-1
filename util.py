import json

def snake_to_pascal(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

def get_seed_data():
    file_name = 'sample_data.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def convert_keys_to_pascal_case(data):
    if isinstance(data, dict):
        return {
            snake_to_pascal(k): convert_keys_to_pascal_case(v) 
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [convert_keys_to_pascal_case(item) for item in data]
    else:
        return data