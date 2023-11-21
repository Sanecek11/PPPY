# TODO импортировать необходимые молули
import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8', errors='ignore') as c_file:
        reader = csv.DictReader(c_file, delimiter=',', lineterminator='\n')
        for row in reader:
            data.append(row)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as j_file:
        json.dump(data, j_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(INPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
!!
!!