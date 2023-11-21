# TODO Напишите функцию calculate_average_age
def calculate_average_age(students: list[dict]) -> float:
    total_age = sum([student["age"] for student in students])
    avg_age = (total_age / len(students))
    return avg_age

# TODO Напишите функцию filter_students_by_age


def filter_students_by_age(students: list[dict], aver_age: float) -> list:
    filter_students = [student for student in students if student["age"] < aver_age]

    return filter_students

if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]
    # Вычисление среднего возраста
    average_age = calculate_average_age(students_list)
    # TODO Вычислите средний возраст учеников
    print("Средний возраст учеников:", average_age)

    # Фильтрация учеников по возрасту
    filtered_students = filter_students_by_age(students_list, average_age)
    # TODO Офильтруйте учеников
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filtered_students:
        print(current_student['name'])


