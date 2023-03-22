
import json

def json_read(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def json_write(file_path, data_to_write):
    with open(file_path, 'w') as f:
        json.dump(data_to_write, f)
        