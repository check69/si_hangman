import json


def read_json(path):
    with open(path, 'rb') as json_file:
        return json.load(json_file)
