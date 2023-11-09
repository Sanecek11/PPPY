# TODO Напишите функцию get_student_names
def get_student_names(list_):
    # list_1 = ([list_, key=lambda p: p["age"]]) не ворк
    for i in list_['name']:
        list_1.append(i)
        return list_1

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
    # TODO Вызовите функцию get_student_names
    print(get_student_names(students_list))
