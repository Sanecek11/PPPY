import json


FILENAME = "input.json"


def task() -> int:
    ...  # TODO Десериализуйте содержимое JSON файла
    with open(FILENAME, "r") as f:
        json_data = json.load(f)
        list_values = [item["contains_improvement_appeals"] for item in json_data]
    ...  # TODO Просуммируйте все значения по ключу contains_improvement_appeals
    return sum(list_values)

if __name__ == '__main__':
    print(task())
