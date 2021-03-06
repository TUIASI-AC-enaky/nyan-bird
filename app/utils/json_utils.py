import json


def write_to_json_file(data, filename="training.json"):
    with open(filename, mode="w") as out:
        json.dump(data, out, indent=1)


def read_dict_from_json(filename="training.json"):
    try:
        with open(filename, mode="r") as input_file:
            data = json.load(input_file)
            return data
    except json.decoder.JSONDecodeError:
        return None
