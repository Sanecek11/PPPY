# TODO решите задачу
import json
JSON_FILE = 'input.json'
result = []


def task() -> float:
    with open(JSON_FILE, "r") as f:
        json_data = json.load(f)
    total_sum = 0
    for item in json_data:
        total_sum += item["score"] * item["weight"]
    return round(total_sum, 3)


print(task())

