import json


def import_json_data(file_name):
    with open(file_name, 'r') as file:
        people = json.load(file)
        data = []
        for person in people:
            data.append(person)
    return data
